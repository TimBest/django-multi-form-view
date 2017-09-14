Feature: ProfileFormView
  A demo view for illustrating how to use a MultiModelFormView where two of the forms are of the
  same form type

  Scenario: A user creates a profile
    Given that a user fills in the profile form with valid input
    When the user submits the profile form
    Then a Profile and 2 unique Photo instance are created
