Feature: Checkout Process

  Scenario: Guest user completes checkout
    Given the user is on the checkout page
    When the user provides shipping and payment details as a guest
    Then the order is confirmed and a confirmation message is displayed

  Scenario: Registered user completes checkout
    Given the user is logged in
    When the user adds items to the cart and proceeds to checkout
    Then the checkout process is completed successfully
