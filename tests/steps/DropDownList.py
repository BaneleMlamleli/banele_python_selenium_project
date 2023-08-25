from behave import given, when, then
from pageobjects.DropDownListDomain import DropDownList

# @given('user is on the home page')
# def user_is_on_the_home_page(context):
#     context.current_page = DropDownList()
#     context.current_page.home_page()

# @When('user clicks on "{dropdown}"')
# def user_clicks_on_button_add_element(context, dropdown):
#     context.current_page.click_on_link(dropdown) 

@then('user clicks on the dropdown element and select first option')
def user_clicks_on_the_dropdown_element_and_select_first_option(context):
    context.current_page.drop_down_option()