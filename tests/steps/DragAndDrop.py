from behave import given, when, then
from pageobjects.DragAndDropDomain import DragAndDrop

@given('user is on the home page')
def user_is_on_the_home_page(context):
    context.current_page = DragAndDrop()
    context.current_page.home_page()

@when('user clicks on "{drag_and_drop}"')
def user_clicks_on_button_add_element(context, drag_and_drop):
    context.current_page.click_on_link(drag_and_drop)

@Then('drag and drop box A to box B')
def drag_and_drop_box_A_to_box_B(context):
    context.current_page.drag_and_drop_to_swap_boxes()