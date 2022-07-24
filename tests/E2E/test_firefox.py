import pytest
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time


@pytest.fixture()
def driver():
    firefox_driver_library = 'geckodriver.exe'
    driver = webdriver.Firefox()
    yield driver
    driver.close()


def test_register(driver):
    # Open the web page

    driver.get('http://127.0.0.1:8000/#/')
    time.sleep(3)

    # Login button

    driver.find_element(By.CSS_SELECTOR, 'a.nav-link:nth-child(2)'
                        ).click()
    time.sleep(3)

    # Register button

    driver.find_element(By.CSS_SELECTOR,
                        'div.py-3:nth-child(3) > div:nth-child(1) > a:nth-child(1)'
                        ).click()
    time.sleep(3)

    # Name input

    driver.find_element(By.CSS_SELECTOR, '#name'
                        ).send_keys('Johannah Scott')
    time.sleep(2)
    name = driver.find_element(By.CSS_SELECTOR, '#name').text
    time.sleep(3)

    # Email

    driver.find_element(By.CSS_SELECTOR, '#email'
                        ).send_keys('myemail4@gmail.com')
    time.sleep(3)

    # Password

    driver.find_element(By.CSS_SELECTOR, '#password'
                        ).send_keys('password')
    time.sleep(3)

    # Repeat password

    driver.find_element(By.CSS_SELECTOR, '#passwordConfirm'
                        ).send_keys('password')
    time.sleep(3)

    # Register button

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)'
                          )
    time.sleep(3)
    button = driver.find_element(By.XPATH,
                                 '/html/body/div/div/main/div/div/div/form/button'
                                 )
    driver.implicitly_wait(10)
    ActionChains(driver).click(button).perform()
    time.sleep(4)
    assert driver.current_url == 'http://127.0.0.1:8000/#/'


def test_invalid_login(driver):
    # Open the web page

    driver.get('http://127.0.0.1:8000/#/')
    time.sleep(3)

    # Login button

    driver.find_element(By.CSS_SELECTOR, 'a.nav-link:nth-child(2)'
                        ).click()
    time.sleep(3)

    # Email

    driver.find_element(By.CSS_SELECTOR,
                        '#email'
                        ).send_keys('fake_user@gmail.com')
    time.sleep(3)

    # Password

    driver.find_element(By.CSS_SELECTOR, '#password'
                        ).send_keys('noPassword')
    time.sleep(2)

    # Sign in
    driver.find_element(By.CSS_SELECTOR, '.mt-3').click()
    time.sleep(2)

    # Invalid account
    error_msg = driver.find_element(By.CSS_SELECTOR, '.fade').text
    time.sleep(2)

    assert error_msg == 'No active account found with the given credentials'


def test_search_product(driver):
    # Open the web page

    driver.get('http://127.0.0.1:8000/#/')
    time.sleep(3)

    # Search Input
    driver.find_element(By.CSS_SELECTOR, '.mr-sm-2').send_keys(
        'Dean Vinnie Moore Semi-Hollow Body Guitar Classic White')
    time.sleep(1)

    # Search button
    driver.find_element(By.CSS_SELECTOR, '.p-2').click()
    time.sleep(2)

    driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')

    # Check search result
    search_result = driver.find_element(By.CSS_SELECTOR, '.card-title > strong:nth-child(1)').text
    time.sleep(1)

    assert search_result == 'Dean Vinnie Moore Semi-Hollow Body Guitar Classic White'
