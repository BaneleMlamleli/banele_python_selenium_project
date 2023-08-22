@AddAndRemoveElement
Feature: Add and remove an element

    Background: landing page
        Given user is on the home page
        When user clicks on "Add/Remove Elements"

    Scenario: Add and remove an element
        When user clicks on Add Element button to add Delete button
        Then user clicks on Delete button to remove the button