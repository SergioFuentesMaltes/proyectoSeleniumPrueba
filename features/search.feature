Feature: Search functionality

  @search
  Scenario: Search for a valid product
    Given I got navigated to the homepage
    When I enter valid product name "iPhone" in the search box
    And I click on the search button
    Then I should see "iPhone" in the search results

  @search
  Scenario: Search for an invalid product
    Given I got navigated to the homepage
    When I enter invalid product name "xyz" in the search box
    And I click on the search button
    Then Proper error message should be displayed

  @search
  Scenario: Search without entering any product name
    Given I got navigated to the homepage
    When I dont enter any product name in the search box
    And I click on the search button
    Then Proper error message should be displayed
