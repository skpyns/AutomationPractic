from selenium.webdriver.common.by import By
from TestFramework.pageObjects.AccountCreationPage import AccountCreationPage


class AccountPage:
    def __init__(self, driver):
        self.driver = driver

    email = (By.CSS_SELECTOR, 'input#email_create')
    createbutton = (By.CSS_SELECTOR, 'button#SubmitCreate')


    def creatingaccount(self):
        return self.driver.find_element(*AccountPage.email)

    def submitingemail(self):
        self.driver.find_element(*AccountPage.createbutton).click()
        accountcreationpage = AccountCreationPage(self.driver)
        return accountcreationpage