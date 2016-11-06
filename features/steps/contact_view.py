#pylint: disable=function-redefined, no-name-in-module, import-error
from behave import given
from behave import then
from behave import when


@given('that a user fills in the contact form with valid input')
def step_impl(context):
    context.browser.visit(context.get_url('contact'))
    context.browser.fill('sender_email', 'bob@example.com')
    context.browser.fill('subject', 'just saying hello')
    context.browser.fill('message', 'Hi bob, havn\'t talk in a while. All the Best, --Joe')

@when('the user submits the contact form')
def step_impl(context):
    context.browser.find_by_css('input[type=submit]').first.click()

@then('the contact form is successfully submitted')
def step_impl(context):
    assert context.browser.url == context.get_url('contact_sent')

@given('that a user fills in the contact form with an invalid email')
def step_impl(context):
    context.browser.visit(context.get_url('contact'))
    context.browser.fill('subject', 'just saying hello')
    context.browser.fill('message', 'Hi bob, havn\'t talk in a while. All the Best, --Joe')

@then('the contact form is not successfully submitted')
def step_impl(context):
    assert context.browser.url == context.get_url('contact')
    assert context.browser.is_element_present_by_css('.errorlist')
