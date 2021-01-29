*** Settings ***
Library     String
Library     Collections
Library     OperatingSystem
Library     DateTime
Library     SeleniumLibrary
Library     Process
Library     biblioteca.py

*** Test Cases ***
Banco de dados
    Get Movie     Paul M.    Christmastime   


*** Keywords ***
Get Movie  
    [Arguments]    ${artist}        ${song_title}

    get       ${artist}         ${song_title}