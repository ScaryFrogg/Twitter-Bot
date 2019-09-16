from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests
import re
import time
import random
username = "Your username"
password = "Your password"

searchWord = "searchWord"
interactions = ["Hey I am Python bot, don't be scared I am not harmful, my master @puricvojin sent me to make him some friends. So Hi <3 :D",
                "I have been sent here to greet you and ask you to follow @puricvojin on his #100DayCodeChellange. Oh I forgot to introduce myself I am just bot <3"]
like = True
retweet = False

driver = webdriver.Firefox()
driver.get("https://twitter.com/login")
def waithForBrowser(element,browser=driver,timeout=15):
    try:
        WebDriverWait(browser, timeout).until(EC.presence_of_element_located(element))    
    except Exception:
        pass

""" login """
time.sleep(2)
inputUsername = driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[1]/input")
inputUsername.click()
inputUsername.send_keys(username)
inputUsername.send_keys(Keys.TAB)

inputPassword = driver.find_element_by_xpath(
    "/html/body/div[1]/div[2]/div/div/div[1]/form/fieldset/div[2]/input")
inputPassword.send_keys(password)
inputPassword.send_keys(Keys.ENTER)
time.sleep(2)

""" search """
searchWord = searchWord.replace("#", "%23")
searchWord = searchWord.replace("@", "%40")
driver.get("https://twitter.com/search?q="+searchWord+"&src=typed_query")
time.sleep(5)
driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
time.sleep(5)
""" interact """

tweets = driver.find_elements_by_tag_name("article")
links =[]
""" get links """
for t in tweets:
    link =t.find_element_by_css_selector('a[href*="status"]')
    links.append(link.get_attribute("href"))

""" loopThrough posts """
for l in links:
    driver.get(l)
    time.sleep(random.randint(7,11))
    if(retweet):
        driver.find_element_by_css_selector('div[data-testid="retweet"]').click()
        time.sleep(random.randint(1,5))
    if(like):
        driver.find_element_by_css_selector('div[data-testid="like"]').click()
        time.sleep(random.randint(1,5))
    if(len(interactions)>0):
        driver.find_element_by_css_selector('div[data-testid="reply"]').click()
        time.sleep(1)
        textInput =driver.find_element_by_css_selector('div[data-testid="tweetTextarea_0"]')
        textInput.click()
        textInput.send_keys(interactions[random.randrange(len(interactions))])
        driver.find_element_by_css_selector('div[data-testid="tweetButton"]').click()
        time.sleep(1)