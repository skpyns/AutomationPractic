from selenium.webdriver.common.by import By

from TestFramework.pageObjects.PaymentConfirmation import PaymentConfirmation


class OrderConfirmation:
    def __init__(self, driver):
        self.driver = driver

    address = (By.CSS_SELECTOR, 'button[name=processAddress]')
    termsagreement = (By.CSS_SELECTOR, 'input[type=checkbox]')
    acceptterms = (By.CSS_SELECTOR,'button[name=processCarrier]')
    # Confirm addresses with test data

    # driver.find_element_by_css_selector('button[name=processAddress]').click()

    # confirm terms and proceed to checkout
    # driver.find_element_by_css_selector('input[type=checkbox]').click()
    # driver.find_element_by_css_selector('button[name=processCarrier]').click()

    def address_confirmation(self):
        self.driver.find_element(*OrderConfirmation.address).click()
        self.driver.find_element(*OrderConfirmation.termsagreement).click()
        self.driver.find_element(*OrderConfirmation.acceptterms).click()
        paymentconfirmation = PaymentConfirmation(self.driver)
        return paymentconfirmation



