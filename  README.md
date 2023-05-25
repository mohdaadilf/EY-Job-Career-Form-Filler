# EY Job/Careers Form Automation

This Python program automates form field filling on the EY job/careers website.

## Prerequisites

Before running the program, please make sure you have the following:

- Python 3.x installed
- Selenium library installed (`pip install selenium`)
- Chrome WebDriver installed and added to the system PATH (Not important)

## Usage

1. Clone the repository to your local machine.
2. Create a separate Python file titled `DataValues.py` in the project directory.
3. Define values for all variables that may be undefined in the main program.
4. Run the main program by executing `python fillingouteyform.py`.

## Customizing DataValues.py

The `DataValues.py` file is used to store values for variables that may be undefined in the main program. This allows users to input their own values or remove undefined variables and provide the required values directly in the main program.

Ensure that you provide the necessary values for the following variables in `DataValues.py`:

- `username`: Your username for the EY job/careers website.
- `password`: Your password for the EY job/careers website.
- Other variables specific to the form fields you're automating.

## Why this program?

Applying for positions on the EY job/careers website can be challenging and time-consuming due to the large number of data fields that need to be filled. Additionally, many of these fields may not be necessary for your specific application, causing further frustration and confusion.

This program aims to simplify the application process by automating the form filling for multiple jobs at once. It allows you to quickly and efficiently fill the required fields while skipping unnecessary data fields, saving you time and effort.

Users who are unsure about using the program can try applying for positions manually by visiting the [EY job/careers website](https://eyglobal.yello.co/job_boards/c1riT--B2O-KySgYWsZO1Q?locale=en). However, for those who want to apply for multiple jobs more efficiently and avoid the hassle of unnecessary data fields, this program provides a streamlined solution.

## Notes

- Make sure you have a stable internet connection.
- The program uses the Chrome WebDriver. If you're using a different browser, you need to download the corresponding WebDriver and update the code accordingly.
- Code commenting may need improvement. Feel free to review and enhance the comments in the main program for better readability and understanding.

**Disclaimer: The author of this program shall not be held responsible for any errors, issues, or consequences arising from the usage of this program. Use it at your own risk and discretion.**

Feel free to customize the program and adapt it to your specific needs.

