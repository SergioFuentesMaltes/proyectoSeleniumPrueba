Feature: Register Account functionality

  Scenario: Register with mandatory fields
    Given I navigate to Register Page
    When I enter details into mandatory fields
    And I click on Continue button
    Then Account should be created successfully

  Scenario: Register with all fields
    Given I navigate to Register Page
    When I enter details into all fields
    And I click on Continue button
    Then Account should be created successfully

  Scenario: Register with duplicate email
    Given I navigate to Register Page
    When I enter details into all fields except email field
    And I enter existing account email into email field
    And I click on Continue button
    Then Proper warning message informing about duplicate account should be displayed

  Scenario: Register without providing any details
    Given I navigate to Register Page
    When I dont enter anything in the fields
    And I click on Continue button
    Then Proper warning message informing about mandatory fields should be displayed



