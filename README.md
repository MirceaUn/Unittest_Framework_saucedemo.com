About the project

The test cases (LoginTests and CartTests) and the test suite from this repository were created using the Unit Testing Framework. 

They were built in Python with:
- Unittest library
- Selenium
- HTMLTestRunner

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Test Cases description

1. LoginTests - for the website https://www.saucedemo.com/ I have tested the responses for the different types of login
   - testWrongCredentials asserts that, in case of wrong credentials, the error message is displayed
   - testSuccesfulLogin asserts that, in case of successful login, the current URL changes
   - testClickLoginNoCredentials asserts that, in case of no credentials, the error message is displayed
   - testGlitchUser asserts that, in case of an implicit wait of 10 seconds, eventually the current URL changes

2. CartTests - 
     
