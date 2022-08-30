from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_driver_path = "c:\development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

Promissed_down = 150
Promissed_up = 20
Email = "anshkulshreshtha01@gmail.com"
Username = "AnshKulshresht3"
password = "Mytwitter@123"

class InternetSpeedTwitterBot:
    def __init__(self, driver):
        self.driver = driver
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        driver.get("https://www.speedtest.net/")
        sleep(5)

        # turning off the cookies--
        cookies_off = driver.find_element(By.XPATH, '//*[@id="onetrust-close-btn-container"]/button')
        if (cookies_off):
            cookies_off.click()

        GO_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[1]/a/span[4]')
        GO_button.click()

        sleep(70)
        # getting down and up speed------------

        self.down = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        print("down: " + self.down)
        self.up = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        print("up: " + self.up)

    def tweet_at_provider(self):

    # login------
        driver.get("https://twitter.com/i/flow/login")
        sleep(5)

        EMAIL = driver.find_element(By.CSS_SELECTOR,'[name = "text"]')
        EMAIL.send_keys(Email)
        EMAIL.send_keys(Keys.ENTER)
        sleep(2)
# ---------if u login saveral times then twitte will send an username along with the login id and password for authentication!

        # USERNAME = driver.find_element(By.XPATH,'//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/input')
        # if(USERNAME):
        #     USERNAME.send_keys(Username)
        #     USERNAME.send_keys(Keys.ENTER)
        #     sleep(2)

        PASSWORD = driver.find_element(By.CSS_SELECTOR,'[name = "password"]')
        PASSWORD.send_keys(password)
        PASSWORD.send_keys(Keys.ENTER)

    # Message part ----------
        sleep(2)
        Message =f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {Promissed_down}down/{Promissed_up}up?"

        Msg = driver.find_element(by=By.CLASS_NAME, value="public-DraftEditor-content")
        Msg.click()
        Msg.send_keys(Message)

    # tweeting button-----
        tweet_button = driver.find_element(By.XPATH, "//*[text()='Tweet']")
        tweet_button.click()

        sleep(2)
        print("Message-sent!")
        self.driver.quit()


bot = InternetSpeedTwitterBot(driver)
bot.get_internet_speed()
bot.tweet_at_provider()
