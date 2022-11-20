*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup   Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username   kal
    Set Password   kalle123
    Set Password Confirmation   kalle123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username   k
    Set Password   kalle123
    Set Password Confirmation  kalle123
    Submit Credentials
    Register Should Fail With Message  Username must contain at least 3 characters. Accepted characters are letters from a to z.


Register With Valid Username And Too Short Password
    Set Username  kallekalle
    Set Password   kal
    Set Password Confirmation  kal
    Submit Credentials
    Register Should Fail With Message  Passwords must contain at least 8 characters and must not only contain letters.

Register With Nonmatching Password And Password Confirmation
    Set Username  kallekalle
    Set Password   kal123456
    Set Password Confirmation  kalevi123
    Submit Credentials
    Register Should Fail With Message  Passwords did not match

Login After Successful Registration
    Go To Login Page
    Set Username  kalle
    Set Password  kalle123
    Submit Credentials Login
    Login Should Succeed

Login After Failed Registration
    Go To Login Page
    Set Username  kallekalle
    Set Password   kal
    Submit Credentials Login
    Login Should Fail With Message   Invalid username or password


*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Submit Credentials Login
    Click Button   Login

Register Should Succeed
    Welcome Page Should Be Open

Create User And Go To Register Page
    Create User  kalle  kalle123
    Go To Register Page
    Register Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}