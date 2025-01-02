# AIO-Scraper 
# (All-in-One High Quality Proxy Scraper)

**AIO-Scraper** is a Python-based proxy scraper that aggregates high-quality proxies from multiple sources. This tool allows you to download and save proxies from a variety of proxy lists, including HTTP, HTTPS, SOCKS4, and SOCKS5 proxies. It ensures that duplicate proxies are removed, saving only unique proxies to local files for later use. 

With an easy-to-use interface, AIO-Scraper offers both automatic and manual scraping modes, giving you flexibility in how you wish to use the tool. The scraper allows you to specify the interval for automatic scraping, ensuring regular updates to your proxy lists.

## Features

- **Proxy Collection**: Download proxies from multiple trusted sources, categorized by protocol type (HTTP, HTTPS, SOCKS4, SOCKS5).
- **Automatic Scraping**: Schedule proxy scraping at user-defined intervals (e.g., 5, 10, 20, 60 minutes).
- **Manual Scraping**: Option to run the scraper manually whenever needed.
- **Unique Proxies**: Automatically removes duplicate proxies to ensure only unique ones are saved.
- **Multiple Proxy Types**: Supports downloading HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.
- **User Interface**: Simple and interactive interface that guides the user through the process.
- **Easy-to-Use**: You can choose between manual and automatic scraping modes based on your preferences.

## How It Works

AIO-Scraper fetches proxy lists from various online repositories and saves them locally. It checks multiple sources for updated proxies and merges the results into different categories: `http.txt`, `https.txt`, `socks4.txt`, and `socks5.txt`. 

The script allows you to either run the scraper manually or automatically with periodic intervals. It uses the `requests` library to fetch proxy data and handles proxy uniqueness by eliminating duplicates before saving the final lists to disk.

## Requirements

- Python 3.x
- `requests`: For making HTTP requests to fetch proxy lists.
- `termcolor`: For colorful terminal output.

You can install the required dependencies using `pip`:

```bash
pip install requests termcolor
