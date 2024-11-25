from playwright.sync_api import Page, expect  # type: ignore
from pages.main_page import MainPage


def test_fill_numbers(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    main_page.search_field.fill('123456')
    expect(main_page.search_field).to_have_attribute('value', '123456')

def test_fill_letters(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    main_page.search_field.fill('qwqwqw')
    expect(main_page.search_field).to_have_attribute('value', 'qwqwqw')


def test_fill_special_characters(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    main_page.search_field.fill('!"№;%:?*')
    expect(main_page.search_field).to_have_attribute('value', '!"№;%:?*')


def test_fill_all_combination(page: Page):
    main_page = MainPage(page)
    main_page.page.goto("https://gh-users-search.netlify.app/")
    main_page.search_field.fill('RE!@2323')
    expect(main_page.search_field).to_have_attribute('value', 'RE!@2323')