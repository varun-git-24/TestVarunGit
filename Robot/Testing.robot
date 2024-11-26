*** Settings ***
Library                String
Library                Collections
Library                BuiltIn
Library                String

*** Variables ***
${sfp_value_of_module}    ''3.3394''

*** Keywords ***
Remove the single quote
    Log To Console        Strip String    ${sfp_value_of_module}    characters='

*** Test Cases ***
My Test
    Remove The Single Quote
