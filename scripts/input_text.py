from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from hidden import *

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "eager"

driver = webdriver.Chrome(executable_path='source/chromedriver', desired_capabilities=caps)


def setup():
    driver.get(url='https://app.roll20.net/sessions/new')

    email = driver.find_element_by_id('email')
    email.send_keys(EMAIL)
    password = driver.find_element_by_id('password')
    password.send_keys(PASSWORD)
    login_button = driver.find_element_by_id('login')
    login_button.click()
    driver.get(url='https://app.roll20.net/editor/setcampaign/' + ROOMURL)


def input_text(text):
    textbox = driver.find_element_by_xpath('//*[@id="textchat-input"]/textarea')
    textbox.send_keys(text)
    textbox.send_keys(Keys.ENTER)

