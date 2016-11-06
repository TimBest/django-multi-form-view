#pylint: disable=function-redefined, no-name-in-module, import-error
from behave import given
from behave import then
from behave import when


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

@given('that a user fills in the contact form with an invalid email')
def step_impl(context):
    context.values = {
        "sender_email": "",
        "subject": "just saying hello",
        "message": "Hi bob, havn't talk in a while. All the Best, --Joe",
    }

@then('the contact form is not successfully submitted')
def step_impl(context):
    context.test.assertFormError(
        context.response,
        'user_form',
        'sender_email',
        "This field is required."
    )
