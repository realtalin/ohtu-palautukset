*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  elias  elias123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  elias123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  a  elias123
    Output Should Contain  Invalid username

Register With Valid Username And Too Short Password
    Input Credentials  elias  a1
    Output Should Contain  Invalid password

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  elias  onlyletters
    Output Should Contain  Invalid password

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123