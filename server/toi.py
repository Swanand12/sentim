import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup


def scrape_toi_data(search_query):
    url = "https://timesofindia.indiatimes.com/"

    driver = webdriver.Chrome()

    try:

        driver.get(url)
        num = 0

        wait = WebDriverWait(driver, 10)
        search_button = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'OG1TB')))
        actions = ActionChains(driver)
        actions.click(search_button).perform()

        search_bar = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, 'textbox')))
        actions = ActionChains(driver)
        actions.click(search_bar).perform()

        search_statement = search_query
        search_bar.send_keys(search_statement)

        search_bar.send_keys(Keys.ENTER)

        while num<5:
            load_more_articles = wait.until(EC.element_to_be_clickable((By.CLASS_NAME, "IVNry")))
            action = ActionChains(driver)
            action.click(load_more_articles).perform()
            time.sleep(5)
            num += 1
            
        html = driver.page_source
        soup = BeautifulSoup(html , "html.parser")
        
        headlines = soup.find_all("div", {"class": "fHv_i o58kM"})
        headline_list = [headline.text.strip() for headline in headlines]
        # for headline in headlines:
        #     print("Title: ",headline.text.strip())

        return headline_list
        

    except Exception as e:
        print("An error occurred:", e)

    finally:
        driver.quit()
