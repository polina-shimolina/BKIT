Feature: 3 roots

  Scenario: k -4 16 0
    Given I have -4*x**4 + 16*x**2 + 0 = 0
    When I solve the equation
    Then I expect 3 roots: 0, 2, -2