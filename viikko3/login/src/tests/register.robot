*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  meemil
    Set Password  kalle123
    Set Password Confirmation  kalle123
    Click  button >> text=Register
    Register Should Succeed

Register With Password Containing A Special Character
    Set Username  meemil
    Set Password  kalle#abc
    Set Password Confirmation  kalle#abc
    Click  button >> text=Register
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  me
    Set Password  moimeemil
    Set Password Confirmation  moimeemil
    Click  button >> text=Register
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  meemil
    Set Password  meemil
    Set Password Confirmation  meemil
    Click  button >> text=Register
    Register Should Fail With Message  Password too short

Register With Password Containing Only Lowercase Letters
    Set Username  meemil
    Set Password  kallekalle
    Set Password Confirmation  kallekalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Password Containing Only Uppercase And Lowercase Letters
    Set Username  meemil
    Set Password  KalleKalle
    Set Password Confirmation  KalleKalle
    Click  button >> text=Register
    Register Should Fail With Message  Password must contain at least one non-letter character

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  moikalle123
    Set Password Confirmation  moikalle123
    Click  button >> text=Register
    Register Should Fail With Message  User with username kalle already exists

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Get Text  body  *=  ${message}

Set Username
    [Arguments]  ${username}
    Fill Text  id=username  ${username}

Set Password
    [Arguments]  ${password}
    Fill Secret  id=password  $password

Set Password Confirmation
    [Arguments]  ${password}
    Fill Secret  id=password_confirmation  $password

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
