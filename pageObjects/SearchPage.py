from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from TestFramework.TestData.OrderData import Order
from TestFramework.pageObjects.SingInPage import SignInPage
from TestFramework.utils.BaseClass import BaseClass


class SearchPage(BaseClass):
    def __init__(self, driver):
        self.driver = driver

    searchresults = (By.CSS_SELECTOR, 'ul.product_list div.product-container')
    product = (By.CSS_SELECTOR, 'a.product-name')
    productdetails = (By.CSS_SELECTOR, 'a.quick-view')
    iframe = (By.TAG_NAME, 'iframe')
    twitter = (By.CSS_SELECTOR, 'button.btn-twitter')
    facebook = (By.CSS_SELECTOR, 'button.btn-facebook')
    google = (By.CSS_SELECTOR, 'button.btn-google-plus')
    pintereset = (By.CSS_SELECTOR, 'button.btn-pinterest')
    discount = (By.CSS_SELECTOR, 'span#reduction_percent_display')
    order_quantity = (By.CSS_SELECTOR, 'input#quantity_wanted')
    size = (By.CSS_SELECTOR, 'select#group_1')
    color = (By.CSS_SELECTOR, 'a[title=Blue]')
    addtocartbutton = (By.CSS_SELECTOR, 'p#add_to_cart button')
    checkoutname = (By.CSS_SELECTOR, 'a.cart_block_product_name')
    checkoutattributes = (By.CSS_SELECTOR, 'div.product-atributes a')
    checkoutquantity = (By.CSS_SELECTOR, 'span#layer_cart_product_quantity')
    submitcheckout = (By.CSS_SELECTOR, "a[title='Proceed to checkout']")

    def search_and_save_results(self):
        dresslist = self.driver.find_elements(*SearchPage.searchresults)
        with open('./searchresults2.txt', 'w') as file:
            for dress in dresslist:
                name = dress.find_element(*SearchPage.product).text.strip()
                file.write('%s \n' % name)

    def social_media_btn(self):
        dresslist = self.driver.find_elements(*SearchPage.searchresults)
        first_result = dresslist[0]
        ActionChains(self.driver).move_to_element(first_result).perform()
        first_result.find_element(*SearchPage.productdetails).click()
        iframe = self.driver.find_element(*SearchPage.iframe)
        self.driver.switch_to.frame(iframe)
        self.driver.implicitly_wait(20)
        twitterbtn = self.driver.find_element(*SearchPage.twitter)
        facebookbtn = self.driver.find_element(*SearchPage.facebook)
        googlebtn = self.driver.find_element(*SearchPage.google)
        pinterestbtn = self.driver.find_element(*SearchPage.pintereset)
        reduction = self.driver.find_element(*SearchPage.discount).text
        return twitterbtn, facebookbtn, googlebtn, pinterestbtn, reduction

    def placing_order(self):
        self.driver.implicitly_wait(10)
        dresslist = self.driver.find_elements(*SearchPage.searchresults)
        first_result = dresslist[0]
        ActionChains(self.driver).move_to_element(first_result).perform()
        first_result.find_element(*SearchPage.productdetails).click()
        iframe = self.driver.find_element(*SearchPage.iframe)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*SearchPage.order_quantity).clear()
        self.driver.find_element(*SearchPage.order_quantity).send_keys(Order.order['quantity'])
        locator = self.driver.find_element(*SearchPage.size)
        self.selectOptionByText(locator, Order.order['size'])
        # select2 = Select(driver.find_element_by_css_selector('select#group_1'))
        # select2.select_by_visible_text('M')
        self.driver.find_element(*SearchPage.color).click()
        self.driver.find_element(*SearchPage.addtocartbutton).click()
        self.driver.switch_to.default_content()
        checkoutname = self.driver.find_element(*SearchPage.checkoutname).get_attribute('title')
        checkoutattributes = self.driver.find_element(*SearchPage.checkoutattributes).get_attribute('innerHTML')
        checkoutquantity = self.driver.find_element(*SearchPage.checkoutquantity).text
        return checkoutname, checkoutattributes, checkoutquantity

    def checkingout(self):
        self.driver.implicitly_wait(10)
        dresslist = self.driver.find_elements(*SearchPage.searchresults)
        first_result = dresslist[0]
        ActionChains(self.driver).move_to_element(first_result).perform()
        first_result.find_element(*SearchPage.productdetails).click()
        iframe = self.driver.find_element(*SearchPage.iframe)
        self.driver.switch_to.frame(iframe)
        self.driver.find_element(*SearchPage.order_quantity).clear()
        self.driver.find_element(*SearchPage.order_quantity).send_keys(Order.order['quantity'])
        locator = self.driver.find_element(*SearchPage.size)
        self.selectOptionByText(locator, Order.order['size'])
        # select2 = Select(driver.find_element_by_css_selector('select#group_1'))
        # select2.select_by_visible_text('M')
        self.driver.find_element(*SearchPage.color).click()
        self.driver.find_element(*SearchPage.addtocartbutton).click()
        self.driver.switch_to.default_content()
        self.driver.find_element(*SearchPage.submitcheckout).click()
        signinpage = SignInPage(self.driver)
        return signinpage






