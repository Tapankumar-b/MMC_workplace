from selenium import webdriver

"""
1. Whatis webdriver?
2. How to handel selective dropdown, write a snippet for it?
3. How to handel auto suggestive dropdown, write a snippet for it.?
4. How to handel multiple windows and back to current window?
5. What StaleElementException?
6. Explain the wait mechanism, write syntax and snippet for it.
7. How to handle dynamic web element, (write at least 3 point)
8. How many locators in selenium
9. In webtable want to fetch 3rd Column , 3rd row data, write a xpath for it.
10. Write xpath
Steps.
 1.Navigate to https://www.nseindia.com/
"""

"""
Ans:1- 
it is an interface , through webriver we can communicate with browser.

Ans:2- 
8 Types of locaters are:
    Id,Class,Linktext,partial linktext,tag name,Xpath,CSS locator.
    
Ans:3-
dropdown = Select(driver.find_element(By.id("dropdown_id"))
dropdown.select_by_visible_text("Option Text")

Ans:6-
wait mechanisim used for stop the execution for certain time.
2 types of wait mechanisim implicit and explicit
implicit wait it will applicable for all
Syntax: time.sleep(10)
Explicit wait wi will applicable for specific element
syntax: wait = WebDriverWait(5)

Ans:7-
-using find_Elements
-Always we have to use Xpath(preceding, following,parent and child) or Css selector. 

Ans:10-
"""

