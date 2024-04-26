from behave import given, when, then

@given(u'I navigate to Register Page')
def step_impl(context):
    print("Inside - I navigate to Register Page")


@when(u'I enter details into mandatory fields')
def step_impl(context):
    print("Inside - I enter details into mandatory fields")


@when(u'I click on Continue button')
def step_impl(context):
    print("Inside - I click on Continue button")


@then(u'Account should be created successfully')
def step_impl(context):
    print("Inside - Account should be created successfully")


@when(u'I enter details into all fields')
def step_impl(context):
    print("Inside - I enter details into all fields")


@when(u'I enter details into all fields except email field')
def step_impl(context):
    print("Inside - I enter details into all fields except email field")


@when(u'I enter existing account email into email field')
def step_impl(context):
    print("Inside - I enter existing account email into email field")


@then(u'Proper warning message informing about duplicate account should be displayed')
def step_impl(context):
    print("Inside - Proper warning message informing about duplicate account should be displayed")


@then(u'Proper warning message informing about mandatory fields should be displayed')
def step_impl(context):
    print("Inside - Proper warning message informing about mandatory fields should be displayed")

