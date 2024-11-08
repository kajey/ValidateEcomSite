Feature: User Registration

  Scenario: User successfully registers with valid details
    Given the user is on the registration page
    When the user fills in valid registration details
    Then the user should be redirected to the welcome page
