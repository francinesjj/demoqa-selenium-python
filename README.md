# 🧪 DemoQA Automated Test Suite

A robust automated testing framework built using **Selenium** and **Python**, following the **Page Object Model (POM)** design pattern. This suite is designed to validate various components of [DemoQA](https://demoqa.com/), a practice web app for QA testing tools and concepts.

---

## 🚀 Technologies Used

- **Python 3.x**
- **Selenium WebDriver**
- **Pytest**
- **Page Object Model (POM)**
- **Faker** (for generating test data)
- **CSS Selectors and XPath Locators**
- **Google Chrome + ChromeDriver**
- **pytest-html** (for HTML reports)

---

## ✅ Project Features

- Modular structure using **Page Object Model**
- Automated tests for:
  - Web Elements (Buttons, Links, Textboxes, etc.)
  - Widgets (Accordions, Sliders)
  - Forms with dynamically generated data
- Custom assertions and validations
- HTML test reporting via `pytest-html`
- Organized folder structure for tests and page objects

---

## 🧪 Functions Tested

### Elements Module
- **TextBox**: Input and output validation
- **CheckBox**: Tree selection and state checking
- **RadioButton**: Selection states and result validation
- **WebTables**: Add/edit/delete functionality
- **Buttons**: Double click, right click, and dynamic click
- **Links**: API response codes (201, 204, 301, 400, 401, 403, 404)
- **Broken Pages**: Validates broken links and image handling
- **Dynamic Properties**: Verifies element state changes (enabled, visible, color) after delay
- **Radio Buttons**: Confirms selection and feedback messages
- **Uploads and Downloads**: Tests file upload and download functionality

### Forms Module
- **Practice Form**: Input validation with Faker data
- **Submission Result**: Table output verification

### Alerts, Frame & Windows Module
- **Alerts**: Handles simple, timed, confirmation, and prompt alerts
- **Browser Windows**: Tests opening and switching between new tabs and windows
- **Modals**: Validates display, content, and closing of modal dialogs

### Widgets Module
- **Accordian**: Expand/collapse section visibility
- **Slider**: Value change through drag
- **Progress Bar**: Completion tracking
- **Autocomplete**: Input suggestion and selection handling
- **Date Picker**: Date and month selection from calendar UI
- **Tabs**: Switches between tab content and validates active state
- **Menu**: Verifies multi-level hover navigation menu functionality and visibility of nested items
- **Select Menu**: Tests selection of dropdown values (single and multi-select) and validates selected options
- **Tool Tip**: Hovers over elements to trigger tooltip display and verifies correct tooltip text


---

## 🧪 How to Run the Tests

### 📁 1. Run All Tests

This command runs the entire test suite and generates a full HTML report:

```bash
pytest --html=report.html --self-contained-html
```

### 🔍 2. Run Individual Tests

To run a specific test file (e.g., link tests):

```bash
pytest tests/elements/test_link.py
```

---

## ⚠️ Disclaimer

This project is intended for **educational and demonstration purposes only**.  
The test cases are written against a public site: [https://demoqa.com/](https://demoqa.com/), which is designed for QA testing practice.

No ownership is claimed over the website, and tests may break if the site structure changes.

---

## 👨‍💻 Author

**Francine P. San Jose**  
*BS Information Technology – Major in Mobile and Web Development* 

📫 **Email**: franzsjj@gmail.com  

🌐 **GitHub**: https://github.com/francinesjj

💼 **LinkedIn**: https://www.linkedin.com/in/francinesanjose/



