package com.herokuapp.theinternet;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class LoginTest {

    @Test
    public void loginTest() {

        System.out.println("STARTING TEST...");

        // setting system property
        System.setProperty("webdriver.chrome.driver" , "src/main/resources/chromedriver");
        
        // create webdriver
        ChromeDriver driver = getChromeDriver();

        //sleep 3 secs
        sleep(2000);

        // open site
        // Create a separate properties files for this n n
        String url ="https://the-internet.herokuapp.com/login" ;
        driver.get(url);
        driver.manage().window().maximize();
        System.out.println("The site is opened and maximized");

        sleep(2000);

        // Input username password and press login
        WebElement username = driver.findElement(By.xpath("//input[@id='username']"));
        username.sendKeys("tomsmith");
        sleep(2000);

        WebElement password = driver.findElement(By.xpath("//input[@id='password']"));
        password.sendKeys("SuperSecretPassword!");
        sleep(2000);

        WebElement loginButton = driver.findElement(By.tagName("button"));
        loginButton.click();
        sleep(2000);

        //verify if login was successful
        WebElement logoutButton = driver.findElement(By.xpath("//a[@class='button secondary radius']"));
        sleep(4000);

        // close browser
        //driver.quit();

    }

    private static ChromeDriver getChromeDriver() {
        ChromeDriver driver;
        driver = new ChromeDriver();
        return driver;
    }

    public static void sleep(long m) {
        try {
            Thread.sleep(m);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    }

}