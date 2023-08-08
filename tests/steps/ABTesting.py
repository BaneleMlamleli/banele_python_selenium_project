from behave import given, when, then
from pageobjects.ABTestingDomain import ABTesting

@given('user is on the home page')
def user_is_on_the_home_page(context):
    context.ABTesting = ABTesting
    context.ABTesting.home_page

@when('user clicks on AB Testing')
def user_clicks_on_AB_Testing(context):
    context.ABTesting.click_link
    
@then('user is redirected to the AB Test Variation 1 page')
def user_is_redirected_to_the_AB_Test_Variation_1_page(context):
    context.ABTesting.redirected