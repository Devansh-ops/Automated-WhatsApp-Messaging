# Whatsapp-Message
Python Script to send whatsapp message via chrome

To install dependencies type:

`pip install -r requirements.txt`

chromedriver version uploaded - [ChromeDriver 103.0.5060.53](https://chromedriver.storage.googleapis.com/index.html?path=103.0.5060.53/)

- Supports Chrome version 103

## Help
Type `python3 script.py --help` for usage details

```
usage: script.py [-h] [-c COLUMN] [-d DELAY] file [message]

positional arguments:
  file                  Path to Excel file containing numbers to send message to
  message               String or Text file containing message to send

options:
  -h, --help            show this help message and exit
  -c COLUMN, --column COLUMN
                        Column name or number where numbers are located
  -d DELAY, --delay DELAY
                        Time (in seconds) to wait after sending the message. Default = 3
```
