# gen-ai-automation
This project uses OpenAI's API to generate test cases and provide conversational assistance. Built with Python, it leverages the latest GPT models. Clone the repo, install dependencies, set up your API key, and run the script to get started. Contributions welcome!
Automated Testing & Monitoring Framework for a Web/Mobile App Using GenAI
Description
This project develops an Automated Testing & Monitoring Framework utilizing GenAI to enhance and streamline testing for web and mobile applications. The framework integrates advanced testing tools and technologies to ensure robust and efficient testing processes.

Features
GenAI Integration: Leverage GenAI to identify automation test cases and optimize testing paths for both functional and non-functional testing.
Automation Framework: Build an automation suite using Selenium, Appium, Cypress, and REST Assured for comprehensive UI and API testing.
Security & Performance Testing: Automate security scans using ZAP and conduct performance tests with JMeter.
Mocking: Employ Mockito to simulate dependencies for effective unit testing.
Kubernetes: Establish a CI/CD pipeline that automates test executions and deployments within a Kubernetes cluster.

Installation
Clone the Repository

bash
Copy code
git clone https://github.com/nidhdeshmukh/gen-ai-automation.git

Navigate to the Project Directory

bash
Copy code
cd automated-testing-framework
Install Dependencies

For Python dependencies:

bash
Copy code
pip install -r requirements.txt

For Node.js dependencies (if applicable):

bash
Copy code
npm install
Set Up Configuration

Create a .env file for sensitive information such as API keys:

bash
Copy code
GENAI_API_KEY=fisty
Usage
Run Tests Locally

For UI testing with Selenium/Appium:

bash
Copy code
pytest tests/ui
For API testing with REST Assured:

bash
Copy code
mvn test
Run Security Scans

Execute ZAP scans:

bash
Copy code
zap-cli quick-scan --self-contained http://localhost:8080
Run Performance Tests

Start JMeter tests:

bash
Copy code
jmeter -n -t tests/performance/test-plan.jmx
CI/CD Pipeline

The pipeline is configured to run tests and deploy using Kubernetes. Ensure your CI/CD configurations (e.g., GitHub Actions, Jenkins) are set up correctly.

Contributing
Contributions are welcome! Please follow the CONTRIBUTING.md guidelines for details on how to contribute to this project.

License
This project is licensed under the MIT License.
