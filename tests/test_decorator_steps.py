import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import have
from selene.support.shared import browser
from selene.support.shared.jquery_style import s

@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "user1")
@allure.feature("Задачи в репозитории")
@allure.story("Авторизованный пользователь может создать задачу в репозитории")
@allure.link("https://github.com", name="Testing")
def test_decorator_steps():
    open_main_page()
    search_for_repository("eroshenkoam/allure-example")
    go_to_repository("eroshenkoam/allure-playwright-example")
    open_issue_tab()
    should_see_issue_with_number("#1")


@allure.step("Открываем главную страницу")
def open_main_page():
    browser.open("/")

@allure.step("Ищем репозиторий {repo}")
def search_for_repository(repo):
    s(".search-input").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()


@allure.step("Переходим по ссылке репозитория {repo}")
def go_to_repository(repo):
    s(by.link_text("eroshenkoam/allure-playwright-example")).click()


@allure.step("Открываем таб Issues")
def open_issue_tab():
    s("#issues-tab").click()


@allure.step("Проверяем наличие Issue с номером {number}")
def should_see_issue_with_number(number):
    s(".issue-item-module__defaultNumberDescription--GXzri > span").should(have.exact_text('#1'))