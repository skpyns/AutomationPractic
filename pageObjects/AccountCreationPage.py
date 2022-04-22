from selenium.webdriver.common.by import By
# from TestFramework.conftest import user
from selenium.webdriver.support.select import Select


class AccountCreationPage:

    def __init__(self, driver):
        self.driver = driver

    gender = (By.CSS_SELECTOR, 'input#id_gender1')
    firstname = (By.CSS_SELECTOR, 'input#customer_firstname')
    lastname = (By.CSS_SELECTOR, 'input#customer_lastname')
    password = (By.CSS_SELECTOR, 'input#passwd')
    address = (By.CSS_SELECTOR, 'input#address1')
    city = (By.CSS_SELECTOR, 'input#city')
    state = (By.CSS_SELECTOR, 'select#id_state')
    zipcode = (By.CSS_SELECTOR, 'input#postcode')
    phonenumber = (By.CSS_SELECTOR, 'input#phone_mobile')
    submitbutton = (By.CSS_SELECTOR, 'button#submitAccount')
    logoutbutton = (By.CSS_SELECTOR, 'a.logout')


    def genderselection(self):
        return self.driver.find_element(*AccountCreationPage.gender).click()

    def firstnameinput(self):
        return self.driver.find_element(*AccountCreationPage.firstname)

    def lastnameinput(self):
        return self.driver.find_element(*AccountCreationPage.lastname)

    def passwordinput(self):
        return self.driver.find_element(*AccountCreationPage.password)

    def addressinput(self):
        return self.driver.find_element(*AccountCreationPage.address)

    def cityinput(self):
        return self.driver.find_element(*AccountCreationPage.city)

    # def stateinput(self):
    #     select = Select(self.driver.find_element(*AccountCreationPage.state))
    #     select.select_by_visible_text(user['state'])
    #     return select

    def getStates(self):
        return self.driver.find_element(*AccountCreationPage.state)

    def zipcodeinput(self):
        return self.driver.find_element(*AccountCreationPage.zipcode)

    def phonenumberinput(self):
        return self.driver.find_element(*AccountCreationPage.phonenumber)

    def submitingaccount(self):
        return self.driver.find_element(*AccountCreationPage.submitbutton).click()

    def logoutbtn(self):
        return self.driver.find_element(*AccountCreationPage.logoutbutton)