import allure
from pages.page_object_placing_an_order import WhoIsTheScooterFor


class TestPlacingAnOrder:
    @allure.title('Проверяем заполнение заказа с данными 1')
    def test_making_an_order_one(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        who_is_the_page = WhoIsTheScooterFor(driver)

        name = "Михаил"
        last_name = "Андреев"
        address = "Санкт - Петербург"
        metro_station = "Черкизовская"
        phone = "+7777777777"

        who_is_the_page.waiting_for_the_main_page_to_load()
        who_is_the_page.click_button_top_order()
        who_is_the_page.click_button_cookies()
        who_is_the_page.fill_field_who(name, last_name, address, metro_station, phone)

        date = "20.12.2022"
        comment = "Спасибо"

        who_is_the_page.fill_field_about_rent(date, comment)

        button_text = who_is_the_page.display_button_view_status()
        text = "Посмотреть статус"
        assert button_text == text

    @allure.title('Проверяем заполнение заказа с данными 2')
    def test_making_an_order_two(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        who_is_the_page = WhoIsTheScooterFor(driver)

        name = "Игорь"
        last_name = "Гусев"
        address = "Москва"
        metro_station = "Сокольники"
        phone = "+7777777555"

        who_is_the_page.waiting_for_the_main_page_to_load()
        who_is_the_page.scroll_to_button_bottom_order()
        who_is_the_page.waiting_button_bottom_order()
        who_is_the_page.click_button_bottom_order()
        who_is_the_page.click_button_cookies()
        who_is_the_page.fill_field_who_two(name, last_name, address, metro_station, phone)

        date = "21.12.2022"
        comment = "Жду"

        who_is_the_page.fill_field_about_rent(date, comment)

        button_text = who_is_the_page.display_button_view_status()
        text = "Посмотреть статус"
        assert button_text == text

    @allure.title('Проверяем клик по логотипу Самокат')
    def test_click_logo_scooter(self, driver):
        driver.get('https://qa-scooter.praktikum-services.ru/')

        who_is_the_page = WhoIsTheScooterFor(driver)
        who_is_the_page.waiting_for_the_main_page_to_load()
        who_is_the_page.click_button_top_order()
        who_is_the_page.click_logo_scooter()
        who_is_the_page.waiting_for_the_main_page_to_load()

        assert who_is_the_page.title_scooter_for_a_couple_days().is_displayed()
