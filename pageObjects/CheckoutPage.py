from selenium.webdriver.common.by import By

from pageObjects.ConfirmPage import ConfirmPage


class CheckOutPage:
    def __init__(self, driver):
        self.driver = driver

    cardTitle = (By.XPATH, "//div[@class='card h-100']")
    # driver.find_elements(By.XPATH, "//div[@class='card h-100']"
    cardFooter = (By.XPATH, "div/button")
    # find_element(By.XPATH, "div/button"
    checkOutItemsList = (By.XPATH, "//button[@class='btn btn-success']")

    # driver.find_element(By.XPATH, "//button[@class='btn btn-success']")

    def getCardTitles(self):
        return self.driver.find_elements(*CheckOutPage.cardTitle)

    def getCardFooter(self):
        return self.driver.find_elements(*CheckOutPage.cardFooter)

    def checkOutItems(self):
        self.driver.find_element(*CheckOutPage.checkOutItemsList).click()
        confirmPage = ConfirmPage(self.driver)
        return confirmPage