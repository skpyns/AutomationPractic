from selenium.webdriver.common.by import By

from TestFramework.pageObjects.SingInPage import SignInPage


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver

    price = (By.CSS_SELECTOR, 'td#total_product')
    totalprice = (By.CSS_SELECTOR, 'span#total_price')
    submitcheckout = (By.CSS_SELECTOR, 'a.standard-checkout')

    def checkingout(self):
        orderprice = self.driver.find_element(*CheckoutPage.price).text
        totalorderprice = self.driver.find_element(*CheckoutPage.totalprice).text
        self.driver.find_element(*CheckoutPage.submitcheckout).click()
        signinpage = SignInPage(self.driver)
        return orderprice, totalorderprice, signinpage




# price = driver.find_element_by_css_selector('td#total_product').text
        # print(price)
        # totalprice = driver.find_element_by_css_selector('span#total_price').text
        # print(totalprice)

        # driver.find_element_by_css_selector('a.standard-checkout').click()
