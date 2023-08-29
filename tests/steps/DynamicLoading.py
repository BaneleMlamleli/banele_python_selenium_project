from behave import given, when, then
from pageobjects.DynamicLoadingDomain import DynamicLoading

# @given('user is on the home page')
# def user_is_on_the_home_page(context):
#     context.current_page = DynamicLoading()
#     context.current_page.home_page()

# @when('user clicks on "{dynamic_loading}"')
# def user_clicks_on_button_add_element(context, dynamic_loading):
#     context.current_page.click_on_link(dynamic_loading)
    
@when('user click on "{example}"')
def user_click_on_an_example(context, example):
    context.current_page.clink_on_example_option(example)
    
@when('user click on start button')
def user_click_on_start_button(context):
    context.current_page.start_button()
    
@then('loader is displayed')
def loader_is_displayed(context):
    context.current_page.loader()
    
@then('Hello World is displayed')
def hello_world_is_displayed(context):
    context.current_page.hello_world()