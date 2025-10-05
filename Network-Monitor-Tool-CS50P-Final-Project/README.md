# NetSage - Network Monitor Tool (CLI Edition)
#### Video Demo: <https://youtu.be/_gS_DNmrXtE?si=sQu8NxQBiQaqcjkB>
#### Description:

**NetSage** is a **command-line tool** for monitoring and analyzing your internet connection.  
This project is my **Final Project for CS50P**. It applies everything I learned in CS50’s *Introduction to Programming with Python*, such as functions, error handling, external libraries, data persistence, and testing.

This is **Version 1 (CLI-only)** of NetSage, submitted for CS50P.  
I am also working on **Version 2 (CLI + GUI)** which will be published on GitHub. The GUI version will include enhanced visualization and interactivity.

---

## Features
NetSage provides the following features directly from the CLI:

- **Run Speed Test**  
  Measure download speed, upload speed, and ping.

- **Automatic Speed Tests**  
  Continuously test speeds every X seconds with thresholds and alerts.

- **Live Internet Status**  
  Monitor whether you are online, offline, or having DNS issues, with troubleshooting suggestions.

- **Compare with Global Average**  
  Compare your internet speed against your country’s average.

- **Wi-Fi Signal Strength**  
  Check Wi-Fi quality and get troubleshooting tips.

- **ISP & Location Info**  
  Show your public IP, ISP, city, region, country, postal code, and timezone.

- **Website/URL Info**  
  Check if a website is online, view response time, SSL status, domain information, and server IP.

- **Test History**  
  Save and display past test results in a table or interactive graph.

- **Export Logs**  
  Export speed test history to PDF.

- **Manage Data**  
  Delete all saved history when needed.

---

## CLI Commands
Users interact with NetSage via the following commands:

- `speed-test` / `st` - Run network speed test
- `auto-test` / `at` - Run automatic speed tests every X seconds
- `status` / `stts` - Live internet status
- `compare-global` / `cg` - Compare your speed to global average
- `signal` / `sgnl` - Wi-Fi strength + troubleshooting tips
- `isp` - Show ISP & location info
- `url-info` / `url` - Get info about a website or URL
- `table-history` / `th` - Show past results in a table
- `graph-history` / `gh` - Show past results as graph
- `export` / `xprt` - Export logs to PDF
- `delet` / `dlt` - Delete all saved test history
- `exit` or `Ctrl+C` / `xt` - Exit the application

---

## File Structure
For CS50P submission, the project is organized as:

```
project/
├── project.py        # main entry + all CLI features
├── test_project.py  # pytest tests for at least 3 functions
├── requirements.txt  # external dependencies
└── README.md        # this file
```

### project.py
- Contains `main()` as the entry point.
- Defines all CLI feature functions (speed test, internet status, ISP info, etc.).
- Includes a command parser to handle user input.

### test_project.py
- Implements pytest test cases for at least 3 custom functions:
  - `test_check_speed()`
  - `test_check_internet()`
  - `test_check_website_stat()`

### requirements.txt
External dependencies:
- `prettytable` (for CLI tables)
- `fpdf` (for PDF export)
- `requests` (for API and HTTP requests)
- `colorama` (for colorful CLI output)
- `speedtest-cli` (to perform the speed tests)
- `plotly` (for creating data visualisation graphs)
- `pytest` (for testing the code functions)
---

## Design Choices
- Modular functions: each feature has its own function for clarity and testing.
- Colorful CLI with `colorama` for a professional, user-friendly experience.
- Database-backed history of tests (SQLite).
- Export functionality via `fpdf` for portability.
- CLI menus use emojis and structured output for readability.

---

## Reflections
NetSage is my **first complete project** after learning Python with CS50P.  
I started it in February 2025 with zero programming knowledge and slowly built it up feature by feature.  

Looking back, I now see design choices I could improve, but I decided to keep this version as-is to represent my CS50P learning progress. The app works fully and shows how I applied the basics of Python to a real-world tool.  

Future work will focus on Version 2 (GUI + CLI), with more polished architecture and modern design patterns. You can see it in my [GitHub](https://github.com/HossamJa/NetSage-Network-Monitoring-Tool).

---

## How to Run
1. Install requirements:

```bash
pip install -r requirements.txt
```

2. Start the app:

```bash
python project.py
```

3. Run tests:

```bash
pytest test_project.py
```

---

## Author
- **Name**: Hossam Jamjama

- **Submission Date**:  05 October 2025
