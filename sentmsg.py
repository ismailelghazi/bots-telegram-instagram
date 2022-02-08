import sys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager as CM
from selenium import webdriver
import sqlite3
import time

TIMEOUT = 60


def read_users():
    con = sqlite3.connect('database.db')
    curs = con.execute('SELECT name FROM accounts')
    rows = curs.fetchall()
    users = []
    for row in rows:
        users.append(row[0])
    return users


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
    for user in read_users():
        bot.get(f'https://www.instagram.com/{user}')
        try:
            follow_btn = bot.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/div[2]/div/div/div/span/span[1]/button')
            follow_btn.click()
            print('clicked follow btn')
        except NoSuchElementException:
            pass

        msg_btn = WebDriverWait(bot, 10).until(EC.presence_of_element_located((By.XPATH, '//button[@class="sqdOP  L3NKy    _8A5w5    "]')))
        msg_btn.click()

        time.sleep(1)
        input_field = bot.find_element(By.XPATH, '//textarea[@placeholder="Message..."]')
        input_field.send_keys('Hello There, How are you.')
        time.sleep(1)
        input_field.send_keys(Keys.ENTER)
        input()


if __name__ == '__main__':
    login()
