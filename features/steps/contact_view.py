#pylint: disable=function-redefined, no-name-in-module, import-error
from behave import given
from behave import then
from behave import when

from base.forms import UserForm


@given('that a user fills in the contact form with valid input')
def step_impl(context):
    context.values = {
        "sender_email": "test@example.bike",
        "subject": "just saying hello",
        "message": "Hi bob, havn't talk in a while. All the Best, --Joe",
    }

@when('the user submits the contact form')
def step_impl(context):
    context.response = context.test.client.post(
        context.get_url('/contact/'),
        context.values,
        follow=True,
    )

@then('the contact form is successfully submitted')
def step_impl(context):
    context.test.assertRedirects(context.response, context.get_url('contact_sent'))
