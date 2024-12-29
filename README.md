About the project

The test cases (LoginTests and CartTests) and the test suite from this repository were created using the Unit Testing Framework. 

They were built in Python with:
- Unittest library
- Selenium
- HTMLTestRunner

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Test Cases description

1. LoginTests - for the website https://www.saucedemo.com/ I have tested the responses for the different types of login:
   - testWrongCredentials asserts that, in case of wrong credentials, the error message is displayed
   - testSuccesfulLogin asserts that, in case of successful login, the current URL changes
   - testClickLoginNoCredentials asserts that, in case of no credentials, the error message is displayed
   - testGlitchUser asserts that, in case of an implicit wait of 10 seconds, eventually the current URL changes

2. CartTests - after successfully logging in I have tested the following:
   - testCurrentURL - asserts that the current URL is the resulting one from the successful logging in
   - testDropdownSortAscending - for the case when we want to sort the products on the page in ascending order it asserts that the sorting is correct and the products are ordered ascendingly
   - testAddToCart - asserts that, in case a product has been added to the cart, the "add to cart" button for that product becomes unavailable on the main page
   - testNumberProductsInCart - asserts that every time a product is added to the cart the number near the cart icon on the upper right part of the page is incremented
   - testCheckProductsInCart - asserts that, when clicking on the cart icon on the upper right part of the page, the URL changes to the "cart page"

------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

 Test Suite - it is composed of the tests from LoginTests and Cart Tests and the results can be seen in the generated report
