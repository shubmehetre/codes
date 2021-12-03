package com.herokuapp.theinternet;

import org.openqa.selenium.By;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.Assert;
import org.testng.annotations.Test;

import java.util.Objects;

public class LoginTest {

    @Test
    public void loginTest() {

        System.out.println("STARTING TEST...");

        // setting system property
        System.setProperty("webdriver.chrome.driver" , "src/main/resources/chromedriver");
        
        // create webdriver
        ChromeDriver driver = getChromeDriver();

        // open site
        // Create a separate properties files for this n n
        String url ="https://the-internet.herokuapp.com/login" ;
        driver.get(url);
        driver.manage().window().maximize();

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
        String currentUrl  = driver.getCurrentUrl();

        String finalUrl = "https://the-internet.herokuapp.com/secure";

        sleep(4000);
        Assert.assertEquals(finalUrl, currentUrl, "GO HOME");

        WebElement logoutButton = driver.findElement(By.xpath("//a[@class='button secondary radius']"));
        Assert.assertTrue(logoutButton.isDisplayed(), "Logout button not visible" );
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