package com.herokuapp.theinternet;

import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class LoginTest {

    @Test
    public static void main(String [] args) {

        System.out.println("STARTING TEST...");

        // setting system property
        System.setProperty("webdriver.chrome.driver" , "src/test/resources/chromedriver");
        
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

        //verify if login was successful


        // close browser
        driver.quit();

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