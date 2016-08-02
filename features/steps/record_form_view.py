#pylint: disable=function-redefined, no-name-in-module, import-error
from StringIO import StringIO

from behave import given
from behave import then
from behave import when

from base.models import Photo


@given('that a user fills in the form with valid input')
def step_impl(context):
    image = StringIO()
    image.name = 'record_photo.png'

    context.values = {
        "title": "Test title",
        "description": "Test description",
        "Tag": Photo.UNKNOWN,
        "image": image
    }

@when('the user submits the form')
def step_impl(context):
    context.response = context.test.client.post(
        context.get_url('/records/new/'),
        context.values,
        follow=True
    )

@then('a Record and Photo instance are created')
def step_impl(context):
    assert context.response.status_code == 200
