import pytest
import softest
from pages.login import Login
from pages.main_page import MainPage
from ddt import ddt, data, file_data, unpack
from utilities.utils import Utils


@pytest.mark.usefixtures("setup")
# @ddt
class TestLogin(softest.TestCase):
    log = Utils.custom_logger()
    @pytest.fixture(autouse=True)
    def class_setup(self):
        self.lgn = Login(self.driver)
        self.main = MainPage(self.driver)
        self.ut = Utils()

    def test_login_successful(self):
        email = "emailusman.66@gmail.com"
        password = "Helloworld@11"

        login_text = self.lgn.login_to_website(email, password)
        self.ut.assert_text(login_text, "You are logged in to RStudio. Please select your destination.")

    def test_create_new_space(self):
        space_name = "test space"
        email = "emailusman.66@gmail.com"
        password = "Helloworld@11"

        self.lgn.login_to_website(email, password)
        header_title = self.main.create_new_space(space_name)
        self.ut.assert_text(header_title, space_name)

    def test_create_new_project(self):
        project_name = "Untitled Project"
        email = "emailusman.66@gmail.com"
        password = "Helloworld@11"

        self.lgn.login_to_website(email, password)
        result = self.main.create_new_project()
        self.ut.assert_text(result, project_name)
























