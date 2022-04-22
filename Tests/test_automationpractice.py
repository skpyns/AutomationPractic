from TestFramework.TestData.OrderData import Order
from TestFramework.pageObjects.HomePage import HomePage
from TestFramework.pageObjects.SearchPage import SearchPage
from TestFramework.utils.BaseClass import BaseClass
from TestFramework.TestData.LogInData import UserLogin


class TestAutomationPractise(BaseClass):


    def test_creatingaccount(self):
        log = self.getLogger()
        log.info('Testing account creation.')
        self.driver.implicitly_wait(10)
        homepage = HomePage(self.driver)
        accountpage = homepage.logingin()
        accountpage.creatingaccount().send_keys(UserLogin.user['email'])
        accountcreationpage = accountpage.submitingemail()
        accountcreationpage.genderselection()
        accountcreationpage.firstnameinput().send_keys(UserLogin.user['firstname'])
        accountcreationpage.lastnameinput().send_keys(UserLogin.user['lastname'])
        accountcreationpage.passwordinput().send_keys(UserLogin.user['passwd'])
        accountcreationpage.addressinput().send_keys(UserLogin.user['address'])
        accountcreationpage.cityinput().send_keys(UserLogin.user['city'])
        self.selectOptionByText(accountcreationpage.getStates(), UserLogin.user['state'])
        accountcreationpage.zipcodeinput().send_keys(UserLogin.user['zipcode'])
        accountcreationpage.phonenumberinput().send_keys(UserLogin.user['phonenumber'])
        accountcreationpage.submitingaccount()
        logoutbtn = accountcreationpage.logoutbtn()
        assert logoutbtn.is_displayed()
        log.info('Account created.')

    def test_categories(self):
        log = self.getLogger()
        log.info('Testing categories.')
        homepage = HomePage(self.driver)
        popularlist, bestsellinglist = homepage.findingproducts()
        log.info('Confirming expected results with actual result.')
        log.info('Popular product list equals to ' + str(popularlist) + ' and best selling products list equals to ' + str(bestsellinglist) + '.')
        assert popularlist == 7 and bestsellinglist == 7


    def test_PrintedDresses(self):
        homepage = HomePage(self.driver)
        searchpage = homepage.search_dresses()
        searchpage.search_and_save_results()

    def test_PrintedDress(self):
        homepage = HomePage(self.driver)
        resultspage = homepage.search_dresses()
        twitterbtn, facebookbtn, googlebtn, pinterestbtn, reduction = resultspage.social_media_btn()
        assert twitterbtn.is_displayed()
        assert facebookbtn.is_displayed()
        assert googlebtn.is_displayed()
        assert pinterestbtn.is_displayed()
        assert reduction == '-5%'

    def test_PlacingOrder(self):
        homepage = HomePage(self.driver)
        resultspage = homepage.search_dresses()
        checkoutname, checkoutattributes, checkoutquantity = resultspage.placing_order()
        assert Order.order['name'] in checkoutname
        assert Order.order['size'] in checkoutattributes
        assert Order.order['color'] in checkoutattributes
        assert Order.order['quantity'] in checkoutquantity

    def test_CheckoutOrder(self):
        log = self.getLogger()
        homepage = HomePage(self.driver)
        resultspage = homepage.search_dresses()
        checkoutpage = resultspage.checkingout()
        orderpage = checkoutpage.signingin()
        confirmationpage = orderpage.address_confirmation()
        confirmtext = confirmationpage.proceed_to_checkout()
        assert 'Your order on My Store is complete.' in confirmtext
        log.info('Testing finished.')