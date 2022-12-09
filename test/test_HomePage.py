import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from Testdata.HomepageData import HomepageData
from pageObjects.HomePage import HomePage
from utilities.BaseClass import BaseClass


class TestHomePage(BaseClass):


    def test_formSubmission(self,getData):


        homepage = HomePage(self.driver)
        homepage.getName().send_keys(getData["firstname"])
        homepage.getEmail().send_keys(getData["lastname"])
       # driver.find_element(By.NAME, "email").send_keys("heello@gmail.com")
        homepage.getPassword().send_keys(getData["password"])
       # driver.find_element(By.ID, "exampleInputPassword1").send_keys("12345")
        homepage.getCheckBoxVal().click()
       # driver.find_element(By.ID, "exampleCheck1").click()

    # xpath= //tagname[@attribute='value']  --> //input[@type='submit']
    # css = //tagname[@attribute='value']  --> input[name='name']

        self.selectOptionBygender(homepage.getGender(), getData["gender"])

        homepage.submitForm().click()
        alertText = homepage.getSuccessMsg().text
        #driver.find_element(By.CSS_SELECTOR, "input[name='name']").send_keys("abcd")
        #driver.find_element(By.CSS_SELECTOR, "#inlineRadio1").click()
       # dropdown = Select(driver.find_element(By.ID, "exampleFormControlSelect1"))
       # dropdown.select_by_visible_text("Female")
       # dropdown.select_by_index(1)
    # dropdown.select_by_value()
      #  driver.find_element(By.XPATH, "//input[@type='submit']").click()
       # message = driver.find_element(By.CLASS_NAME, "alert-success").text
        print(alertText)

        assert ("Success" in alertText)
        self.driver.refresh()


    #@pytest.fixture(params = [("Rahul","Shetty","12345","Male"),("Anisha","Shetty","45677","Female")])
    @pytest.fixture(params=HomepageData.test_HomepageData)
    def getData(self, request):
        return request.param
