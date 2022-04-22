from selenium.webdriver.common.by import By
from TestFramework.TestData.LogInData import UserLogin
from TestFramework.pageObjects.ConfirmationPage import OrderConfirmation


class SignInPage:
    def __init__(self, driver):
        self.driver = driver

    submitcheckout = (By.CSS_SELECTOR, 'a.standard-checkout')
    signin_email = (By.CSS_SELECTOR, 'input#email')
    signin_passwd = (By.CSS_SELECTOR, 'input#passwd')
    signin_btn = (By.CSS_SELECTOR, 'button#SubmitLogin')

    def signingin(self):
        self.driver.find_element(*SignInPage.submitcheckout).click()
        self.driver.find_element(*SignInPage.signin_email).send_keys(UserLogin.active_user['email'])
        self.driver.find_element(*SignInPage.signin_passwd).send_keys(UserLogin.active_user['passwd'])
        self.driver.find_element(*SignInPage.signin_btn).click()
        confirmationpage = OrderConfirmation(self.driver)
        return confirmationpage

