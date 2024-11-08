Feature: Search Functionality

  Scenario: User performs a general search for products
    Given the user is on the homepage
    When the user searches for "laptop"
    Then the search results page displays relevant products

  Scenario: User applies filters on search results
    Given the user is on the search results page
    When the user filters products by "price range" and "brand"
    Then the results are updated based on the selected filters
