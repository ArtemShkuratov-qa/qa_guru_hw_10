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
def test_selene():
    browser.open("/")

    s(".search-input").click()
    s("#query-builder-test").send_keys("eroshenkoam/allure-example")
    s("#query-builder-test").submit()

    s(by.link_text("eroshenkoam/allure-playwright-example")).click()

    s("#issues-tab").click()

    s(".issue-item-module__defaultNumberDescription--GXzri > span").should(have.exact_text('#1'))