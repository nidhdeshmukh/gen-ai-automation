import io.restassured.RestAssured;
import io.restassured.response.Response;
import org.junit.Test;
import static org.hamcrest.Matchers.equalTo;

public class ApiTestRestAssured {
    @Test
    public void testLoginAPI() {
        RestAssured.baseURI = "https://your-api-url.com";

        Response response = RestAssured.given()
            .param("username", "testuser")
            .param("password", "password")
            .when()
            .post("/login")
            .then()
            .statusCode(200)
            .body("message", equalTo("Login successful"))
            .extract().response();

        System.out.println(response.asString());
    }
}
