<div id="top"></div>

[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<br />
<div align="center">
  <!-- <a href="https://github.com/Devansh-ops/Whatsapp-Message/">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a> -->

  <h3 align="center">WhatsApp Bulk Messenger</h3>

  <p align="center">
    Python Script to send bulk whatsapp message via chrome!
    <!-- <br />
    <a href="https://github.com/Devansh-ops/Whatsapp-Message"><strong>Explore the docs »</strong></a> -->
    <br />
    <br />
    <!-- <a href="https://github.com/Devansh-ops/Whatsapp-Message">View Demo</a>
    · -->
    <a href="https://github.com/Devansh-ops/Whatsapp-Message/issues">Report Bug</a>
    ·
    <a href="https://github.com/Devansh-ops/Whatsapp-Message/issues">Request Feature</a>
  </p>
</div>

<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#features">Features</a></li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>

## About The Project

The project was first built out of neccesity while sending messages to hundreds of people for an online event conducted by [Sigma Xi VIT](https://github.com/SIGMA-XI-VIT)
Later, it was updated to run in automatically and headlessly, so we could use our time more wisely.

If you find this script useful, please leave a ⭐
<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

<p align="right">(<a href="#top">back to top</a>)</p>

### Built With

* [Python](https://www.python.org/)
* [Selenium](https://selenium.dev/)

<p align="right">(<a href="#top">back to top</a>)</p>

## Getting Started

To get a local copy up and running follow these simple example steps.

### Prerequisites
Make sure to add both to the PATH
* [Python 3](https://www.python.org/downloads/) 
* [Git](https://git-scm.com/downloads) (optional) 

To get the repository, either download the ZIP folder from Code and extract it, or clone the repository via git using

`git clone https://github.com/Devansh-ops/Whatsapp-Message.git`
### Installation

Move into the folder

`cd Whatsapp-Message`

To install dependencies type:

`pip install -r requirements.txt`

<p align="right">(<a href="#top">back to top</a>)</p>

## Features
- Modular - can be imported
- Fast - Default run in headless mode
- CLI - Takes input from the terminal 
- Error logging and screenshots

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- USAGE EXAMPLES -->
## Usage
<!-- 
_For more examples, please refer to the [Documentation](https://example.com)_ -->

### Basic Usage
`python script.py <EXCEL SHEET> <TEXT FILE>`

You might want to specify the column containing the numbers via the `-c` flag ( 0-based indexing )

For more usage details, Type `python script.py --help`

```
usage: script.py [-h] [-c COLUMN] [-d DELAY] [-s] [-e EXTENSION] [--screenshot SCREENSHOT] [-z] file [message]

positional arguments:
  file                  Path to Excel file containing numbers to send message to
  message               Text file containing message to send

options:
  -h, --help            show this help message and exit
  -c COLUMN, --column COLUMN
                        Column name or number where numbers are located
  -d DELAY, --delay DELAY
                        Time (in seconds) to wait after sending the message. Default = 4
  -s, --string          Treat message as string input
  -e EXTENSION, --extension EXTENSION
                        Change default phone extention. Default is Indian: 91
  --screenshot SCREENSHOT
                        Defines error screenshot folder
  -z, --head            Runs without headless mode
```
<p align="right">(<a href="#top">back to top</a>)</p>

<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Clone it locally (`git clone https://github.com/<YOUR-USERNAME>/Whatsapp-Message.git`)
2. <a href="#installation"> Install </a> the dependencies
4. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#top">back to top</a>)</p>

<!-- LICENSE -->
## License

Distributed under the BSD 3-Clause License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Devansh Sehgal - [@covfebeforecode](https://twitter.com/covfebeforecode) - devanshsehgal@gmail.com

Project Link: [https://github.com/Devansh-ops/Whatsapp-Message](https://github.com/Devansh-ops/Whatsapp-Message)

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* [Choose an Open Source License](https://choosealicense.com)
* [Img Shields](https://shields.io)
* [PyQRCode](https://pypi.org/project/PyQRCode/)
* [Best-README-Template](https://github.com/othneildrew/Best-README-Template)

<p align="right">(<a href="#top">back to top</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/Devansh-ops/Whatsapp-Message.svg?style=for-the-badge
[contributors-url]: https://github.com/Devansh-ops/Whatsapp-Message/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/Devansh-ops/Whatsapp-Message.svg?style=for-the-badge
[forks-url]: https://github.com/Devansh-ops/Whatsapp-Message/network/members
[stars-shield]: https://img.shields.io/github/stars/Devansh-ops/Whatsapp-Message.svg?style=for-the-badge
[stars-url]: https://github.com/Devansh-ops/Whatsapp-Message/stargazers
[issues-shield]: https://img.shields.io/github/issues/Devansh-ops/Whatsapp-Message.svg?style=for-the-badge
[issues-url]: https://github.com/Devansh-ops/Whatsapp-Message/issues
[license-shield]: https://img.shields.io/github/license/Devansh-ops/Whatsapp-Message.svg?style=for-the-badge
[license-url]: https://github.com/Devansh-ops/Whatsapp-Message/blob/main/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/devansh-sehgal/
<!-- [product-screenshot]: images/screenshot.png -->
