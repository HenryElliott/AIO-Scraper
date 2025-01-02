import requests
import time
import os
from termcolor import colored

# Define the URLs and corresponding filenames
urls = {
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/http/global/http_checked.txt": "http.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks4/global/socks4_checked.txt": "socks4.txt",
    "https://raw.githubusercontent.com/elliottophellia/yakumo/master/results/socks5/global/socks5_checked.txt": "socks5.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/http.txt": "http.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/https.txt": "https.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks4.txt": "socks4.txt",
    "https://raw.githubusercontent.com/mmpx12/proxy-list/master/socks5.txt": "socks5.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/http.txt": "http.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks4.txt": "socks4.txt",
    "https://raw.githubusercontent.com/yemixzy/proxy-list/main/proxies/socks5.txt": "socks5.txt",
    "https://raw.githubusercontent.com/proxy4parsing/proxy-list/main/http.txt": "http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/http.txt": "http.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/https.txt": "https.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks4.txt": "socks4.txt",
    "https://raw.githubusercontent.com/Zaeem20/FREE_PROXIES_LIST/master/socks5.txt": "socks5.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/http/data.txt": "http.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks4/data.txt": "socks4.txt",
    "https://raw.githubusercontent.com/proxifly/free-proxy-list/main/proxies/protocols/socks5/data.txt": "socks5.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/http.txt": "http.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks4.txt": "socks4.txt",
    "https://raw.githubusercontent.com/MuRongPIG/Proxy-Master/main/socks5.txt": "socks5.txt",
    "https://raw.githubusercontent.com/NotUnko/autoproxies/main/proxies/https": "https.txt",
    "https://raw.githubusercontent.com/NotUnko/autoproxies/main/proxies/socks4": "socks4.txt",
    "https://raw.githubusercontent.com/NotUnko/autoproxies/main/proxies/socks5": "socks5.txt",
    "https://raw.githubusercontent.com/hookzof/socks5_list/master/proxy.txt": "socks5.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/http.txt": "http.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/https.txt": "https.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks4.txt": "socks4.txt",
    "https://raw.githubusercontent.com/ErcinDedeoglu/proxies/main/proxies/socks5.txt": "socks5.txt",
    "https://raw.githubusercontent.com/im-razvan/proxy_list/main/http.txt": "http.txt",
    "https://raw.githubusercontent.com/im-razvan/proxy_list/main/socks5.txt": "socks5.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/http.txt": "http.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/https.txt": "https.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks4.txt": "socks4.txt",
    "https://raw.githubusercontent.com/zloi-user/hideip.me/main/socks5.txt": "socks5.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/http.txt": "http.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/https.txt": "https.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks4.txt": "socks4.txt",
    "https://raw.githubusercontent.com/vakhov/fresh-proxy-list/master/socks5.txt": "socks5.txt"
}

# Function to download and save proxies
def download_proxies(urls):
    proxies = {"http.txt": set(), "https.txt": set(), "socks4.txt": set(), "socks5.txt": set()}
    for url, filename in urls.items():
        try:
            response = requests.get(url)
            response.raise_for_status()
            fetched_proxies = set(response.text.strip().split('\n'))
            proxies[filename].update(fetched_proxies)
            print(colored(f"Downloaded proxies from {url}", "red"))
        except requests.exceptions.RequestException as e:
            print(colored(f"Failed to download from {url}: {e}", "green"))
    return proxies

# Function to save proxies to files and remove duplicates
def save_proxies(proxies):
    for filename, proxy_set in proxies.items():
        with open(filename, 'w', encoding='utf-8') as file:  # Specify utf-8 encoding
            file.write('\n'.join(proxy_set))
        print(colored(f"Saved {len(proxy_set)} unique proxies to {filename}", "cyan"))

# Function to run the download and save process
def run_proxy_downloader():
    proxies = download_proxies(urls)
    save_proxies(proxies)

# Function to ask the user for the mode of operation
def get_user_choice():
    print(colored(" /$$ /$$$$$$$                                        ", "red"))
    print(colored("|__/| $$__  $$                                       ", "red"))
    print(colored(" /$$| $$  \ $$ /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$", "red"))
    print(colored("| $$| $$$$$$$//$$__  $$ /$$__  $$|  $$ /$$/| $$  | $$", "red"))
    print(colored("| $$| $$____/| $$  \__/| $$  \ $$ \  $$$$/ | $$  | $$", "red"))
    print(colored("| $$| $$     | $$      | $$  | $$  >$$  $$ | $$  | $$", "red"))
    print(colored("| $$| $$     | $$      |  $$$$$$/ /$$/\  $$|  $$$$$$$", "red"))
    print(colored("|__/|__/     |__/       \______/ |__/  \__/ \____  $$", "red"))
    print(colored("                                            /$$  | $$", "red"))
    print(colored("                                           |  $$$$$$/", "red"))
    print(colored("                                            \______/ ", "red"))
    print(colored("Coded by: Lucifer", "red"))
    print(colored("Do you want to run the script manually or automatically?", "yellow"))
    choice = input("Enter 'manual' or 'auto': ").strip().lower()
    return choice

# Function to get the interval from the user
def get_interval():
    print(colored("Suggested intervals: 5, 10, 20, 60 minutes", "yellow"))
    try:
        interval = int(input("Enter the interval in minutes: "))
        return interval * 60  # Convert minutes to seconds
    except ValueError:
        print(colored("Invalid input. Please enter a number.", "red"))
        return get_interval()

# Main function
def main():
    user_choice = get_user_choice()
    if user_choice == 'auto':
        interval = get_interval()
        while True:
            run_proxy_downloader()
            time.sleep(interval)
    elif user_choice == 'manual':
        run_proxy_downloader()
    else:
        print(colored("Invalid choice. Please run the script again and enter 'manual' or 'auto'.", "red"))

if __name__ == "__main__":
    main()