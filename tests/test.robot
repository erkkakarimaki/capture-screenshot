*** Settings ***
Library                QWeb
Library                OperatingSystem
Library                ../libraries/Capture.py
Suite Setup            OpenBrowser                about:blank    chrome
Suite Teardown         CloseAllBrowsers

*** Test Cases ***
Sample
    [Documentation]
    [Tags]
    GoTo               https://google.com
    ClickText          Accept all
    TypeText           q  Copado\n
    Sleep              2
    Create Directory    ${EXECDIR}/output/screenshots
    Capture Screenshot  path=${EXECDIR}/output/screenshots/foo.png
    Log                 <img src\="output/screenshots/foo.png">  html=True
