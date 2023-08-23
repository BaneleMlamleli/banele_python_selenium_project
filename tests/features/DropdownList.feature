@Dropdown
Feature: Demonstration when dropdown list is click and an option is selected.

    Background: landing page
        Given user is on the home page
        When user clicks on "Dropdown"

    Scenario: Dropdown list is click and an option is selected
        Then user clicks on the dropdown element and select first option