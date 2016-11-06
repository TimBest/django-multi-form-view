Feature: ContactView
  A demo view for illustrating how to use a MultiFormView.

  Scenario: A user enters the required contact info
    Given that a user fills in the contact form with valid input
    When the user submits the contact form
    Then the contact form is successfully submitted

  Scenario: A user attempts to contact with an invalid email
    Given that a user fills in the contact form with an invalid email
    When the user submits the contact form
    Then the contact form is not successfully submitted
