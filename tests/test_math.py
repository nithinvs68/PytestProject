import pytest
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver


# def test_add1():
#     assert 1+1==2


# @pytest.mark.parametrize('a,b',[(1,2),(3,4),(5,6),(7,8),(9,0)])
# def test_add(a,b):
#     print(a+b)
#
#
# def test_divide_by_zero():
#     with pytest.raises(ZeroDivisionError):
#         1/0

@pytest.fixture(scope='session',autouse=True)
def browser():
    # services=Service(executable_path=r'.//driver//chromedriver.exe')
    option=webdriver.ChromeOptions()
    option.add_experimental_option('detach', True)
    driver=webdriver.Chrome(options=option)
    driver.implicitly_wait(10)

    yield driver
    driver.maximize_window()
    # driver.quit()


# def test_basic_duck_search(browser):
def test_basic_duckduckgo_search(browser):
    URL = 'https://www.duckduckgo.com'
    PHRASE = 'panda'

    browser.get(URL)

    search_input = browser.find_element(By.ID,'searchbox_input')
    search_input.send_keys(PHRASE + Keys.RETURN)

    link_divs = browser.find_element(By.CSS_SELECTOR,'#links > div')
    assert len(link_divs) > 0

    xpath = f"//div[@id='links']//*[contains(text(), '{PHRASE}')]"
    results = browser.find_element(By.XPATH,xpath)
    assert len(results) > 0

    search_input = browser.find_element(By.ID,'search_form_input')
    assert search_input.get_attribute('value') == PHRASE


