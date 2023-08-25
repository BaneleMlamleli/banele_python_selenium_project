from behave import given, when, then
from pageobjects.FormAuthenticationDomain import FormAuthentication

# @given('user is on the home page')
# def user_is_on_the_home_page(context):
#     context.current_page = FormAuthentication()
#     context.current_page.home_page()

# @When('user clicks on "{form_authentication}"')
# def user_clicks_on_button_add_element(context, form_authentication):
#     context.current_page.click_on_link(form_authentication)

@then('user enter "{username}" and "{password}" for authentication')
def user_enter_username_and_password(context, username, password):
    context.current_page.user_enter_login_credentials(username, password)
    
@then('user clicks on login button and login message is displayed')
def user_clicks_on_login_button(context):
    context.current_page.login_and_confirm_login_message()