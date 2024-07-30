# Web Scraper and Extractor for Zomato Delivery Information

This project is a web scraper and extractor designed to collect and process delivery information from Zomato using Selenium and BeautifulSoup.

## Features

- **Scraping Mode:** Collects the entire page source from the specified URL by scrolling to the bottom of the page.
- **Extraction Mode:** Extracts relevant data from the saved page source, including the title, link, rating, description, price, and time.
- **Data Storage:** Saves the extracted data into Excel and CSV files.

## Requirements

- Python 3.x
- Selenium
- BeautifulSoup4
- Pandas

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/web-scraper-extractor.git
   cd web-scraper-extractor
2. **Install the Required Package:**
   ```bash
   pip install selenium beautifulsoup4 pandas

3. **Set Mode :**
      To scrape data, set mode = "scrape"
      To extract data, set mode = "extract"
      Leave mode empty to perform both actions.

4. **Run the Script**
   ```bash
   python web_scraper_extractor.py



## Contributing
Feel free to fork this repository, create a branch, and submit a pull request with your improvements.

## Contact
If you have any questions or suggestions, please open an issue or contact me at [rdssjayswal@gmail.com].


