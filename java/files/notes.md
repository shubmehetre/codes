# Selenium Workshop
> https://tcs2.webex.com/tcs2/onstage/g.php?MTID=e4cfc40ad474ab90edf18d5680dbb2dcd

Automation tool to test fucntionality of webapplication

## Why

- Its Open-Source!
- Available for all major browsers.
- Language support : java, c#, perl, python,

## Conponents

- Selenium IDE - Record and Playback feature
- Selenium WebDriver
- Selenium Grid

-------------------------------------------------------------------

## Selenium WebDriver

- Programmamatic part of selenium
- That is, all the actions that are tested are written as a program.
- According to the language is used.

## Pre-requisites

- JAVA 11
- Maven
- IDE (eclipse, intellij, etc any)

----------------------------------------------------------------

### Setup (using Eclipse)
eg.
Page Object model framework

- Create new  project
- add selenium server jar


### Framework

* Methodology to make code in structured format
* RRR - Reliable, Readable, Resuable

1. JUnit
2. TestNG

### Annotations

- BeforeEach => init webdriver, open browser, goto irl
- AfterEach => post testing steps, taking screenshots, close browser
- Test => actual tests, testing functionalities




===========================
### Missed

what is xpath??

> Refer: guru99.com/xpath-selenium.html

Best Practices:
never use absolute xpath

===========================
### Actions
#### Regular
- clicking on a particular webelement
driver.findElement(By.xpath("//input[@aria-label='Search']")).click();

- clearing a text web element
driver.findElement(By.xpath("//input[@aria-label='Search']")).clear();

- type input charecter to text box
driver.findElement(By.xpath("//input[@aria-label='Search']")).sendKeys("Samsung M51");

driver.findElement(By.xpath("//input[@aria-label='Search']")).sendKeys(Keys.ENTER);

- selecting a value from drop down
select class -->
	- div based
	- select based

select based -->
select select = new Select(driver.findElement(By.xpath("")))
this will pass control to dropdown to make selection from the drop down
make a selection : (possible by 3 ways)
	- select by value => select.SelectByValue("6000");
	- select by visible text => select.SelecyByVisible("");
	- select by index => select.SelectByIndex(4) ;
- If drop down present in some other tag, then
driver.findElement(By.xpath("//main button locator']")).click();
driver.findElement(By.xpath("//drop downed button locator']")).click();

#### Advanced

Actions actions = new Actions(driver);
actions.moveToElement(driver.findElement(By.xpath("//a[@asd='zxc']"))).build.perform();
actions.moveToElement(driver.findElement(By.xpath("//a[@asd='zxc']"))).click().build().perform();
actions.dragAndDrop("sourceXpath", "targetXpath").build().perform();

- handle alert popups
driver.switchTo().alert().accept(); ==> click yes
driver.switchTo().alert().dismiss(); ==> click no
driver.switchTo().alert().sendKeys("200"); ==> send chars to alert
String retrieveText = driver.switchTo().alert().getText(); ==> get txt from alert
String  = driver.switchTo().alert().getText(); ==> get txt from alert

------------

https://www.guru99.com/take-screenshot-selenium-webdriver.html16:36

----------------

# 29/10/21


data parameterization?? DDT
	- Property file
	- excel sheet
	- class level, constant java class
	- database
	- datasets

## TestNG


### Advantages

- more features
- more annotations
-
