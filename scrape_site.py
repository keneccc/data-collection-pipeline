
import requests
from bs4 import BeautifulSoup
from selenium import webdriver 
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

urls_set=[]


driver=webdriver.Chrome()
url="https://soundcloud.com/"

def scroll_down_vary(driver):
    driver.execute_script("window.scrollTo(0, 700)")

def accept_cookies(driver):
    try:
        accept_cookies=driver.find_element(By.XPATH ,value='//*[@id="onetrust-accept-btn-handler"]')
        accept_cookies.click()
        time.sleep(1)
    except:
        pass



def click_explore(driver): 
    open_explore_page=driver.find_element(By.XPATH, value='//*[@class="trendingTracks__ctaButton sc-button sc-button-large sc-button-cta sc-button-primary"]')
    open_explore_page.click()


def open_top50hiphop_charts(driver):
    open_hiphop_top50= driver.find_element(By.XPATH, value='//*[@class="sc-artwork  sc-artwork-placeholder-11  image__full g-opacity-transition"]')
    open_hiphop_top50.click()

def scroll_to_end(driver):
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

def search_bar_metro(driver):
    search_library=driver.find_element(By.XPATH, value='//*[@class="headerSearch__input sc-input g-all-transitions-300"]')
    search_library.send_keys("Metro Boomin")
    search_library.send_keys(Keys.ENTER)

def search_bar_travis(driver):
    search_library=driver.find_element(By.XPATH, value='//*[@class="headerSearch__input sc-input g-all-transitions-300"]')
    search_library.send_keys("Travis Scott")
    search_library.send_keys(Keys.ENTER)

def go_back(driver):
    driver.back()

def add_url(driver):
    driver.current_url
    urls_set.append(driver.current_url)

def get_metro_songs(driver):
    page=requests.get(driver.current_url)
    html=page.content
    time.sleep(2)  # Allow 2 seconds for the web page to open
    scroll_pause_time = 1 # You can set your own pause time. My laptop is a bit slow so I use 1 sec
    screen_height = driver.execute_script("return window.screen.height;")   # get the screen height of the web
    i = 1

    song_link_list=[]

    while True:
        # scroll one screen height each time
        driver.execute_script("window.scrollTo(0, {screen_height}*{i});".format(screen_height=screen_height, i=i))  
        i += 1
        time.sleep(scroll_pause_time)
        # update scroll height each time after scrolled, as the scroll height can change after we scrolled the page
        scroll_height = driver.execute_script("return document.body.scrollHeight;")  
        # Break the loop when the height we need to scroll to is larger than the total scroll height
        if i==10:
            break 



    soup= BeautifulSoup(html, "html.parser")
    song_content =soup.find_all(name="li", attrs={"class":"searchList__item sc-mt-3x"})
    print(type(song_content))
    for song in song_content:
        song_title_tag=song.find_all(name="a",class_="sc-link-primary soundTitle__title sc-link-dark sc-text-h4")
        song_link=song_title_tag.attrs['href']
        print(song_link)
        song_title=song_title_tag.find_all('span','class').text
        print(song_title_tag)
        song_link_list.append(song_link)
        #song_title_list.append(song_title)
        
    
    #print(song_link_list)

    
    
        
        





def get_songs(driver,url):
    driver.get(url)
    time.sleep(7)
    accept_cookies(driver)
    time.sleep(2)
    add_url(driver)
    scroll_down_vary(driver)
    time.sleep(2)
    click_explore(driver)
    time.sleep(2)
    open_top50hiphop_charts(driver)
    add_url(driver)
    time.sleep(2)

    search_bar_metro(driver)
    add_url(driver)
    time.sleep(2)
    scroll_to_end(driver)
    get_metro_songs(driver)
    songs_list=driver.find_elements(By.XPATH, value='//*[@class="systemPlaylistTrackList__item sc-border-light-bottom sc-px-2x"]')
    #time.sleep(2)
    #search_bar(driver)
    #time.sleep(2)
    #go_back(driver)





    
get_songs(driver,url)


