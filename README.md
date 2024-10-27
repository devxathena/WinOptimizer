# WinOptimizer
A powerful, professional-grade toolkit designed for Windows optimization and automation. Automatically fetches and deploys the latest tools, scripts, and repositories for Windows performance enhancements, system maintenance, debloating, and security improvements. Perfect for IT professionals and enthusiasts seeking a streamlined solution for optimizing and managing Windows environments.

[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/downloads/)
[![AsyncIO](https://img.shields.io/badge/Async-Enabled-green.svg)](https://docs.python.org/3/library/asyncio.html)


## Overview

**WinOptimize-Downloader** is a sophisticated Python-based utility tailored to facilitate the downloading and extraction of Windows optimization tools and scripts directly from various GitHub repositories and Sysinternals. Designed for efficiency and user-friendliness, this tool automates the entire process, ensuring that users have access to the latest versions of essential tools for optimizing their Windows environments.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Output](#output)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Features

- **Asynchronous Downloads**: Utilizes `aiohttp` for concurrent downloading, significantly reducing overall wait time compared to synchronous methods.
- **Latest Release Retrieval**: Automatically fetches the latest release of each specified GitHub repository, utilizing the GitHub API for efficiency.
- **Branch Fallback**: If no release is available, the tool automatically defaults to downloading the primary branch, ensuring that users can still access the latest code.
- **Sysinternals Suite Download**: Seamlessly integrates with the Sysinternals Suite, downloading the latest version to provide essential Windows utilities.
- **Rich Console Output**: Employs the `rich` library for visually appealing and informative logging, enhancing the user experience during operations.
- **Organized File Structure**: Downloads are organized into clearly defined directories, simplifying file management for users.


## Installation

1. Clone the repository:
```
git clone https://github.com/devxathena/WinOptimizer.git
cd WinOptimizer
```

2. Install required packages:
Ensure you have Python 3.7 or higher installed. Use `pip` to install the necessary packages listed in `requirements.txt`.
```
pip install -r requirements.txt
```

## Configuration

1. Set your GitHub token in the script. This token is necessary for accessing private repositories and API rate limits. You can create a personal access token in your GitHub account settings under Developer Settings > Personal access tokens.

2. Modify the `DESKTOP_PATH` variable if you want to change the download location.
```
python WinOptimizer.py
```

## Output

Upon successful execution, the tool will:

- Download the Sysinternals Suite and extract it into the specified directory.
- Iterate through each GitHub repository, downloading the latest releases or default branches, and extracting them as necessary.
- Log all operations to the console, displaying successful downloads and any errors encountered.

## Contributing

Contributions are welcomed and encouraged! Here’s how you can help:

1. Fork the repository to your GitHub account.
2. Create a new branch for your feature or fix:
```
git checkout -b feature/YourFeature
```

3. Make your changes and commit them:
```
git commit -m "Add your message here"
```

4. Push to your branch:
```
git push origin feature/YourFeature
``` 

5. Submit a pull request with a description of your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- Special thanks to the developers of the libraries utilized in this project:
- **aiohttp**: A popular asynchronous HTTP client for Python, enabling efficient network operations.
- **rich**: A Python library for rich text and beautiful formatting in the terminal, enhancing console logging.
- **zipfile**: A built-in Python library for reading and writing zip files, utilized for extracting downloaded content.
- Thanks to the contributors and maintainers of the GitHub repositories and Sysinternals Suite that this tool interacts with.

## Requirements

Ensure that the following packages are included in your `requirements.txt` for smooth operation:
```
aiohttp
rich
```

## Additional Information

- **Python Version**: The script requires Python 3.7 or higher for compatibility with asynchronous features.
- **Operating System**: While designed primarily for Windows, this script should run on any operating system that supports Python.

Feel free to reach out for any questions or suggestions!
