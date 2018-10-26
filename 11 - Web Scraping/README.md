# Web Scraping

## What is this about?

This is the demonstration of scraping multiple web pages for the different pieces of the information regarding Mars and a travel to it. The scraping is done using Python and `beautifulsoup4` library. The scraped data is then stored inside MongoDB (with the help of `pymongo`, using a local instance) and is presented on HTML page that is served by the `Flask` application.

## What is Inside
  
- A Jupyter Notebook file [scraper.ipynb](scraper.ipynb) that contains all the scraping and storing logic

- A Python file [scraper.py](scraper.py) that contains all the same logic but in the form of a script

- `Flask` Python [app](web_app.py) that provides UI to run the scraping process and display its results