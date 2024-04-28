# Web Scraper

A Python web scraper for downloading files from a given URL.

## Description

This web scraper is a versatile tool designed to automate the process of downloading files from websites. It allows users to specify a URL to scrape and filter files based on their extensions. The scraper utilizes the `requests` library for making HTTP requests, `BeautifulSoup` for parsing HTML content, `tqdm` for displaying progress bars, and `colorama` for colorizing console output.

## Installation

To install the web scraper and its dependencies, follow these steps:

1. Clone this repository:

    ```bash
    git clone https://github.com/mryadanigu/My_Projects/Scraper.git
    ```

2. Navigate to the project directory:

    ```bash
    cd My_Projects/Scraper
    ```

3. Run the setup script:

    ```bash
    python3 setup.py
    ```

## Usage

To use the web scraper, follow these steps:

1. Run the main interface:

    ```bash
    puthon3 web_scrap.py
    ```

2. Follow the on-screen instructions to input the URL you want to scrape and specify the file extensions you want to download.

3. The scraper will then fetch all the links from the webpage, filter them based on the specified file extensions, and download the files to the specified directory.

## Features

- Scrapes files from a specified URL.
- Supports filtering files by extension.
- Displays progress bars for download status.
- Logs errors and download activity to a file.

