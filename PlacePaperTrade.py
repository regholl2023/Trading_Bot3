import requests
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import os

# api_url = "https://api.tdameritrade.com/v1/oauth2/token"
# json = {"grant_type" : "authorization_code", "access_type" : offline, "code" : , "client_id" : , "redirect_uri	" : }
# response = requests.pos(api_url, json = )
# print(response.json())

username = os.environ["username"]
password = os.environ["password"]
driver = webdriver.Chrome("/Users/arnavmehta/Downloads/chromedriver")

driver.get("https://www.tdameritrade.com/")
# find username/email field and send the username itself to the input field
driver.find_element("id", "stepup_username0").send_keys(username)
# find password input field and insert password as well
driver.find_element("id", "stepup_password1").send_keys(password)
# click login button
driver.find_element("title", "Client Login").click()

