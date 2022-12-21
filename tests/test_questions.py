from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.page_object_questions import QuestionsPage


class TestQuestion:
    def test_price(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page = QuestionsPage(driver)

        questions_page.waiting_for_the_main_page_to_load()

        answer_1 = 'Сутки — 400 рублей. Оплата курьеру — наличными или картой.'

        questions_page.click_button_cookies()
        questions_page.scroll_to_price()
        questions_page.waiting_price()
        questions_page.click_price()
        questions_page.waiting_for_the_text_answer_1()
        answer_from_price = questions_page.answer_for_price()

        assert answer_from_price == answer_1

    def test_several_scooters(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page_2 = QuestionsPage(driver)

        questions_page_2.waiting_for_the_main_page_to_load()

        answer_2 = 'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.'

        questions_page_2.click_button_cookies()
        questions_page_2.scroll_to_several_scooters()
        questions_page_2.waiting_price()
        questions_page_2.click_several_scooters()
        questions_page_2.waiting_for_the_text_answer_2()
        answer_from_several_scooters = questions_page_2.answer_for_several_scooters()

        assert answer_from_several_scooters == answer_2

    def test_rental_time(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page_3 = QuestionsPage(driver)

        questions_page_3.waiting_for_the_main_page_to_load()

        answer_3 = 'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'

        questions_page_3.click_button_cookies()
        questions_page_3.scroll_to_rental_time()
        questions_page_3.waiting_rental_time()
        questions_page_3.click_rental_time()
        questions_page_3.waiting_for_the_text_answer_3()
        answer_from_rental_time = questions_page_3.answer_for_rental_time()

        assert answer_from_rental_time == answer_3

    def test_order_today(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page_4 = QuestionsPage(driver)

        questions_page_4.waiting_for_the_main_page_to_load()

        answer_4 = 'Только начиная с завтрашнего дня. Но скоро станем расторопнее.'

        questions_page_4.click_button_cookies()
        questions_page_4.scroll_to_order_today()
        questions_page_4.waiting_order_today()
        questions_page_4.click_order_today()
        questions_page_4.waiting_for_the_text_answer_4()
        answer_from_order_today = questions_page_4.answer_for_order_today()

        assert answer_from_order_today == answer_4

    def test_extend_the_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page_5 = QuestionsPage(driver)

        questions_page_5.waiting_for_the_main_page_to_load()

        answer_5 = 'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'

        questions_page_5.click_button_cookies()
        questions_page_5.scroll_to_extend_the_order()
        questions_page_5.waiting_extend_the_order()
        questions_page_5.click_extend_the_order()
        questions_page_5.waiting_for_the_text_answer_5()
        answer_from_extend_the_order = questions_page_5.answer_for_extend_the_order()

        assert answer_from_extend_the_order == answer_5

    def test_charging(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page_6 = QuestionsPage(driver)

        questions_page_6.waiting_for_the_main_page_to_load()

        answer_6 = 'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.'

        questions_page_6.click_button_cookies()
        questions_page_6.scroll_to_charging()
        questions_page_6.waiting_charging()
        questions_page_6.click_charging()
        questions_page_6.waiting_for_the_text_answer_6()
        answer_from_charging = questions_page_6.answer_for_charging()

        assert answer_from_charging == answer_6

    def test_cancel_the_order(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page_7 = QuestionsPage(driver)

        questions_page_7.waiting_for_the_main_page_to_load()

        answer_7 = 'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'

        questions_page_7.click_button_cookies()
        questions_page_7.scroll_to_cancel_the_order()
        questions_page_7.waiting_cancel_the_order()
        questions_page_7.click_cancel_the_order()
        questions_page_7.waiting_for_the_text_answer_7()
        answer_from_cancel_the_order = questions_page_7.answer_for_cancel_the_order()

        assert answer_from_cancel_the_order == answer_7

    def test_i_live(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        questions_page_8 = QuestionsPage(driver)

        questions_page_8.waiting_for_the_main_page_to_load()

        answer_8 = 'Да, обязательно. Всем самокатов! И Москве, и Московской области.'

        questions_page_8.click_button_cookies()
        questions_page_8.scroll_to_i_live()
        questions_page_8.waiting_i_live()
        questions_page_8.click_i_live()
        questions_page_8.waiting_for_the_text_answer_8()
        answer_from_i_live = questions_page_8.answer_for_i_live()

        assert answer_from_i_live == answer_8
