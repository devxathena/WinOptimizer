import os
import aiohttp
import asyncio
import zipfile
from pathlib import Path
from rich.console import Console
from rich.logging import RichHandler
import logging

# Logger configuration
console = Console()
logging.basicConfig(
    level=logging.INFO,
    format='%(message)s',
    handlers=[RichHandler(console=console)]
)
logger = logging.getLogger("Downloader")

# Set GitHub token and desktop path
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN_HERE'  # Replace with your actual GitHub token
DESKTOP_PATH = Path.home() / "Desktop" / "WinOptimizer"
DESKTOP_PATH.mkdir(parents=True, exist_ok=True)

# List of repositories to download and Sysinternals URLs
repos = [
    "https://github.com/meetrevision/playbook",
    "https://github.com/Atlas-OS/Atlas",
    "https://github.com/microsoft/devhome",
    "https://github.com/CorentinTh/it-tools",
    "https://github.com/massgravel/Microsoft-Activation-Scripts",
    "https://github.com/ChrisTitusTech/winutil",
    "https://github.com/OgnitorenKs/Toolbox",
    "https://github.com/hellzerg/optimizer",
    "https://github.com/just-maik/win-opti-resources",
    "https://github.com/DuckyOnQuack-999/WinKit",
    "https://github.com/Marvin700/Windows_Optimisation_Pack",
    "https://github.com/azurejoga/Aurora-Windows-Optimizer",
    "https://github.com/semazurek/ET-Optimizer",
    "https://github.com/rayenghanmi/RyTuneX",
    "https://github.com/caxzy/LynxOptimizer",
    "https://github.com/LightMode00/Hone-Optimizer",
    "https://github.com/Greedeks/GTweak",
    "https://github.com/mrandcris/WIN10-OPTIMIZER",
    "https://github.com/Parcoil/Sparkle",
    "https://github.com/Kuuuuuuuu/Tweaks",
    "https://github.com/hasanalt/Windows-Optimizer",
    "https://github.com/DevToys-app/DevToys",
    "https://github.com/gordonbay/Windows-On-Reins",
    "https://github.com/PublicSatanicVoid/WindowsPowerWash",
    "https://github.com/Raphire/Win11Debloat",
    "https://github.com/farag2/Sophia-Script-for-Windows",
    "https://github.com/LeDragoX/Win-Debloat-Tools",
    "https://github.com/awesome-windows11/windows11",
    "https://github.com/99natmar99/Windows-11-Fixer",
    "https://github.com/rcmaehl/NotCPUCores",
    "https://github.com/farag2/Utilities",
    "https://github.com/svenmauch/WinSlap",
    "https://github.com/SanGraphic/QuickBoost",
    "https://github.com/equk/windows",
    "https://github.com/TairikuOokami/Windows",
    "https://github.com/denis-g/windows10-latency-optimization",
    "https://github.com/alfinauzikri/WinCustom",
    "https://github.com/ancel1x/Ancels-Performance-Batch",
    "https://github.com/Jisll/windows11",
    "https://github.com/alfaaarex/awesome-tweaks",
    "https://github.com/Zusier/Zusiers-optimization-Batch",
    "https://github.com/Ec-25/FixIt",
    "https://github.com/Jisll/Sadcoy",
    "https://github.com/Batlez/Batlez-Tweaks",
    "https://github.com/Teramanbr/TerabyteTweaker",
    "https://github.com/leetfin/Windows10Tools",
    "https://github.com/WinTweaks/windows-optimization",
    "https://github.com/Foulest/RepairKit",
    "https://github.com/Empyreal96/win-10-services-toolbox",
    "https://github.com/2rf/winGetDebloated",
    "https://github.com/iamtraction/WindowsRegistry",
    "https://github.com/zoicware/ZOICWARE",
    "https://github.com/AFaustini/OtimizeWindows",
    "https://github.com/ehsan18t/Win10-Ultimate-System-Tweaks",
    "https://github.com/felikcat/W11Boost",
    "https://github.com/shoober420/windows11-scripts",
    "https://github.com/K3V1991/Increase-Perfomance-on-Windows",
    "https://github.com/TheDoctorTash/MegaTweakPack",
    "https://github.com/buxh/ZER0-Batch-Optimizer",
    "https://github.com/Jisll/Sadeaner",
    "https://github.com/zoicware/RepairBadTweaks",
    "https://github.com/AzhamProdLive/WPC-Useful-Box",
    "https://github.com/christopherhowe02/Debloat10",
    "https://github.com/SegoCode/DebloBat",
    "https://github.com/vukilis/Windows11-Optimizer-Debloater",
    "https://github.com/PusPC/Pus",
    "https://github.com/ivandfx/DFXWinTweaks",
    "https://github.com/kubsonxtm/Windows-Tweaks",
    "https://github.com/Batch-o-Taco/UBC",
    "https://github.com/emylfy/simplify11",
    "https://github.com/RickyDevs/QOptimizer",
    "https://github.com/DavoDC/WindowsFiles",
    "https://github.com/aazhbd/WinDecluttered",
    "https://github.com/0000xFFFF/reghacks",
    "https://github.com/MartinLXXX6/The-Windows-Suite",
    "https://github.com/SchooiCodes/smt",
    "https://github.com/DevSentinel/SentinelsToolbox",
    "https://github.com/equk/w10_gaming",
    "https://github.com/DestroyerDarkNess/StrelyCleaner",
    "https://github.com/Empyreal96/win-10-toolbox-gui",
    "https://github.com/waylaa/WindowsOptimizations",
    "https://github.com/kubsonxtm/Windows-Tweaks",
    "https://github.com/mattreecebentley/Windows-10-11-Simplifier",
    "https://github.com/teeotsa/windows-11-debloat",
    "https://github.com/teeotsa/windows-10-debloat",
    "https://github.com/mrandcris/WIN10-OPTIMIZER",
    "https://github.com/ionuttbara/melody_windows"
]

