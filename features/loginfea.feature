Feature: Orange Hrm Login

  Scenario: Login to Orange HRM with valid parameters
    Given I launch chrome browser
    When I open Orange HRM Homepage
    And Enter username "admin" and password "admin123"
    And Click login button
    Then User must successfully login to the Dashboard page


  Scenario Outline:  Login to OrangeHRM with multiple parameters
    Given I launch chrome browser
    When I open Orange HRM Homepage
    And Enter username "<Username>" and password "<password>"
    And Click login button
    Then User must successfully login to the Dashboard page
    Examples:
      | email    | password |
      | admin    | admin123 |
      | admin123 | admin    |


