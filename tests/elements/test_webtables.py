import random
from faker import Faker
from pages.elements.webtables import WebTablesPage

fake = Faker()

def test_webtables(driver):
    webtable_page = WebTablesPage(driver)
    webtable_page.open()

    webtable_page.click_add()
    webtable_page.enter_firstName(fake.first_name())
    webtable_page.enter_lastName(fake.last_name())
    webtable_page.enter_email(fake.email())

    # selects a random number between 18 and 65
    fake_age = random.randint(18, 65)
    webtable_page.enter_age(str(fake_age))

    fake_salary = random.randint(10000, 20000)
    webtable_page.enter_salary(fake_salary)

    webtable_page.click_submit()

    webtable_page.search_by_firstName("Cierra")

    # edit age and salary
    webtable_page.edit_user_by_firstName("Cierra", new_age=30, new_salary=15000)

    # delete record
    webtable_page.delete_user_by_firstName("Cierra")
