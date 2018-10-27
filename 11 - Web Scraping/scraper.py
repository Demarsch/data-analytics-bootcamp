# Import dependecies
from splinter import Browser
from bs4 import BeautifulSoup as bs
import pandas as pd
import random
import re

# Configuring splinter browser to access HTML of the target pages
executable_path = {'executable_path': 'chromedriver.exe', 'headless': True }
browser = Browser('chrome', **executable_path)

def scrape_news():
    # Scraping NASA website for a title and contents of the latest news
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    soup = bs(browser.html, 'lxml')

    news_title = None
    news_text = None

    article = soup.find('li', class_='slide')
    if article:
        header = article.find('div', class_='content_title')
        if header:
            news_title = header.text.strip()
        body = article.find('div', class_='article_teaser_body')
        if body:
            news_text = body.text.strip()
    return {
        'title': news_title,
        'text': news_text
    }

def scrape_featured_image():
    # Scraping Jet Propulsion Laboratory website for one high-res image of Mars
    url_base = 'https://www.jpl.nasa.gov'
    url = f'{url_base}/spaceimages/?search=&category=Mars'
    browser.visit(url)
    soup = bs(browser.html, 'lxml')

    featured_img_url = None
    featured_img_title = None

    section = soup.find('section', class_='main_feature')
    if section:
        article = section.find('article', class_='carousel_item')
        if article:
            match = re.search(r"url\('.+'\)", article['style'])
            featured_img_url = match[0][5:][:-2]
            featured_img_url = f'{url_base}{featured_img_url}'
            title = article.h1
            if title:
                featured_img_title = article.h1.text.strip()
    return {
        'title': featured_img_title,
        'url': featured_img_url
    }
    
def scrape_weather():
    # Scraping Twitter webpage for the latest tweet on Mars weather
    url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(url)
    soup = bs(browser.html, 'lxml')

    mars_weather = None

    tweet = soup.find('div', class_='tweet')
    if tweet:
        tweet_text = tweet.find('p', class_='tweet-text')
        if tweet_text:
            mars_weather = tweet_text.text.strip()
    return mars_weather

def scrape_facts():
    # Scraping Space Facts webpage for the interesting info on Mars
    url = 'http://space-facts.com/mars/'
    browser.visit(url)

    facts_df = pd.read_html(browser.html)[0]
    facts_df.rename(columns={0:'Fact', 1:'Details'}, inplace=True)
    facts_df.set_index('Fact', inplace=True)
    return facts_df.to_html(classes=['table', 'table-stripped'], border=0, header=False)

def scrape_hemisphere_images():
    # Scraping high-res images of Mars hemispheres
    url_base = 'https://astrogeology.usgs.gov'
    url = f'{url_base}/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(url)
    soup = bs(browser.html, 'lxml')

    thumbs = soup.find_all('div', class_='item')
    hemisphere_images = []
    word_to_trim = ' Enhanced'
    for thumb in thumbs:
        img_url = None
        img_title = None
        thumb_link = thumb.find('a', class_='itemLink')
        if thumb_link:    
            browser.visit(f'{url_base}{thumb_link["href"]}')
            soup = bs(browser.html, 'lxml')
            img = soup.find('img', class_='wide-image')
            if img:
                img_url = img['src']
                img_url = f'{url_base}{img_url}'
            title = soup.find('h2', class_='title')
            if title:
                img_title = title.text.strip()
                if img_title.endswith(word_to_trim):
                    img_title = img_title[:-len(word_to_trim)]

            if img_url:
                hemisphere_images.append({
                    'title': img_title,
                    'url': img_url
                })
    return hemisphere_images

def scrape_all():
    result = {}
    result['news'] = scrape_news()
    result['featured_image'] = scrape_featured_image()
    result['weather'] = scrape_weather()
    result['facts'] = scrape_facts()
    result['hemisphere_images'] = scrape_hemisphere_images()
    return result