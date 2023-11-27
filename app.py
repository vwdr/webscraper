import requests
from bs4 import BeautifulSoup
import re


def web_scraper(url, pattern):
    """
    A function that can scrape the web using regular expressions

    Parameters:
        url (str): The url to scrape
        pattern (str): The regular expression pattern to search for

    Returns:
        list: A list of all the matches found on the page
    """
    try:
        # Make a request to the website
        r = requests.get(url)

        # Get the content of the request
        soup = BeautifulSoup(r.content, 'html.parser')

        # Get all the text from the page
        page_text = soup.get_text()

        # Use the regular expression pattern to find matches in the page text
        matches = re.findall(pattern, page_text)

        return matches

    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    url = input("Enter the url to scrape: ")
    pattern = input("Enter the regular expression pattern to search for: ")

    results = web_scraper(url, pattern)

    if results:
        print(f"Found {len(results)} matches:")
        for i, match in enumerate(results, start=1):
            print(f"Match {i}: {match}")
    else:
        print("No matches found.")


if __name__ == "__main__":
    main()