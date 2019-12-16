#!/usr/bin/python3

# -------------------------------------------------------------------
# Set a cronjob 5 minutes before you clock-in/out
# running this script and forget about using SesameTime :)
# -------------------------------------------------------------------

import os
import time
import random
import argparse
import logging
from logging.handlers import TimedRotatingFileHandler

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options


logging_handler = TimedRotatingFileHandler(filename='sesametime.log', when='D', interval=30)
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S', level=logging.INFO, handlers=[logging_handler])


parser = argparse.ArgumentParser()
parser.add_argument('--action', type=str, required=True, dest='action', choices=['in', 'out'])

args = parser.parse_args()
action = args.action

# --------------------------------------------
URL = 'https://panel.sesametime.com'
EMAIL = os.environ['SESAME_EMAIL']
PASSWORD = os.environ['SESAME_PASS']
# --------------------------------------------

# To avoid clock-in/out always at the same exact time
random_mins = random.randint(2, 6) * 60
time.sleep(random_mins)

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome('/usr/local/bin/chromedriver', chrome_options=chrome_options)
wait = WebDriverWait(driver, 10)

driver.get(URL)

# Log in
email = driver.find_element_by_id("UserEmail")
password = driver.find_element_by_id("UserPassword")

email.send_keys(EMAIL)
password.send_keys(PASSWORD)

driver.find_element_by_css_selector('#UserLoginForm .submit input').click()

# Wait until the page is loaded
wait.until(lambda driver: driver.find_element_by_id('check_button'))

if action == 'in':
	driver.find_element_by_id("check_button").click()
	alert = driver.switch_to.alert
	alert.accept()
	logging.info('In')

elif action == 'out':
	driver.find_element_by_id("check_button").click()
	alert = driver.switch_to.alert
	alert.accept()
	logging.info('Out')


driver.close()
