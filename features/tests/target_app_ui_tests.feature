# Created by lgodi at 10/2/2025
Feature: Tests for Target App page


  Scenario: User is able to open Privacy Policy
    Given Open Target App page
    And Store original window
    And Click Privacy Policy link
    And Switch to new window
    Then Verify Privacy Policy page opened
    And close current page
    And Return to original window