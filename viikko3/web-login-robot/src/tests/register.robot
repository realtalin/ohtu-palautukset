*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  elias
    Set Password  elias123
    Set Password Confirmation  elias123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  e
    Set Password  elias123
    Set Password Confirmation  elias123
    Submit Register Credentials
    Register Should Fail With Message  Invalid username

Register With Valid Username And Too Short Password
    Set Username  elias
    Set Password  e1
    Set Password Confirmation  e1
    Submit Register Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  elias
    Set Password  elias123
    Set Password Confirmation  elias321
    Submit Register Credentials
    Register Should Fail With Message  Passwords don't match

Login After Successful Registration
    Set Username  elias
    Set Password  elias123
    Set Password Confirmation  elias123
    Submit Register Credentials
    Register Should Succeed
    Go To Login Page
    Set Username  elias
    Set Password  elias123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  elias
    Set Password  e
    Set Password Confirmation  e
    Submit Register Credentials
    Register Should Fail With Message  Invalid password
    Go To Login Page
    Set Username  elias
    Set Password  e
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password




*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Register Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open