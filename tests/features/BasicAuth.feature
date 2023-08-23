@BasicAuth
Feature: Login using a JavaScript Alert popup windows authentication

    Background: landing page
        Given user is on the home page
        When user clicks on "Basic Auth"

    Scenario Outline: Enter correct and incorrect login credentials for authentication
        Then user enter "<username>" and "<password>" and clicks on sign in button
        Then login status
        Examples:
            | username | password     |
            | admin    | admin        |
            | wrong_pw | wrong_usernm |