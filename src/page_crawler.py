import random
import time
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from restaurant_parser import RestaurantParser


class PageCrawler():

    def __init__(self, url, lat='40.68088531', lng='-73.91765595',
                 headless=True, ll=25, ul=50):
        self.url = url % (lat, lng)
        self.lat = lat
        self.lng = lng
        self.headless = headless
        self.page_num = None
        self.ll = ll
        self.ul = ul


    def _get_page_num(self):
        chrome_options = Options()
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(ChromeDriverManager().install(),
                                   options=chrome_options)
        driver.get(self.url)
        try:
            WebDriverWait(driver, 60).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'searchResult'))
            )
        except TimeoutException:
            print('Loading took too much time – could not get page number')
        else:
            html = driver.page_source
            soup = BeautifulSoup(html, features="lxml")
            num = soup.find('div', {'class': 'searchResults-footer'}).find(
                'p', {'class': 'u-text-secondary u-center'}).text.split(' ')[-1]
            self.page_num = int(num)
        finally:
            driver.quit()


    def _get_restaurant_html(self, item):
        self.driver.get(self.url)
        try:
            # wait for button to be enabled
            WebDriverWait(self.driver, random.uniform(self.ll,self.ul)).until(
                EC.element_to_be_clickable((By.CLASS_NAME, 'searchResult')))

            self.driver.implicitly_wait(random.uniform(self.ll,self.ul))
            try:
                button = self.driver.find_element_by_xpath("//div[@impressionranky=%s]" % item)
                button.click()

                WebDriverWait(self.driver, random.uniform(self.ll,self.ul)).until(
                    EC.element_to_be_clickable((By.CLASS_NAME, 'menuItem')))

                self.driver.implicitly_wait(random.uniform(self.ll,self.ul))
                html = self.driver.find_element_by_tag_name('html').get_attribute('innerHTML')
            except:
                return
        except TimeoutException:
            print('Loading took too much time!')
            return
        else:
            html = self.driver.page_source
        finally:
            self.driver.quit()
        return html


    def _get_info(self, html):
        re = RestaurantParser(html)
        return {'name': re._get_name(),
                'phone': re._get_phone_number(),
                'address': re._get_address(),
                'pop_items': re._get_pop_items(),
                'menu': re._get_menu_items()}


    def crawl_page(self, lim=20):
        data = []
        self._get_page_num()
        for page in range(1, self.page_num):
            if page > 1:
                self.url = self.url + '&pageNum=' + str(page)
                time.sleep(self.ll)
            for num in range(1,lim+1):
                self.chrome_options = Options()
                if self.headless:
                    self.chrome_options.add_argument("--headless")

                self.driver = webdriver.Chrome(ChromeDriverManager().install(),
                                               options=self.chrome_options)
                html = self._get_restaurant_html(str(num))
                if html != None:
                    data.append(self._get_info(html))
                    time.sleep(random.uniform(self.ll,self.ul))
                else:
                    data.append(None)
            if page > 10:
                break
        return data
