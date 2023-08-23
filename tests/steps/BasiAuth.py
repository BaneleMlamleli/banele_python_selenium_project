from behave import given, when, then
from pageobjects.BasiAuthDomain import BasicAuth

# @given('user is on the home page')
# def user_is_on_the_home_page(context):
#     context.current_page = BasicAuth()
#     context.current_page.home_page()

# @when('user clicks on "{basic_auth}"')
# def user_clicks_on_button_add_element(context, basic_auth):
#     context.current_page.click_on_link(basic_auth)

@then('user enter "{username}" and "{password}" and clicks on sign in button')
def user_enter_login_credentials_and_clicks_on_sign_in_button(context, username, password):
    context.current_page.user_credentials_verification(username, password)

@then('login status')
def login_status(context):
    context.current_page.login_status()