from testsite import OperationsHelperUI
import time

class Tests():
    def test_text_from_about(self, browser):
        testpage = OperationsHelperUI(browser)
        testpage.go_to_site()
        testpage.enter_login("alexxxxx")
        testpage.enter_pass("ad0364a494")
        testpage.click_login_button()
        time.sleep(3)
        testpage.click_about_link()
        time.sleep(3)
        font_size = testpage.get_font_size()
        assert font_size == '32px'

