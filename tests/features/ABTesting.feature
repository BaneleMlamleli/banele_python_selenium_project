@ABTesting
Feature: AB Test Variation 1

    Background: landing page
        Given user is on the home page
        When user clicks on "A/B Testing"

    Scenario: AB Test Variation 1
        Then user is redirected to the AB Test Variation 1 page