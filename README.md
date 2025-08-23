# Browser Automator - Selenium Automation

A Python project using Selenium WebDriver for web automation tasks.

## Setup Instructions

### 1. Create a Virtual Environment (Recommended)


# Create a virtual environment
python3 -m venv venv
source venv/bin/activate

```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### Make sure you got Chrome

### Basic Usage

Run the main script to open Chrome and navigate to a website:

```bash
python main.py
```

By default, this script will:
- Open Chrome browser
- Navigate to Google.com
- Wait 5 seconds
- Display page information
- Close the browser

### Customization

You can modify the `main.py` file to:
- Change the target website URL
- Add custom automation logic
- Enable headless mode (no GUI)
- Add more Selenium interactions

## Features

- **Automatic ChromeDriver Management**: Uses webdriver-manager to automatically download and manage ChromeDriver
- **Optimized Chrome Settings**: Configured for stability and performance
- **Error Handling**: Exception handling and cleanup
- **Wait Strategies**: Uses explicit waits for better reliability
- **Anti-Detection**: Includes options to avoid detection as automated browser

## Project Structure

```
TikTok-Unfollower/
├── main.py              # Main Selenium automation script
├── requirements.txt     # Python dependencies
└── README.md           # This file
```

### Common Issues

1. **Chrome not found**: Make sure Google Chrome is installed
2. **Permission errors**: Run with appropriate permissions
3. **WebDriver issues**: The webdriver-manager should handle this automatically

### Headless Mode

To run on background, uncomment:
```python
chrome_options.add_argument("--headless")
```

## Next Steps

This template is a base for web automation. You can extend it by:
- Adding more sophisticated page interactions
- Implementing login functionality
- Adding data extraction capabilities
- Creating more complex automation workflows
