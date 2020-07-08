Feature: Test CRUD methods in Sample REST API testing framework

Scenario: UPDATE posts example
  Given I Set PUT posts api endpoint for "1"
  When I Set Update request Body
	And Send PUT HTTP request
  Then I receive valid HTTP response code 200 for "PUT"
	And Response BODY "PUT" is non-empty
