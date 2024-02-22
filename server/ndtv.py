import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def scrape_ndtv_data(search_query):
    url = "https://www.ndtv.com/"

    driver = webdriver.Chrome()

    try:

        driver.get(url)
        num = 0

        wait = WebDriverWait(driver, 10)
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'searchicon')))
        actions = ActionChains(driver)
        actions.click(search_button).perform()

        search_bar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'n_searchfld')))
        actions = ActionChains(driver)
        actions.click(search_bar).perform()

        search_statemen = search_query

        search_bar.send_keys(search_statemen)
        search_bar.send_keys(Keys.ENTER)

        while num<5:
            load_more_articles = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "src_mre-btn")))
            action = ActionChains(driver)
            action.click(load_more_articles).perform()
            time.sleep(5)
            num += 1
            
        html = driver.page_source
        soup = BeautifulSoup(html , "html.parser")
        headlines = soup.find_all("div", {"class": "src_itm-ttl"})
        headline_list = [headline.text.strip() for headline in headlines]
     
   
        return headline_list
    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

