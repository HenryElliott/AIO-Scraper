# AIO-Scraper

**AIO-Scraper** is a Python-based proxy scraper and testing tool that aggregates high-quality proxies from multiple sources. This tool allows you to download, test, and save proxies from various lists, including HTTP, HTTPS, SOCKS4, and SOCKS5 proxies. It ensures that duplicate proxies are removed, saving only unique proxies to local files for later use.

In addition to scraping proxies, AIO-Scraper includes a proxy testing feature that verifies the functionality of proxies from text files, allowing you to check if the proxies are working across different protocols.

With an easy-to-use interface, AIO-Scraper offers both automatic and manual scraping modes, giving you flexibility in how you wish to use the tool. The scraper allows you to specify the interval for automatic scraping, ensuring regular updates to your proxy lists.

## Features

- **Proxy Collection**: Download proxies from multiple trusted sources, categorized by protocol type (HTTP, HTTPS, SOCKS4, SOCKS5).
- **Automatic Scraping**: Schedule proxy scraping at user-defined intervals (e.g., 5, 10, 20, 60 minutes).
- **Manual Scraping**: Option to run the scraper manually whenever needed.
- **Unique Proxies**: Automatically removes duplicate proxies to ensure only unique ones are saved.
- **Proxy Testing**: Test proxies (HTTP, HTTPS, SOCKS4, SOCKS5) to check if they are working with a real URL request.
- **Multiple Proxy Types**: Supports downloading and testing HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.
- **User Interface**: Simple and interactive interface that guides the user through the process.
- **Easy-to-Use**: You can choose between manual and automatic scraping modes based on your preferences.

## How It Works

AIO-Scraper fetches proxy lists from various online repositories, saves them locally, and tests them for functionality. The script checks multiple sources for updated proxies and merges the results into different categories: `http.txt`, `https.txt`, `socks4.txt`, and `socks5.txt`.

The scraper can run in two modes:
1. **Manual Scraping**: Run the scraper on-demand to fetch proxies immediately.
2. **Automatic Scraping**: Set a periodic interval for automatic scraping (e.g., every 5, 10, 20, or 60 minutes).

Additionally, you can test proxies from the saved `.txt` files to ensure they are working. The proxy testing feature checks proxies for each protocol (HTTP, HTTPS, SOCKS4, SOCKS5) and reports whether the proxies are functional.

## Requirements

- `Python 3.x`
- `requests`: For making HTTP requests to fetch proxy lists and test proxies.
- `termcolor`: For colorful terminal output.

You can install the required dependencies using `pip`:

```bash
pip install requests termcolor
```
# Usage
Clone the Repository:
```bash
git clone https://github.com/yourusername/AIO-Scraper.git
cd AIO-Scraper
```
# Run the Script:
You can run the script manually or automatically.

Automatic Scraping:
The script will run at user-defined intervals to fetch proxies.

Manual Scraping:
Run the script to scrape proxies only once.

# To start the script, simply run:

```bash
python aio_scraper.py
```
# Choose the Mode:
Manual Mode: Scrape proxies immediately.
Auto Mode: Set the interval for periodic scraping (e.g., every 5, 10, 20, or 60 minutes).
Proxy Testing:
The script will test the proxies (HTTP, HTTPS, SOCKS4, SOCKS5) from the proxy text files you provide and check if they are working with a real HTTP request.

Configuration:
The script allows you to modify the proxy URLs or adjust the scraping intervals directly within the code.

Example Output
When you run the script, you will see messages indicating the status of the proxy download process:

```bash
Downloaded proxies from https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt
Saved 150 unique proxies to http.txt
```
Additionally, if you're testing proxies, you will see:

```bash
Proxy 27.79.155.220:16000 (HTTP) is working!
Proxy 67.43.227.227:18819 (SOCKS5) is not working.
```
# Contributing
If you'd like to contribute to the project, feel free to fork the repository, make changes, and submit a pull request.

