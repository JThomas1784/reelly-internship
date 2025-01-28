# Created by jamontethomas at 1/18/25
@allure
Feature: Verification Settings

  Scenario: User can click on verification settings option and verify the right page opens
    Given the user is on the main page
    When the user logs in with valid credentials
    And the user clicks on "settings" in the left menu
    And the user clicks on the "verification" option
    Then the verification page should open
    And "upload image" and "Next step" buttons should be available