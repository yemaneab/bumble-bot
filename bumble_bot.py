from selenium import webdriver
from time import sleep
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

from secrets import username, password


class BumbleBot():
    def __init__(self):
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get('https://bumble.com/get-started')

        sleep(5)

        cell_button = self.driver.find_element_by_xpath(
            '/html/body/div/div/div[1]/div[3]/main/div/div[2]/form/div[3]/div')

        cell_button.click()

        phone_in = self.driver.find_element_by_xpath('//*[@id="phone"]')
        phone_in.send_keys(username)

        continue_button = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[1]/div[3]/main/div/div[2]/form/div[4]/button')
        continue_button.click()
        sleep(5)

        pw_in = self.driver.find_element_by_xpath('//*[@id="pass"]')
        pw_in.send_keys(password)

        signin_button = self.driver.find_element_by_xpath(
            '//*[@id="main"]/div/div[1]/div[3]/main/div/div[2]/form/div[2]/button')
        signin_button.click()

        sleep(5)

    def like(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_RIGHT).perform()

    def dislike(self):
        actions = ActionChains(self.driver)
        actions.send_keys(Keys.ARROW_LEFT).perform()

    def auto_swipe(self):
        while True:
            sleep(2)
            try:
                self.like()
            except Exception:
                self.close_match()

    def close_match(self):
        continue_bumbling_btn = self.driver.find_element_by_xpath(
            '/html/body/div/div/div[1]/main/div[2]/article/div/footer/div/div[2]/div/span')
        continue_bumbling_btn.click()


bot = BumbleBot()
bot.login()
bot.auto_swipe()
