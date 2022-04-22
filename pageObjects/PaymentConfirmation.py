from selenium.webdriver.common.by import By


class PaymentConfirmation:
    def __init__(self, driver):
        self.driver = driver

    bankwire = (By.CSS_SELECTOR, 'a.bankwire')
    termsconfirmation = (By.CSS_SELECTOR, 'button[type=submit] i')
    confirmtext = (By.CSS_SELECTOR, 'p strong.dark')
    # confirm payment options
    # driver.find_element_by_css_selector('a.bankwire').click()

    # confirm terms and order
    # driver.find_element_by_css_selector('button[type=submit] i').click()

    # confirmtext = driver.find_element_by_css_selector('p strong.dark').text

    # assert 'Your order on My Store is complete.' in confirmtext

    def proceed_to_checkout(self):
        self.driver.find_element(*PaymentConfirmation.bankwire).click()
        self.driver.find_element(*PaymentConfirmation.termsconfirmation).click()
        confirmtext = self.driver.find_element(*PaymentConfirmation.confirmtext).text
        return confirmtext