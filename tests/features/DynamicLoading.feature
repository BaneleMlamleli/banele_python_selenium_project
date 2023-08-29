@DynamicLoading
Feature: Demonstration of loading when action gets triggered that returns a result dynamically. It does not rely on the page to reload or finish loading. The page automatically gets updated through the use of JavaScript.

    Background: landing page
        Given user is on the home page
        When user clicks on "Dynamic Loading"

    Scenario Outline: Example 1: Element on page that is hidden
        When user click on "<Example>"
        When user click on Start button
        Then loader is displayed
        Then Hello World is displayed
        Examples:
            | Example                                    |
            | Example 1: Element on page that is hidden  |
            | Example 2: Element rendered after the fact |


