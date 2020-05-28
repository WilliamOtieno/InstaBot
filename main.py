from selenium import webdriver
from selenium.webdriver.chrome.options import Options




class Instabot:
    def __init__(self):

        options = Options()
        options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://instagram.com")


Instabot()