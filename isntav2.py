from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from webdriver_manager.chrome import ChromeDriverManager as Cm
from selenium import webdriver
import sqlite3
import time
import random

TIMEOUT = 60


def read_users():
    con = sqlite3.connect('database.db')
    curs = con.execute('SELECT name FROM accounts where sent = 0')
    rows = curs.fetchall()
    users = []
    for row in rows:
        users.append(row[0])
    return users


USERNAME = "droop.deaddd"  # input('[info account] put your email or username:')
PASSWORD = "Nightzokssa1$"  # input('[info account] put your password here:')
options = webdriver.ChromeOptions()
options.add_argument('--no-sandbox')
options.add_argument("--log-level=3")
mobile_emulation = {
    "userAgent": "Mozilla/5.0 (Linux; Android 4.2.1; en-us; Nexus 5 Build/JOP40D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/90.0.1025.166 Mobile Safari/535.19"}
options.add_experimental_option("mobileEmulation", mobile_emulation)

bot = webdriver.Chrome(executable_path=Cm().install(), options=options)




def login():
    bot.get('https://www.instagram.com/accounts/login/')

    time.sleep(2)

    print("[Info] - Logging in...")

    user_element = WebDriverWait(bot, TIMEOUT).until(
        ec.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[3]/div/label/input')))

    user_element.send_keys(USERNAME)

    pass_element = WebDriverWait(bot, TIMEOUT).until(
        ec.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[4]/div/label/input')))

    pass_element.send_keys(PASSWORD)

    login_button = WebDriverWait(bot, TIMEOUT).until(
        ec.presence_of_element_located((
            By.XPATH, '//*[@id="loginForm"]/div[1]/div[6]/button')))

    time.sleep(0.4)

    login_button.click()

    time.sleep(3)
    for user in read_users():
        try:
            bot.get('https://www.instagram.com/direct/new/')
            time.sleep(random.uniform(2, 4))
            input_field = bot.find_element_by_class_name("j_2Hd")
            for ch in user:
                input_field.send_keys(ch)
                time.sleep(0.2)
            print("here1")
            time.sleep(2)
            buton_valid = WebDriverWait(bot, TIMEOUT).until(
                ec.presence_of_element_located((
                    By.CLASS_NAME, '-qQT3')))
            buton_valid.click()
            print("here2")
            time.sleep(2)
            buton_next = WebDriverWait(bot, TIMEOUT).until(
                ec.presence_of_element_located((
                    By.CLASS_NAME, 'sqdOP')))

            buton_next.click()
            input_field = WebDriverWait(bot, TIMEOUT).until(
                ec.presence_of_element_located((
                    By.XPATH, '//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div/textarea')))
            time.sleep(random.uniform(5, 10))
            print("[info...] type the input now ")
            message = "Hello There, How are you."
            for ch in message:
                input_field.send_keys(ch)
                time.sleep(0.2)
            time.sleep(random.uniform(5, 10))
            button_send = WebDriverWait(bot, TIMEOUT).until(
                ec.presence_of_element_located((
                    By.XPATH, '//*[@id="react-root"]/section/div[2]/div/div/div[2]/div/div/div[2]/button')))
            button_send.click()
            con = sqlite3.connect('database.db')
            curs = con.execute('SELECT name FROM accounts')
            print("Connected to SQLite")
            sql_update_query = f"""Update accounts set sent = 1 where name = '{user}'"""
            curs.execute(sql_update_query)
            con.commit()
            print("Record Updated successfully ")
            curs.close()
            time.sleep(random.uniform(10, 30))
        except NoSuchElementException:
            print("error")
            pass


if __name__ == '__main__':
    login()
