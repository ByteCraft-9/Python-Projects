**Web Scraping Project Documentation**

**Overview**

This project involves creating a web scraper using Python to fetch, parse, and extract data from the BBC News website. 
The extracted data includes headlines and their corresponding links. The script is designed to handle errors gracefully 
and can be scheduled to run at regular intervals using task schedulers like cron on Unix-like systems or Task Scheduler on Windows.

Setup Instructions

Prerequisites

Python 3.x

Pip (Python package installer)

Required Libraries

Install the required libraries using pip:

pip install requests beautifulsoup4 pandas

Running the Script Manually

Run the script manually by executing:

python main.py

Automating the Script

Using Cron on Unix-like Systems

Using Task Scheduler on Windows

Open Task Scheduler.

Create a New Basic Task and follow the prompts to schedule your script.

Set the Action to start the Python interpreter with your script and log the output:

path of python file

Code Explanation

Libraries

import requests
from bs4 import BeautifulSoup
import pandas as pd

requests: For making HTTP requests to fetch web pages.

BeautifulSoup: For parsing HTML content.

pandas: For handling and saving data in CSV format.

Constants

URL: The target website for scraping.
HEADERS: HTTP headers to mimic a browser request.

Functions
fetch_html
Fetches HTML content from the specified URL.

Makes an HTTP GET request.
Returns the HTML content if successful.
Handles request exceptions.

parse_html
Parses the fetched HTML content.


Parses HTML using BeautifulSoup.
Returns a BeautifulSoup object if successful.
Handles parsing exceptions.

extract_headlines
Extracts headlines and links from the parsed HTML.


Uses CSS selectors to find headline elements.
Extracts and cleans headline text and links.
Handles cases where elements or links are missing.

save_to_csv
Saves extracted data to a CSV file.


Converts the data to a Pandas DataFrame.
Saves the DataFrame to a CSV file.
Handles file writing exceptions.

main
Main function to orchestrate the scraping process.


Fetches HTML content.
Parses the HTML content.
Extracts headlines.
Saves headlines to a CSV file.

Entry Point


    
Executes the main function when the script is run
