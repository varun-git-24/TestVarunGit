from selenium import webdriver
import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By as B


class TestPyTest:
    driver_path = "C:\\Users\\varun.rotti\\PycharmProjects\\TakeYouForwardDSA\\Test_Pytest_code1\\chromedriver-win64\\chromedriver.exe"
    url = 'https://opensource-demo.orangehrmlive.com/'

    @pytest.fixture(scope="class", autouse=True)
    def setup_class(self, request):
        service = Service(executable_path=self.driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.get(self.url)
        self.driver.maximize_window()
        request.cls.driver = self.driver
        request.addfinalizer(self.teardown_class)

    def teardown_class(self):
        self.driver.quit()

    def wait_for_presence_of_ele(self, locator, waittime):
        wait = WebDriverWait(self.driver, waittime)
        wait.until(EC.presence_of_element_located(locator))

    def test_login(self):
        time.sleep(3)
        self.wait_for_presence_of_ele((B.XPATH, "//img[@alt='orangehrm-logo']"), 10)
        self.driver.find_element(B.XPATH, "//img[@alt='orangehrm-logo']").is_displayed()
        self.driver.find_element(B.NAME, 'username').send_keys('Admin')
        self.driver.find_element(B.NAME, 'password').send_keys('admin123')
        is_login = self.driver.find_element(B.CSS_SELECTOR, '.oxd-button')
        is_login.click()

    def test_close_driver(self):
        self.driver.close()
        assert True

# def test_orange():
#     obj = TestPyTest('https://opensource-demo.orangehrmlive.com/')
#     obj.test_login()
#     time.sleep(3)
#     obj.test_close_driver()


# test_example.py

# class TestMathOperations:
#
#     def test_addition(self):
#         assert 1 + 2 == 2
#
#     def test_subtraction(self):
#         assert 2 - 1 == 1
#
#     def test_multiplication(self):
#         assert 2 * 3 == 6
#
#     def test_division(self):
#         assert 6 / 2 == 3
