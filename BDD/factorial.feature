Feature: Factorial Calculation
  Scenario: Compute the factorial of a number
    Given the number 5
    When I calculate the factorial
    Then the result should be 120
