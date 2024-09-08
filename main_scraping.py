from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def aradReadYourMeter_scraping():
    user_name="nadavgil18@gmail.com"
    password="AAAaaa111"
    s = Service("C:\Program Files (x86)\chromedriver.exe")

    driver = webdriver.Chrome(service=s)
    driver.implicitly_wait(10)  # seconds
    driver.get("https://rym-pro.com/#/home")
    # driver.get("https://www.google.com/")
    try:
        # Insert user name and password to login
        # WebDriverWait(driver, 10).until(
        #     EC.presence_of_element_located((By.NAME, 'email'))
        # ).send_keys(user_name)
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="root"]/div/div[3]/div/form/div[1]/div/input'))
        ).send_keys(user_name)

        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, 'PASSWORD'))
        ).send_keys(password)

        # Wait for the login button to be clickable and click it using CSS selector
        login_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, '#root > div > div:nth-child(3) > div > form > div:nth-child(3) > button > div'))
        )
        login_button.click()


        print("Login successful")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        time.sleep(5)
        driver.quit()
    # driver.find_element(By.NAME, 'email').send_keys(user_name)
    # driver.find_element(By.NAME,'PASSWORD').send_keys(password)
    # driver.find_element(By.XPATH,'//*[@id="root"]/div/div[3]/div/form/div[3]/button').click()
    # time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="tbl_meters_list"]/tbody/tr[5]/td[3]').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="div_body_container"]/div/div[1]/div[4]/a/img').click()
    time.sleep(5)

    driver.find_element(By.XPATH,'//*[@id="btn_table"]').click()
    time.sleep(5)


    date = driver.find_element(By.XPATH,'//*[@id="div_consumption_grapth"]/table/tbody/tr[32]/td[1]')
    time.sleep(5)
    water_consum = driver.find_element(By.XPATH,'//*[@id="div_consumption_grapth"]/table/tbody/tr[32]/td[2]')
    time.sleep(5)




    print(water_consum.text)
    print(date.text)
    return [date.text,water_consum.text]


    time.sleep(10)
    driver.quit()

