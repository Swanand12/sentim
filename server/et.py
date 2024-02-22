import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def scrape_et_data(search_query):
    url = "https://economictimes.indiatimes.com/"

    driver = webdriver.Chrome()

    try:

        driver.get(url)
        # num = 0

        wait = WebDriverWait(driver, 3)

        search_bar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'inputBox')))
        actions = ActionChains(driver)
        actions.click(search_bar).perform()
        # time.sleep(3)
        search_statement = search_query
        search_bar.send_keys(search_statement)
        # time.sleep(3)
        search_bar.send_keys(Keys.ENTER)

        time.sleep(3)

        # while num<4:
        #     load_more_articles = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "loadMore")))
        #     action = ActionChains(driver)
        #     action.click(load_more_articles).perform()
        #     time.sleep(5)
        #     num += 1

        time.sleep(3)
        html = driver.page_source
        soup = BeautifulSoup(html , "html.parser")
        
        headlines = soup.find_all("div", {"class": "updateText"})


        headline_list = []

        for div in headlines:    
            h3_element = div.find("h3")
            if h3_element:           
                headline_list.append(h3_element.text.strip())
       
        print(headline_list)
        return headline_list

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()

# scrape_et_data("budget 2024")
        
