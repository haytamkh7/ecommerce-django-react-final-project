# import time
# from selenium.webdriver.chrome import webdriver
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import pytest
#
#
# @pytest.fixture()
# def driver():
#     # chrome_driver_binary = "chromedriver.exe"
#     # ser_chrome = ChromeService(chrome_driver_binary)
#
#     # driver = webdriver.Chrome(service=ser_chrome)
#     # Headless
#     dc = {
#         "browserName": "chrome",
#         "platformName": "Windows 11"
#
#     }
#     # Selenium grid standAlone
#     driver = webdriver.Remote("http://localhost:4444", desired_capabilities=dc)
#     yield driver
#     driver.close()
#     # java -jar selenium-server-4.3.0.jar standalone
#
#
# def test_open_webpage(driver):
#     # Open the web page
#     driver.get('http://127.0.0.1:8000/#/')
#     time.sleep(3)
#     assert driver.title == "Google"
#
#
# # def test_register(driver):
# #     # Open the web page
# #     driver.get('https://www.amazon.com/')
# #     time.sleep(4)
# #     # Click sign in button
# #     driver.find_element(By.CSS_SELECTOR, "#nav-link-accountList").click()
# #     time.sleep(4)
# #     # Click create account button
# #     driver.find_element(By.CSS_SELECTOR, "#createAccountSubmit").click()
# #     time.sleep(4)
# #     # Full name input
# #     driver.find_element(By.CSS_SELECTOR, "#ap_customer_name").send_keys("Jeff Smith")
# #     time.sleep(4)
# #     # Mobile/Email input
# #     driver.find_element(By.CSS_SELECTOR, "#ap_email").send_keys("sajobi3111@meidir.com")
# #     time.sleep(4)
# #     # Password input
# #     driver.find_element(By.CSS_SELECTOR, "#ap_password").send_keys("testing_909$")
# #     time.sleep(4)
# #     # Repeat-password input
# #     driver.find_element(By.CSS_SELECTOR, "#ap_password_check").send_keys("testing_909$")
# #     time.sleep(4)
# #     # Click the continue button
# #     driver.find_element(By.CSS_SELECTOR, "#continue").click()
# #     time.sleep(4)
# #     # Check authentication page
# #     assert driver.title == "Authentication required"
