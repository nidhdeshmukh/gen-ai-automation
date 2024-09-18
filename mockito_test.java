import static org.mockito.Mockito.*;

import org.junit.Test;

public class MockitoTest {
    @Test
    public void testMocking() {
        // Create a mock of the service
        MyService myServiceMock = mock(MyService.class);
        when(myServiceMock.getData()).thenReturn("Mocked Data");

        // Use the mock
        MyComponent component = new MyComponent(myServiceMock);
        String result = component.processData();
        
        assertEquals("Processed Mocked Data", result);
    }
}
