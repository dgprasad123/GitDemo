from selenium.webdriver.common.by import By


from pageObjects.CheckoutPage import CheckOutPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    shop = (By.CSS_SELECTOR, "a[href*= 'shop']")
    name = (By.CSS_SELECTOR, "[name= 'name']")
    email = (By.NAME, "email")
    pwdtext = (By.ID, "exampleInputPassword1")
    checkboxval = (By.ID, "exampleCheck1")
    gender = (By.ID, "exampleFormControlSelect1")
    submit = (By.XPATH, "//input[@type='submit']")
    successMsg = (By.CLASS_NAME, "alert-success")

    def shopItems(self):
        self.driver.find_element(*HomePage.shop).click()
        checkOutPage = CheckOutPage(self.driver)
        return checkOutPage
        # driver.find_element(By.CSS_SELECTOR, " a[href*= 'shop']")

    def getName(self):
        return self.driver.find_element(*HomePage.name)

    def getEmail(self):
        return self.driver.find_element(*HomePage.email)

    def getPassword(self):
        return self.driver.find_element(*HomePage.pwdtext)

    def getCheckBoxVal(self):
        return self.driver.find_element(*HomePage.checkboxval)

    def getGender(self):
        return self.driver.find_element(*HomePage.gender)

    def submitForm(self):
        return self.driver.find_element(*HomePage.submit)

    def getSuccessMsg(self):
        return self.driver.find_element(*HomePage.successMsg)