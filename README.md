## This project performs several tests on ebay's website

### The project runs under windows machine

##### The project is OOP-based and uses Page Object.
##### The page object represents an area in the web application UI.
##### This technique allows us to:

##### 1. Creating reusable code.
##### 2. Reducing duplicated code.
##### 3. In case of chaning in the user interface , we have to fix only in one place.

## Files and classes

### mytests.py
#### Includes the tests, each test is a unittest test case.
#### We use unittest and selenium webdriver and perform an assertions in order to pass or fail the tests

### webpage.py
#### Creating an object for each web page
#### This help us to create a seperation between the tests and the implementation

### weblocators.py
#### We separate the locator strings from the code which is using it.
#### We create a class for each web page that we have to use the locators on it.

### constants.py
#### Includes a constant text such as usernamw, password and other strings in order to use it instead of writing the value itself in a place we have to use it.

### TestSuite.py
#### We are using a test suite in order to run our tests one after the other
#### 1. Get all tests from WebSiteTests class using unittest.TestLoader()
#### 2. Create a test suite for my_tests
#### 3. Run the suite

### How to run the tests
#### 1. On command line go to the project directory
#### 2. Type python TestSuite.py



