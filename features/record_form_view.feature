Feature: RecordFormView
  A demo view for illustrating how to use a MultiModelFormView.

  Scenario: A user creates a record
    Given that a user fills in the form with valid input
    When the user submits the form
    Then a Record and Photo instance are created
