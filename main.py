from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from secrets import password


class Instabot:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://instagram.com")
        time.sleep(4)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[2]/div/label/input").send_keys(username)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[3]/div/label/input").send_keys(password)
        self.driver.find_element_by_xpath(
            "/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div[4]/button/div").click()
        time.sleep(5)
        self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div[3]/button[2]").click()


my_bot = Instabot('_ch.ills', password)
