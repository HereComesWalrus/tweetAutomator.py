from selenium import webdriver
from getpass import getpass
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains

usr = input("Enter your username or mail:")
pwd = getpass("Enter your password:")
tweetee = input("Enter username to which you want to send a tweet: ")
message = input("Tweet: ")

driver = webdriver.Chrome()
driver.get("https://twitter.com/login")

user_box = driver.find_element_by_class_name("js-username-field")
user_box.send_keys(usr)

pwd_box = driver.find_element_by_class_name("js-password-field")
pwd_box.send_keys(pwd)

sleep(1)

login = driver.find_element_by_css_selector("button.submit.EdgeButton.EdgeButton--primary.EdgeButtom--medium")
login.submit()

driver.get("https://twitter.com/" + tweetee)

msg_butt =driver.find_element_by_css_selector("button.NewTweetButton.u-sizeFull.js-tooltip.EdgeButton.EdgeButton--primary.u-textTruncate")
msg_butt.click()

actions = ActionChains(driver)

tweet_box = driver.find_element_by_id("tweet-box-global")

actions.move_to_element(tweet_box)
actions.click()
actions.send_keys(message)
actions.perform()

final = driver.find_element_by_css_selector("button.tweet-action.EdgeButton.EdgeButton--primary.js-tweet-btn")
final.click()