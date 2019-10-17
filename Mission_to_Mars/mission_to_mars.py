#!/usr/bin/env python
# coding: utf-8

# In[1]:


from splinter import Browser
from bs4 import BeautifulSoup
from pprint import pprint
import pymongo
import pandas as pd
import requests


# Nasa Mars News

# In[2]:


executable_path = {"executable_path": r"C:\Users\Owner\Desktop\RU-HOU-DATA-PT-07-2019-U-C\12-Web-Scraping-and-Document-Databases\2\Activities\08-Stu_Splinter\Solved\chromedriver"}
browser = Browser("chrome", **executable_path, headless=False)


# In[3]:


url = "https://mars.nasa.gov/news/"
browser.visit(url)


# In[4]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[5]:


nasa_mars_news_titles = soup.find("div", class_="content_title").text
print(f"Title: {nasa_mars_news_titles}")


# In[6]:


nasa_mars_news_paragraphs = soup.find('div', class_='article_teaser_body')
print(f"Paragraph: {nasa_mars_news_paragraphs}")


# In[ ]:





# In[ ]:





# In[7]:


soup.find(class_ = 'article_teaser_body').text


# JPL Mars Space Images

# In[8]:


url_1 = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(url_1)


# In[14]:


featured_image_url_1 = url_1 + "spaceimages/images/wallpaper/PIA20465-1920x1200.jpg"
print(featured_image_url_1)


# Mars Weather

# In[16]:


url_2 = "https://twitter.com/marswxreport?lang=en"
browser.visit(url_2)


# In[18]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[21]:


mars_weather_tweet =soup.find(class_ = 'tweet-text')
mars_weather_tweet = mars_weather_tweet.text.strip()
print(mars_weather_tweet)


# Mars Facts

# In[29]:


mars_facts_table = pd.read_html("https://space-facts.com/mars/")
mars_facts_table_df = mars_facts_table[0]
mars_facts_table_df


# In[30]:


mars_facts_table_df.to_html(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, bold_rows=True, classes=None, escape=True, max_rows=None, max_cols=None, show_dimensions=False, notebook=False, decimal='.', border=None, table_id=None)


# Mars Hemispheres

# In[34]:


url_cerberus = "https://astrogeology.usgs.gov/search/map/Mars/Viking/cerberus_enhanced"
browser.visit(url_cerberus)


# In[35]:


html = browser.html
soup = BeautifulSoup(html, "html.parser")


# In[37]:


cerberus_image = soup.find_all("img",class_= "wide-image")
for image in cerberus_image:
    img_cerberus = "https://astrogeology.usgs.gov" + image['src']
print(img_cerberus)


# In[38]:


schiaparelli_image = soup.find_all("img",class_= "wide-image")
for image in schiaparelli_image:
    img_schiaparelli = "https://astrogeology.usgs.gov" + image['src']
print(img_schiaparelli)


# In[39]:


syrtis_image = soup.find_all("img",class_= "wide-image")
for image in syrtis_image:
    img_syrtis = "https://astrogeology.usgs.gov" + image['src']
print(img_syrtis)


# In[40]:


valles_image = soup.find_all("img",class_= "wide-image")
for image in valles_image:
    img_valles = "https://astrogeology.usgs.gov" + image['src']
print(img_valles)


# In[45]:


hemisphere_image_urls = [
    {"title": "Cerberus Hemisphere", "img_url":cerberus_image },
    {"title": "Schiaparelli Hemisphere", "img_url":schiaparelli_image},
    {"title": "Syrtis Major Hemisphere", "img_url":syrtis_image}, 
    {"title": "Valles Marineris Hemisphere", "img_url":valles_image}
]
hemisphere_image_urls


# In[48]:


hemisphere_image_urls_df = pd.DataFrame(hemisphere_image_urls)
hemisphere_image_urls_df


# In[ ]:




