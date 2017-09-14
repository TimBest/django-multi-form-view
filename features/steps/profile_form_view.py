#pylint: disable=function-redefined, no-name-in-module, import-error
from behave import given
from behave import then
from behave import when

from base.models import Photo, Profile


@given('that a user fills in the profile form with valid input')
def step_impl(context):
    context.browser.visit(context.get_url('profiles_new'))
    context.browser.fill('name', 'lando calrissian')
    context.browser.attach_file('avatar-image', 'test.png')
    context.browser.choose('avatar-tag', Photo.UNKNOWN)
    context.browser.attach_file('background-image', 'test1.ico')
    context.browser.choose('background-tag', Photo.PLANT)

@when('the user submits the profile form')
def step_impl(context):
    context.browser.find_by_css('input[type=submit]').first.click()

@then('a Profile and 2 unique Photo instance are created')
def step_impl(context):
    assert Photo.objects.count() == 2
    assert Profile.objects.count() == 1

    # TODO: compare hash of image contents instead of name
    photo1 = Photo.objects.order_by('created_at').first().image.name
    assert photo1 == './test.png' or photo1 == './test1.ico'
    photo2 = Photo.objects.order_by('created_at').last().image.name
    assert photo2 == './test.png' or photo2 == './test1.ico'
    assert photo1 != photo2
