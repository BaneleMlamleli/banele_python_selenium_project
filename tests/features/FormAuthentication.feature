@FormAuthentication
Feature: Demonstration of a secure login area. Enter tomsmith for the username and SuperSecretPassword! for the password. If the information is wrong you should see error messages..

    Background: landing page
        Given a user is on the website home page
        When user clicks on "Form Authentication"

    Scenario Outline: Correct and incorrect login credentials
        Then user enter "<username>" and "<password>" for authentication
        Then user clicks on login button and login message is displayed
        Examples:
            | username | password             |
            | tomsmith | xxxx                 |
            | Xxxx     | SuperSecretPassword! |
            | tomsmith | SuperSecretPassword! |