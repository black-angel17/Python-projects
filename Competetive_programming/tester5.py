import requests
import re


def extract_urls(webpage_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        # Fetch the content of the webpage with custom headers
        response = requests.get(webpage_url, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes

        # Get the content of the page
        content = response.text

        # Define a regex pattern for URLs
        url_pattern = re.compile(r'https?://[^\s<>"]+|www\.[^\s<>"]+')

        # Find all URLs using the regex pattern
        urls = re.findall(url_pattern, content)

        return urls
    except requests.RequestException as e:
        print(f"Error fetching {webpage_url}: {e}")
        return []


if __name__ == "__main__":
    webpage_url = input("Enter the URL of the webpage to extract URLs from: ")
    urls = extract_urls(webpage_url)

    if urls:
        print("\nExtracted URLs:")
        for url in urls:
            print(url)
    else:
        print("No URLs found or an error occurred.")
