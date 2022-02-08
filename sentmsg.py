from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium import webdriver
import sqlite3
import time

TIMEOUT = 60
con = sqlite3.connect('database.db')
USERNAME = "cherepanovarnks1977-ui@rambler.ru"  # input('[info account] put your email or username:')
PASSWORD = "_-nRTR1q)w"  # input('[info account] put your password here:')
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

bot = webdriver.Chrome(executable_path=CM().install(), options=options)


def login():
    bot.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    print("[Info] - Logging in...")

    user_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

    user_element.send_keys(USERNAME)

    pass_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(3)
    bot.get('https://www.instagram.com/direct/inbox/')
    no = bot.find_elements_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
    for chk in no:
        chk.click()

    time.sleep(3)

    no2 = bot.find_element(By.CSS_SELECTOR, 'div.RnEpo')
    no2.click()
    bot.get('https://www.instagram.com/direct/new/')
    time.sleep(2)
    accounts_element = WebDriverWait(bot, TIMEOUT).until(
        EC.presence_of_element_located((
            By.XPATH, '//*[@id="react-root"]/section/div[2]/div/div[1]/div/div[2]/input')))

    accounts_element.send_keys("droop.deaddd")
    click_final = bot.find_element(By.CSS_SELECTOR, 'div.-qQT3')
    click_final.click()
    time.sleep(2)


if __name__ == '__main__':
    login()
