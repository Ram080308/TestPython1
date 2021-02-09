import pytest

from utilities.readConfig import ReagConfig
from pageObjects.Womens_TShirts_Category import Womens_Tshirt_Landing_Page
from pageObjects.Front_HomePage import Front_HomePage
from pageObjects.Front_ShoppingCartSummaryPage import ShoppingCartsummary
from pageObjects.Front_Authentication import AuthenticationPage
from pageObjects.Front_FinalCheckoutPage import FinalCheckout


class Test_001_Login_To_NopCommerce_Admin:

    baseurl = ReagConfig.getfrontend_url()

    @pytest.mark.regression
    def test_place_order(self, setup):
        self.driver = setup
        self.driver.maximize_window()
        self.driver.get(self.baseurl)

        self.fhp = Front_HomePage(self.driver)
        self.fhp.test_select_item_womens_tshirt()

        self.wlp =Womens_Tshirt_Landing_Page(self.driver)
        self.wlp.test_add_item_to_cart("2")

        self.scs = ShoppingCartsummary(self.driver)
        self.scs.test_proceed_to_checkout()

        self.auth = AuthenticationPage(self.driver)
        self.auth.test_checkout_create_account()

        self.fco = FinalCheckout(self.driver)
        self.fco.test_complete_checkout()













