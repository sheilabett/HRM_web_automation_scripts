from behave import *
from selenium import webdriver

@given('launch chrome browser')
def launch_browser(context):
   context.driver =webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe" )


@when('open LinkedIn homepage')
def launch_homepage(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")

@then('verify that the logo prsent on page')
def present_page(context):
    status = context.driver.find_element_by_xpath("//div[@id='divLogo']//img").is_displayed()
    assert status is True

@then('close browser')
def close_browser(context):
    context.driver.close()

