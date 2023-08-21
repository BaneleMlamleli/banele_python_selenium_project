from behave import given, when, then
from pageobjects.ABTestingDomain import ABTesting

# @given('user is on the home page')
# def user_is_on_the_home_page(context):
#     context.current_page = ABTesting()
#     context.current_page.home_page()

# @when('user clicks on "{ab_testing}"')
# def user_clicks_on_AB_Testing(context, ab_testing):
#     context.current_page.click_on_link(ab_testing)
    
@then('user is redirected to the AB Test Variation 1 page')
def user_is_redirected_to_the_AB_Test_Variation_1_page(context):
    context.current_page.redirected_to_the_abTestVariation_page