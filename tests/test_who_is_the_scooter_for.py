from pages.page_object_who_is_the_scooter_for import WhoIsTheScooterFor

class TestWhoIsTheScooterFor:
    def test_fill_field_who(self, driver):
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

        text_to_title_about_rent = "Про аренду"

        assert who_is_the_page.text_to_title_about_rent() == text_to_title_about_rent
