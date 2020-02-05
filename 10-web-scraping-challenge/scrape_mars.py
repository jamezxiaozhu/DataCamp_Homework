# Dependencies
from bs4 import BeautifulSoup
import requests
import pymongo
from splinter import Browser
from splinter.exceptions import ElementDoesNotExist
import time
import pandas as pd


# # Begin scrape_mars.py
def scrape(final_scrape_output):
    final_scrape_output = {}
    # # Nasa Mars News

    # URL of page to be scraped
    url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'

    # Retrieve page with the requests module
    response = requests.get(url)
    # Create BeautifulSoup object; parse with 'lxml'
    soup = BeautifulSoup(response.text, 'lxml')


    # Retrieve the parent divs for all articles
    news_title = soup.find('div', class_='content_title').text.strip()

    # Add results to dict
    final_scrape_output.update(
        {'news_title': news_title}
    )

    # Retrieve news paragraph
    news_p = soup.find('div', class_='rollover_description_inner').text.strip()

    # Add results to dict
    final_scrape_output.update(
        {'news_p': news_p}
    )

    # # JPL Mars Space Images - Featured Image

    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    # URL of page to be scraped
    url_img = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(url_img)


    try:
        browser.select('category', 'featured')
        bg_attribute_string =browser.find_by_css('article').first['style']
        bg_attribute_string_left = bg_attribute_string.split('("',1)[1]
        bg_attribute_string_final = bg_attribute_string_left.split('")',1)[0]
        
    except ElementDoesNotExist:
        print("Clicking Complete")

    featured_image_url = 'https://www.jpl.nasa.gov' + bg_attribute_string_final

    # Add results to dict
    final_scrape_output.update(
        {'featured_image_url': featured_image_url}
    )

    # # Mars Weather

    # URL of page to be scraped
    url_weather = 'https://twitter.com/marswxreport?lang=en'

    # Retrieve page with the requests module
    response_weather = requests.get(url_weather)

    # Create BeautifulSoup object; parse with 'lxml'
    soup_weather = BeautifulSoup(response_weather.text, 'lxml')


    #Extract text from tweet
    weather_p = soup_weather.find('p', class_='TweetTextSize TweetTextSize--normal js-tweet-text tweet-text').text.strip()

    #Clean up text from tweet
    mars_weather = weather_p.replace('\n',', ')

    # Add results to dict
    final_scrape_output.update(
        {'mars_weather': mars_weather}
    )

    # # Mars Facts


    url_facts = 'https://space-facts.com/mars/'

    # Use Panda's `read_html` to parse the url
    tables = pd.read_html(url_facts)
    tables

    #Load data into DataFrame
    facts_df = tables[0]
    facts_df.rename(columns={
        0:"Description",
        1:"Value"
    }, inplace=True)
    facts_df.set_index('Description',inplace=True)

    #convert pandas into html table
    facts_html = facts_df.to_html()

    # Add results to dict
    final_scrape_output.update(
        {'facts_html': facts_html}
    )

    # # Mars Hemispheres


    executable_path = {'executable_path': 'chromedriver.exe'}
    browser = Browser('chrome', **executable_path, headless=True)

    # URL of page to be scraped
    url_mars_hemispheres = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'

    browser.visit(url_mars_hemispheres)

    #loop to get all mars hemispheres
    hemisphere_image_urls = []

    mars_hemishpheres = [
        "Valles Marineris Hemisphere",
        "Cerberus Hemisphere",
        "Schiaparelli Hemisphere",
        "Syrtis Major Hemisphere"
    ]

    for hemisphere in mars_hemishpheres:
        hemisphere_image_urls_dict = {}
        browser.find_by_text(f'{hemisphere} Enhanced').click()
        img_url_href = browser.find_by_text('Sample')['href']
        hemisphere_image_urls_dict.update(
            {'title' : hemisphere,
            'img_url': img_url_href
            }
        )
        hemisphere_image_urls.append(hemisphere_image_urls_dict)
        browser.back()

    # Add results to dict
    final_scrape_output.update(
        {'hemisphere_image_urls': hemisphere_image_urls}
    )

    return final_scrape_output
# # END scrap_mars.py

