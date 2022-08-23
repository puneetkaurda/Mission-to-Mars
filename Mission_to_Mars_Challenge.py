


# Import Splinter and BeautifulSoup
from splinter import Browser
from bs4 import BeautifulSoup as soup
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd


executable_path = {'executable_path': ChromeDriverManager().install()}
browser = Browser('chrome', **executable_path, headless=False)


# Visit the mars nasa news site
url = 'https://redplanetscience.com'
browser.visit(url)


#Optional delay for loading the page
browser.is_element_present_by_css('div.list_text', wait_time=1)


# Convert the browser html to a soup object and then quit the browser
html = browser.html
news_soup = soup(html, 'html.parser')
slide_elem = news_soup.select_one('div.list_text')


slide_elem.find('div', class_='content_title')



# Use the parent element to find the first `a` tag and save it as `news_title`
news_title = slide_elem.find('div', class_='content_title').get_text()
news_title



# Use the parent element to find the paragraph text
news_p = slide_elem.find('div', class_='article_teaser_body').get_text()
news_p


# ### Featured Images


# Visit URL
url = 'https://spaceimages-mars.com'
browser.visit(url)


# Find and click the full image button
full_image_elem = browser.find_by_tag('button')[1]
full_image_elem.click()


# Parse the resulting html with soup
html = browser.html
img_soup = soup(html, 'html.parser')


# Find the relative image url
img_url_rel = img_soup.find('img', class_='fancybox-image').get('src')
img_url_rel


# ## Mars facts


# Use the base URL to create an absolute URL
img_url = f'https://spaceimages-mars.com/{img_url_rel}'
img_url




df = pd.read_html('https://galaxyfacts-mars.com')[0]
df.columns=['description', 'Mars', 'Earth']
df.set_index('description', inplace=True)
df


df.to_html()


# # Deliverable 1: Scrape Full-Resolution Mars Hemisphere Images and Titles


# Hemispheres
# 1. Use browser to visit the URL 
url = 'https://marshemispheres.com/'

browser.visit(url)


# 2. Create a list to hold the images and titles.
hemisphere_image_urls = []

# 3. Write code to retrieve the image urls and titles for each hemisphere.
# Create a for loop to iterate through the tags.
for i in range (3,7):
    
    # Create an empty dictionary to store the current image url and title.
    hemisphere = {}
    
    # Finding and clicking a hemisphere link.
    img_thumb = browser.find_by_tag('img')[i]
    img_thumb.click()
    
    # Parse the resulting html with soup.
    html = browser.html
    hemisphere_soup = soup(html, 'html.parser')
    
    # Find the relative url for the image
    img_rel_url = hemisphere_soup.find('div', class_="downloads").ul.li.a.get('href')
    
    # Create the absolute url for the image
    img_url = f'https://marshemispheres.com/{img_rel_url}'
    
    # Retrieve the title.
    title = hemisphere_soup.find('div', class_="cover").h2.text
    
    # Save the hemisphere url and the title to the dictionary.
    hemisphere['img_url']= img_url
    hemisphere['title'] = title
    
    # Append the hemisphere dictionary to the list.
    hemisphere_image_urls.append(hemisphere)
       
    # Navigate back to the beginning.
    browser.back()


# 4. Print the list that holds the dictionary of each image url and title.
hemisphere_image_urls


# 5. Quit the browser
browser.quit()






