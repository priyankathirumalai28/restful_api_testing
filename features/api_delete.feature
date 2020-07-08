Feature: Test CRUD methods in Sample REST API testing framework

Scenario: DELETE posts example
  Given I Set DELETE posts api endpoint for "1"
  When I Send DELETE HTTP request
  Then I receive valid HTTP response code 200 for "DELETE"
