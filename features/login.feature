Feature: Login Functionality
  @prueba
  Scenario: Login with correct credentials
    Given I navigated to login page
    When I enter valid email address and valid password into the fields
    And I press "Login" button
    Then I should get logged in successfully

  Scenario: Login with incorrect credentials
    Given I navigated to login page
    When I enter invalid email address and invalid password into the fields
    And I press "Login" button
    Then I should get an error message

  Scenario: Login with valid email and invalid password
    Given I navigated to login page
    When I enter valid email address and invalid password into the fields
    And I press "Login" button
    Then I should get an error message

  Scenario: Login with invalid credentials
    Given I navigated to login page
    When I enter invalid email address and invalid password into the fields
    And I press "Login" button
    Then I should get an error message

  Scenario: Login without any credentials
    Given I navigated to login page
    When I dont enter anything in the fields
    And I press "Login" button
    Then I should get an error message

