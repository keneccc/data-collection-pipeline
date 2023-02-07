# %%
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

if __name=="__main__":
    class scraper_methods:

    def __init__(self):
        self.driver=driver 
        driver=webdriver.Chrome()
        self.url=url
        url="https://soundcloud.com/"
        self.urls_set=[]             #Empty list of urls 

    def open_page(self,driver,url):
        driver.get(url)

    def add_url(self,driver):
        driver.current_url
        self.urls_set.append(driver.current_url)

    def scroll_down_vary(self,driver):
        driver.execute_script("window.scrollTo(0, 700)")

    def accept_cookies(self,driver):
        try:
            accept_cookies=driver.find_element(By.XPATH ,value='//*[@id="onetrust-accept-btn-handler"]')
            accept_cookies.click()
            time.sleep(1)
        except:
            pass

    def click_explore(self,driver): 
        open_explore_page=driver.find_element(By.XPATH, value='//*[@class="trendingTracks__ctaButton sc-button sc-button-large sc-button-cta sc-button-primary"]')
        open_explore_page.click()


    def open_top50hiphop_charts(self,driver):
        open_hiphop_top50= driver.find_element(By.XPATH, value='//*[@class="sc-artwork  sc-artwork-placeholder-11  image__full g-opacity-transition"]')
        open_hiphop_top50.click()

    def scroll_to_end(self,driver):
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def search_bar(self,driver):
        search_library=driver.find_element(By.XPATH, value='//*[@class="headerSearch__input sc-input g-all-transitions-300"]')
        search_library.send_keys("Travis scott")
        search_library.send_keys(Keys.ENTER)

    def go_back(self,driver):
        driver.back()
         

class navigate(scraper):
    def __init__():
        super().init()
    
    def test():

        open_page(driver,url)
        time.sleep(7)
        accept_cookies(driver)
        time.sleep(2)
        scroll_to_end(driver)
        time.sleep(2)
        click_explore(driver)
        add_url(driver)
        time.sleep(2)
        search_bar(driver)
        add_url(driver)
        time.sleep(2)
        go_back(driver)

soundcloud= navigate(scraper)
soundcloud.test()

    
        
