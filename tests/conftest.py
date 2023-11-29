import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

@pytest.fixture(scope= "class")
def setup(request):
    driver = webdriver.Chrome ( service = Service ( "C:/Users/0393G8744\Documents/Python/000Practice/SeleniumPytest/"
                                                    "chromedriver_win32/chromedriver.exe" ) )

    driver.get ( "https://rahulshettyacademy.com/client" )
    driver.maximize_window ( )
    request.cls.driver = driver

    yield
    driver.close()

