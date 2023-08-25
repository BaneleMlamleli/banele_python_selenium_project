@DragAndDrop
Feature: Demonstration when elements are dragged and dropped.

    Background: landing page
        Given user is on the home page
        When user clicks on "Drag and Drop"

    Scenario: Dragging and dropping elements
        Then drag and drop box A to box B