import time
import pytest
from selenium import webdriver

@pytest.fixture
def driver(request):
    wd = webdriver.Chrome()
    # wd = webdriver.Ie(capabilities={"requireWindowFocus": True})
    # wd = webdriver.Firefox(capabilities={"marionette": False})
    request.addfinalizer(wd.quit)
    return wd


def test_test_elschet(driver):
    """
    check sending form electonic schet
    :param driver: driver of browser
    :return:
    """
    driver.get('https://mgts.ru/home/payments/elschet/')
    phonenumber = driver.find_element_by_css_selector("[name='FIELDS[HOME_PHONE_FID1]']")
    phonenumber.clear()
    phonenumber.send_keys('4951231212')
    name = driver.find_element_by_css_selector('[name="FIELDS[NAME_FID1]"]')
    name.clear()
    name.send_keys('testname')
    surname = driver.find_element_by_css_selector('[name="FIELDS[SURNAME_FID1]"]')
    surname.clear()
    surname.send_keys('testsurname')
    email = driver.find_element_by_css_selector('[name="FIELDS[EMAIL_FID1]"]')
    email.clear()
    email.send_keys("test@test.com")
    mobile = driver.find_element_by_css_selector('[name="FIELDS[MOBILE_FID1]"]')
    mobile.clear()
    mobile.send_keys("89991112233")
    submit = driver.find_element_by_css_selector('input[type="submit"][value="Отправить"]')
    submit.click()
    text = "Спасибо! Ваша заявка принята. Сотрудник МГТС свяжется с Вами в ближайшее время."
    assert len(driver.find_elements_by_xpath('//p[contains(text(), "' + text + '")]')) > 0