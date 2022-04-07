Feature: Facebook page

  Scenario: Logo presence on the LinkedIn home page
    Given launch chrome browser
    When open LinkedIn homepage
    Then verify that the logo prsent on page
    And close browserclear