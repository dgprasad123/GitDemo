import pytest
from selenium import webdriver
import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC, expected_conditions

from pageObjects.CheckoutPage import CheckOutPage
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


#@pytest.mark.usefixtures("setup")
class TestOne(BaseClass):
    def test_e2e(self):

        homePage = HomePage(self.driver)
        checkoutPage = homePage.shopItems()
    # checkoutpage = homePage.shopItems()
    # checkOutPage= CheckOutPage(self.driver)
        products = checkoutPage.getCardTitles()

        for product in products:
            productName = product.find_element(By.XPATH, "div/h4/a").text
        if productName == "Blackberry":
            checkoutPage.getCardFooter()

        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        confirmPage = checkoutPage.checkOutItems()
        self.driver.find_element(By.ID, "country").send_keys("ind")
        self.verifyLinkPresence("India")
        self.driver.find_element(By.LINK_TEXT, "India").click()
        self.driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
        self.driver.find_element(By.CSS_SELECTOR, "[type='submit']").click()
        successText = self.driver.find_element(By.CLASS_NAME, "alert-success").text

        assert 'Success! Thank you!' in successText


