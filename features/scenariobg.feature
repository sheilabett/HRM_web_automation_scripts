Feature: OrangeHRM login

  Background: common steps
    Given I launch browser
    When I open application
    And enter valid username and password
    And click login

  Scenario: Login to HRM Application
    Then the user must login to the Dashboard

  Scenario: Search user
    When navigate to search page
    Then search page should display

  Scenario: Advanced user search
    When navigate to  advanced search page
    Then advanced search page should display

