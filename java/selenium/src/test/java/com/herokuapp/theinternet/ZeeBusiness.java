package com.herokuapp.theinternet;

import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.annotations.Test;

public class ZeeBusiness {

    @Test
    public void ZeeBizTest(){

        System.setProperty("webdriver.chrome.driver" , "src/main/resources/chromedriver");
        // create webdriver
        ChromeDriver driver = getChromeDriver();

        //sleep 3 secs
        sleep(2000);


        driver.get("https://www.youtube.com/");
        driver.manage().window().maximize();

        WebElement searchBox = driver.findElement(By.xpath("//input[@id='search']"));
        searchBox.sendKeys("Zee Business Live");

        WebElement searchButton = driver.findElement(By.xpath("//button[@id='search-icon-legacy']"));
        searchButton.click();

        WebElement result = driver.findElement(By.xpath("//a[@aria-label='Zee Business LIVE | 1st DEC | Business & Financial News | share bazaar | Anil Singhvi | News Update by Zee Business 198,676 views']"));
        result.click();

        WebElement miniPlayerButton = driver.findElement(By.xpath("//button['data-tooltip-target-id='ytp-miniplayer-button']"));
        miniPlayerButton.click();



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
