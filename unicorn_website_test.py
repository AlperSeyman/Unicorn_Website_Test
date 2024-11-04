import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

class UnicornTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_unicor(self):
        driver = self.driver
        driver = webdriver.Chrome()
        driver.get("http://unicornitems.com/my-account/")

        WebDriverWait(driver,4).until(expected_conditions.visibility_of_element_located((By.ID,"username")))
        login_input = driver.find_element(By.ID,"username")
        login_input.send_keys("1")

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.ID,"password")))
        password = driver.find_element(By.ID,"password")
        password.send_keys("2")

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.NAME,"login")))
        login_button = driver.find_element(By.NAME,"login")
        login_button.click()

        WebDriverWait(driver, 4).until(expected_conditions.visibility_of_element_located((By.XPATH,"/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")))
        error_message = driver.find_element(By.XPATH,"/html/body/div[3]/div[3]/div/div/article/div/div/div[1]/div[1]/ul")

        assert  "ERROR: Incorrect username or password." in error_message.text

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':
    unittest.main()
