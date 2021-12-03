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
        searchBox.sendKeys("Zee News Live");

        WebElement searchButton = driver.findElement(By.xpath("//button[@id='search-icon-legacy']"));
        searchButton.click();

        WebElement result = driver.findElement(By.xpath("//img[@src='https://i.ytimg.com/an_webp/0bnkSroqlOE/mqdefault_6s.webp?du=3000&sqp=CJ_Ko40G&rs=AOn4CLDc9qRTs3rVk6noVK3J3SygqWH7cQ']"));
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
