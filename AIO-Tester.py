import os
import requests
import socks
import socket
from requests.exceptions import RequestException

# Function to test a proxy (HTTP, HTTPS, SOCKS4, SOCKS5)
def test_proxy(proxy, proxy_type='http'):
    url = 'http://www.google.com'  # Test with a simple URL
    proxies = {}

    # Configure the proxy type
    if proxy_type in ['http', 'https']:
        proxies = {
            'http': proxy,
            'https': proxy
        }
    elif proxy_type == 'socks4':
        proxies = {
            'http': f'socks4://{proxy}',
            'https': f'socks4://{proxy}'
        }
    elif proxy_type == 'socks5':
        proxies = {
            'http': f'socks5://{proxy}',
            'https': f'socks5://{proxy}'
        }

    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        if response.status_code == 200:
            print(f"Proxy {proxy} ({proxy_type.upper()}) is working!")
        else:
            print(f"Proxy {proxy} ({proxy_type.upper()}) failed with status code: {response.status_code}")
    except RequestException:
        print(f"Proxy {proxy} ({proxy_type.upper()}) is not working.")

# Function to read proxies from multiple files and extract the proxy address (ignore extra info)
def load_proxies_from_files(file_paths):
    proxies = {'http': [], 'https': [], 'socks4': [], 'socks5': []}
    
    for file_path in file_paths:
        print(f"Checking if file exists: {file_path}")
        if os.path.exists(file_path):
            with open(file_path, 'r') as file:
                # Extract proxies from each file
                for line in file.readlines():
                    if line.strip():
                        proxy_details = line.strip().split(':')
                        ip_port = f"{proxy_details[0]}:{proxy_details[1]}"
                        if len(proxy_details) == 2:  # Basic HTTP/Socks proxy
                            proxies['http'].append(ip_port)
                        elif len(proxy_details) == 3:  # With country information
                            proxies['http'].append(ip_port)
        else:
            print(f"File {file_path} does not exist.")
    return proxies

# Print the current working directory to confirm where the script is running
print(f"Current Working Directory: {os.getcwd()}")

# List all files in the current directory to confirm if proxy files are there
print("Listing all files in the current directory:")
print(os.listdir(os.getcwd()))

# List of paths to the files containing proxies (use relative paths or absolute paths)
file_paths = ['http.txt', 'https.txt', 'socks4.txt', 'socks5.txt']  # Modify this list as necessary

# Load proxies from the files
proxies_dict = load_proxies_from_files(file_paths)

# Test each proxy in the list
for proxy in proxies_dict['http']:
    test_proxy(proxy, 'http')

for proxy in proxies_dict['https']:
    test_proxy(proxy, 'https')

for proxy in proxies_dict['socks4']:
    test_proxy(proxy, 'socks4')

for proxy in proxies_dict['socks5']:
    test_proxy(proxy, 'socks5')
