package com.herokuapp.theinternet;

import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class LoginTest {

    @Test
    public static void main(String [] args) {

        System.out.println("STARTING TEST...");

        // setting system property
        System.setProperty("webdriver.chrome.driver" , "src/main/resources/chromedriver");
        
        // create webdriver
        ChromeDriver driver = getChromeDriver();

        //sleep 3 secs
        sleep(2000);

        // login


        //verify if login was successful


        // close browser
        driver.quit();

    }

    private static ChromeDriver getChromeDriver() {
        ChromeDriver driver = new ChromeDriver();
        driver.get("https://the-internet.herokuapp.com/login");
        driver.manage().window().maximize();
        System.out.println("The site is opened and maximized");
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