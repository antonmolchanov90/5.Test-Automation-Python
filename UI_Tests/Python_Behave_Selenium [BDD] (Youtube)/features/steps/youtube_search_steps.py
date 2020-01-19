from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium import webdriver


@given('Go to Youtube')
def step1(context):
    context.driver = webdriver.Chrome('/opt/chromedriver')
    context.driver.get('https://www.youtube.com/')


@when('Type pokemon last battle vs rival in search input')
def step2(context):
    WebDriverWait(context.driver, 120).until(
        ec.element_to_be_clickable((By.NAME, 'search_query'))
    )
    context.driver.find_element_by_name('search_query').send_keys('pokemon last battle vs rival')


@then('Click search button')
def step3(context):
    WebDriverWait(context.driver, 120).until(
        ec.element_to_be_clickable((By.ID, 'search-icon-legacy'))
    )
    context.driver.find_element_by_id('search-icon-legacy').click()


@then('The result page contains video Pokémon Anime BGM - Champion Battle (Last Battle VS Rival) (1997~1998-M79)')
def step4(context):
    WebDriverWait(context.driver, 120).until(
        ec.presence_of_element_located((By.CSS_SELECTOR, '[title="Pokémon Anime BGM - Champion Battle '
                                                         '(Last Battle VS Rival) (1997~1998-M79)"]'))
    )
    assert context.driver.find_element_by_css_selector('[title="Pokémon Anime BGM - Champion Battle '
                                                       '(Last Battle VS Rival) (1997~1998-M79)"]')
