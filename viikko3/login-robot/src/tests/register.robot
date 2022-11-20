*** Settings ***
Resource  resource.robot
Test Setup  Create User And Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials   kal   kalle123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials     kalle   kalle123
    Output Should Contain  User with username kalle already exists


Register With Too Short Username And Valid Password
    Input Credentials   ka   kalle123
    Output Should Contain  Username must contain at least 3 characters. Accepted characters are letters from a to z.

Register With Valid Username And Too Short Password
    Input Credentials   kaal      j9u
    Output Should Contain   Passwords must contain at least 8 characters and must not only contain letters.


Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  kelly  abcdefghijklmno
    Output Should Contain   Passwords must contain at least 8 characters and must not only contain letters.



*** Keywords ***
Create User And Input Register Command
    Create User  kalle  kalle123
    Input Register Command

