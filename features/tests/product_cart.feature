Feature: Test Scenarios for empty cart functionality

  Scenario: User can verify empty cart
    Given Open target main page
    When Click on Cart icon
    Then Cart is empty

  Scenario: User can add a product to cart
    Given Open target main page
    When Search for mug
    And Click on Add to Cart button
    And Store product name
    And Confirm Add to Cart button from side navigation
    And Open cart page
    Then Verify cart has 1 item(s)
    And Verify cart has correct product

