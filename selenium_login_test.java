import org.openqa.selenium.By;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.WebElement;
import org.openqa.selenium.chrome.ChromeDriver;
import org.junit.Assert;
import org.junit.Test;

public class SeleniumLoginTest {
    @Test
    public void testLogin() {
        WebDriver driver = new ChromeDriver();
        driver.get("https://your-app-url.com/login");

        WebElement usernameField = driver.findElement(By.id("username"));
        WebElement passwordField = driver.findElement(By.id("password"));
        WebElement loginButton = driver.findElement(By.id("loginButton"));

        usernameField.sendKeys("testuser");
        passwordField.sendKeys("password");
        loginButton.click();

        String expectedTitle = "Dashboard";
        Assert.assertEquals(expectedTitle, driver.getTitle());

        driver.quit();
    }
}
