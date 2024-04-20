Feature: demoqa Home Page
  As a web user
  I want to be able to access the demoqa home page
  So that I can browse products

  Scenario: Accessing the demoqa home page
    Given I have a web browser open
    When I navigate to "https://demoqa.com/"
    Then The demoqa home page is displayed