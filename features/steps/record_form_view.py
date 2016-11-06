#pylint: disable=function-redefined, no-name-in-module, import-error
from behave import given
from behave import then
from behave import when

from base.models import Photo, Record


@given('that a user fills in the form with valid input')
def step_impl(context):
    context.browser.visit(context.get_url('records_new'))
    context.browser.fill('title', 'Test title')
    context.browser.fill('description', 'Test description')
    context.browser.attach_file('image', 'test.png')
    context.browser.choose('tag', Photo.UNKNOWN)

@when('the user submits the form')
def step_impl(context):
    context.browser.find_by_css('input[type=submit]').first.click()

@then('a Record and Photo instance are created')
def step_impl(context):
    assert Photo.objects.count() == 1
    assert Record.objects.count() == 1

@given('that a user fills in the form without uploading an image')
def step_impl(context):
    context.browser.visit(context.get_url('records_new'))
    context.browser.fill('title', 'Test title')
    context.browser.fill('description', 'Test description')
    context.browser.choose('tag', Photo.UNKNOWN)

@then('a Record and Photo instance are not created')
def step_impl(context):
    assert Photo.objects.count() == 0
    assert Record.objects.count() == 0
