# AIO-Scraper

# **AIO-Scraper** is a Python-based proxy scraper and testing tool that aggregates high-quality proxies from multiple sources.
# This tool allows you to download, test, and save proxies from various lists, including HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.
# It ensures that duplicate proxies are removed, saving only unique proxies to local files for later use.

# In addition to scraping proxies, AIO-Scraper includes a proxy testing feature that verifies the functionality of proxies from text files,
# allowing you to check if the proxies are working across different protocols.

# With an easy-to-use interface, AIO-Scraper offers both automatic and manual scraping modes, giving you flexibility in how you wish to use the tool.
# The scraper allows you to specify the interval for automatic scraping, ensuring regular updates to your proxy lists.

## Features
# - **Proxy Collection**: Download proxies from multiple trusted sources, categorized by protocol type (HTTP, HTTPS, SOCKS4, SOCKS5).
# - **Automatic Scraping**: Schedule proxy scraping at user-defined intervals (e.g., 5, 10, 20, 60 minutes).
# - **Manual Scraping**: Option to run the scraper manually whenever needed.
# - **Unique Proxies**: Automatically removes duplicate proxies to ensure only unique ones are saved.
# - **Proxy Testing**: Test proxies (HTTP, HTTPS, SOCKS4, SOCKS5) to check if they are working with a real URL request.
# - **Multiple Proxy Types**: Supports downloading and testing HTTP, HTTPS, SOCKS4, and SOCKS5 proxies.
# - **User Interface**: Simple and interactive interface that guides the user through the process.
# - **Easy-to-Use**: You can choose between manual and automatic scraping modes based on your preferences.

## How It Works
# AIO-Scraper fetches proxy lists from various online repositories, saves them locally, and tests them for functionality.
# The script checks multiple sources for updated proxies and merges the results into different categories: `http.txt`, `https.txt`, `socks4.txt`, and `socks5.txt`.

# The scraper can run in two modes:
# 1. **Manual Scraping**: Run the scraper on-demand to fetch proxies immediately.
# 2. **Automatic Scraping**: Set a periodic interval for automatic scraping (e.g., every 5, 10, 20, or 60 minutes).

# Additionally, you can test proxies from the saved `.txt` files to ensure they are working.
# The proxy testing feature checks proxies for each protocol (HTTP, HTTPS, SOCKS4, SOCKS5) and reports whether the proxies are functional.

## Requirements
# - Python 3.x
# - `requests`: For making HTTP requests to fetch proxy lists and test proxies.
# - `termcolor`: For colorful terminal output.

# You can install the required dependencies using `pip`:

pip install requests termcolor

## Usage

### Clone the Repository:
```bash
git clone https://github.com/yourusername/AIO-Scraper.git
cd AIO-Scraper
