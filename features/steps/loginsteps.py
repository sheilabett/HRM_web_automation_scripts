from behave import *
from selenium import webdriver


@given('I launch chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path="C:\Program Files (x86)\chromedriver.exe")


@when('I open Orange HRM Homepage')
def OpenFacebook(context):
    context.driver.get("https://opensource-demo.orangehrmlive.com/")


@when('Enter username "{user}" and password "{password}"')
def step_impl(context, user, password):
    context.driver.find_element_by_id("txtuser").send_keys(user)
    context.driver.find_element_by_id("txtpass").send_keys(password)


@when('Click login button')
def step_impl(context):
    raise NotImplementedError(u'STEP: When Click login button')
    context.driver.find_element_by_id("btnLogin").click()


@then('User must successfully login to the Dashboard page')
def step_impl(context):
    try:
        text=context.driver.find_element_by_xpath("//*[@id='content']/div/div[1]/h1").text
    except:
        context.driver.close()
        assert False, "Test Failed"
    if text=="Dashboard":
        context.driver.close()
        assert True, "Test Passed"




