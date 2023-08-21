from behave import given, when, then
from pageobjects.AddRemoveElementsDomain import AddRemoveElements

@given('user is on the home page')
def user_is_on_the_home_page(context):
    context.current_page = AddRemoveElements()
    context.current_page.home_page()

@When('user clicks on "{add_remove_element}"')
def user_clicks_on_button_add_element(context, add_remove_element):
    context.current_page.click_on_link(add_remove_element)    

@when('user clicks on Add Element button to add Delete button')
def user_clicks_on_add_elements_to_add_delete_button(context):
    context.current_page.redirected_to_the_add_remove_button_page()

@then('user clicks on Delete button to remove the button')
def user_clicks_on_delete_button_to_remove_the_button(context):
    context.current_page.user_clicks_on_the_delete_button()