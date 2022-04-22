from selenium.webdriver.common.by import By
from TestFramework.TestData.OrderData import Order
from TestFramework.pageObjects.AccountPage import AccountPage
from TestFramework.pageObjects.CheckoutPage import CheckoutPage
from TestFramework.pageObjects.SearchPage import SearchPage


class HomePage:
    def __init__(self, driver):
        self.driver = driver

    login = (By.CSS_SELECTOR, 'a.login')
    popularCategory = (By.CSS_SELECTOR, 'a.homefeatured')
    bestsellerCategory = (By.CSS_SELECTOR, 'a.blockbestsellers')
    popluarproductlist = (By.CSS_SELECTOR, 'ul#homefeatured li')
    bestsellerproductlist = (By.CSS_SELECTOR, 'ul#blockbestsellers li')
    searchbar = (By.CSS_SELECTOR, 'input#search_query_top')
    searchbutton = (By.CSS_SELECTOR, 'button.button-search')
    checkoutbutton = (By.CSS_SELECTOR, "a[title='Proceed to checkout']")

    def logingin(self):
        self.driver.find_element(*HomePage.login).click()
        accountpage = AccountPage(self.driver) # creating and returning object for next page
        return accountpage

    def findingproducts(self):
        self.driver.find_element(*HomePage.popularCategory).click()
        popularlist = self.driver.find_elements(*HomePage.popluarproductlist)
        self.driver.find_element(*HomePage.bestsellerCategory).click()
        bestsellinglist = self.driver.find_elements(*HomePage.bestsellerproductlist)
        return len(popularlist), len(bestsellinglist)

    def search_dresses(self):
        self.driver.implicitly_wait(10)
        self.driver.find_element(*HomePage.searchbar).send_keys(Order.searchdress)
        self.driver.find_element(*HomePage.searchbutton).click()
        searchpage = SearchPage(self.driver)
        return searchpage

    def checkout(self):
        self.driver.find_element(*HomePage.checkoutbutton).click()
        checkoutpage = CheckoutPage(self.driver)
        return checkoutpage