# Sysinternals and AME Wizard URLs
sysinternals_url = "https://download.sysinternals.com/files/SysinternalsSuite.zip"
ame_wizard_url = "https://download.ameliorated.io/AME%20Wizard%20Beta.zip"

# Set headers for GitHub API access
headers = {"Authorization": f"token {GITHUB_TOKEN}"}

async def download_file(session, url, dest_path):
    """Download a file and log the process."""
    async with session.get(url) as response:
        if response.status == 200:
            with open(dest_path, 'wb') as file:
                file.write(await response.read())
            logger.info(f"[bold green]Downloaded file:[/bold green] {dest_path}")
        else:
            logger.error(f"[bold red]Download failed (status {response.status}):[/bold red] {url}")

async def fetch_latest_release(session, repo_owner, repo_name):
    """Fetch the latest release link from the GitHub API."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/releases/latest"
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            release = await response.json()
            assets = release.get("assets", [])
            if assets:
                return assets[0]["browser_download_url"]
        return None

async def get_default_branch(session, repo_owner, repo_name):
    """Get the default branch name from GitHub."""
    url = f"https://api.github.com/repos/{repo_owner}/{repo_name}"
    async with session.get(url, headers=headers) as response:
        if response.status == 200:
            repo_info = await response.json()
            return repo_info.get("default_branch", "main")
        return "main"

async def process_repo(session, repo_url):
    """Process downloading the latest release or the default branch from the given repo URL."""
    repo_owner, repo_name = repo_url.strip("/").split("/")[-2:]
    dest_folder = DESKTOP_PATH / f"{repo_name}_{repo_owner}"
    dest_folder.mkdir(parents=True, exist_ok=True)

    release_url = await fetch_latest_release(session, repo_owner, repo_name)
    if release_url:
        await download_file(session, release_url, dest_folder / release_url.split("/")[-1])
    else:
        default_branch = await get_default_branch(session, repo_owner, repo_name)
        await download_repo(session, repo_owner, repo_name, dest_folder, default_branch)
    logger.info(f"[bold blue]Completed repo:[/bold blue] {repo_name}")

async def download_repo(session, repo_owner, repo_name, dest_folder, branch):
    """Download the zip file from the default branch."""
    repo_url = f"https://codeload.github.com/{repo_owner}/{repo_name}/zip/refs/heads/{branch}"
    await download_file(session, repo_url, dest_folder / f"{repo_name}.zip")

async def download_and_extract(session, url, folder_name):
    """Download a file and extract it."""
    zip_path = DESKTOP_PATH / f"{folder_name}.zip"
    await download_file(session, url, zip_path)
    dest_folder = DESKTOP_PATH / folder_name
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(dest_folder)
    zip_path.unlink()
    logger.info(f"[bold yellow]{folder_name} downloaded and extracted.[/bold yellow]")

async def main():
    """Main function to perform download operations."""
    async with aiohttp.ClientSession() as session:
        tasks = [
            download_and_extract(session, sysinternals_url, "SysinternalsSuite"),
            download_and_extract(session, ame_wizard_url, "AME_Wizard_Beta")
        ]
        for repo in repos:
            tasks.append(process_repo(session, repo))
        await asyncio.gather(*tasks)

if __name__ == "__main__":
    asyncio.run(main())