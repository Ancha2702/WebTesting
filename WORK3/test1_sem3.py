import yaml
from testpage import OperationsHelper
import logging
import time

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)


def test_login_negative(browser):
    logging.info("Test login_negative Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login("test")
    testpage.enter_pass("test")
    testpage.click_login_button()
    assert testpage.get_error_text() == "401", "test_login_negative FAILED"


def test_login_positive(browser):
    logging.info("Test login_positive Starting")
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login(testdata["login"])
    testpage.enter_pass(testdata["pswd"])
    testpage.click_login_button()
    assert testpage.login_success() == f"Hello, {testdata['login']}", "test_login_positive FAILED"



def test_add_post(browser):
    logging.info("Test add_post Starting")
    testpage = OperationsHelper(browser)
    # testpage.go_to_site()
    # testpage.enter_login(testdata["login"])
    # testpage.enter_pass(testdata["pswd"])
    # testpage.click_login_button()
    testpage.click_add_post_button()
    testpage.add_title(testdata["title"])
    testpage.add_description(testdata["description"])
    testpage.add_content(testdata["content"])
    testpage.click_save_post_button()
    testpage.find_new_post_title()
    assert testpage.find_new_post_title() == f"{testdata['title']}", "test add post FAILED"

# Задание
#
# Условие: Добавить в проект тест по проверке механики работы формы Contact Us на главной странице личного кабинета.
# Должно проверятся открытие формы, ввод данных в поля, клик по кнопке и появление всплывающего alert.
#
# Совет: переключиться на alert можно командой alert = self.driver.switch_to.alert
# Вывести текст alert.text

def test_check_contact_us_positive(browser):
    logging.info("Test contact us started")
    testpage = OperationsHelper(browser)
    testpage.click_contact_button()
    time.sleep(1)
    testpage.add_name_block_contact(testdata["name"])
    testpage.add_email_block_contact(testdata["email"])
    testpage.add_content_block_contact(testdata["content_1"])
    testpage.click_save_contact_us()
    time.sleep(1)
    assert testpage.get_allert_text() == testdata["message_success"], "Неудачная отправка данных в блоке 'Contact'"