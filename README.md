About the project - The scope of this suite is to test some of the functionalities of the Login Page and AddtoCart Page on the website: https://www.saucedemo.com/ 


Prerequisites

1. PyCharm 2024.3.2

The Python code for these tests was written using PyCharm 2024.3.2. The version of Python can be checked in cmd.exe using the command: "python --version". In my case, it is Python 3.12.

2. Unittest library

Unit Testing is the first level of software testing where the smallest testable parts of software are tested. The Python Unittest is a built-in testing framework that provides a set of tools for testing our code’s functionality in a more systematic and organized manner.

4. HTMLTestRunner-rv 1.1.2

It is a third-party library made to create HTML reports of the tests conducted. These reports are made in a human-readable presentation.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Installation and setup

1. A folder needs to be created in computer, where the code to run the app will be stored
2. A new project needs to be opened in PyCharm, a virtual environment needs to be created and for, each page where tests will be made, a PythonFile needs to be opened
3. In each PythonFile the Unittest Library and the Selenium Package will be used to automate the tests
4. For each set of tests 2 mandatory functions need to be created:
      - the SetUp function - for the economy of code all the steps prior to the actual test are written here (opening the website, maximizing the window, etc.)
      - the TearDown function - all the steps needed after running the test are written here (closing the website and browser)

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Test Cases description

1. LoginTests - for the website https://www.saucedemo.com/ I have tested the responses for the different types of login:
   - testWrongCredentials asserts that, in case of wrong credentials, the error message is displayed
   - testSuccesfulLogin asserts that, in case of successful login, the current URL changes
   - testClickLoginNoCredentials asserts that, in case of no credentials, the error message is displayed
   - testGlitchUser asserts that, in case of an implicit wait of 10 seconds, eventually the current URL changes

2. CartTests - after successfully logging in I have tested the following:
   - testCurrentURL - asserts that the current URL is the resulting one from the successful logging-in
   - testDropdownSortAscending - for the case when we want to sort the products on the page in ascending order it asserts that the sorting is correct and the products are ordered ascendingly
   - testAddToCart - asserts that, in case a product has been added to the cart, the "add to cart" button for that product becomes unavailable on the main page
   - testNumberProductsInCart - asserts that every time a product is added to the cart the number near the cart icon on the upper right part of the page is incremented
   - testCheckProductsInCart - asserts that, when clicking on the cart icon on the upper right part of the page, the URL changes to the "cart page"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Running the tests


 Test Suite - it is composed of the tests from LoginTests and Cart Tests and the results can be seen in the generated report
