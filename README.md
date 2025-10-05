# CS50P Problem Sets Showcase

Welcome to my repository showcasing all the problem challenges I completed as part of **CS50’s Introduction to Programming with Python**! This repository contains solutions to the problem sets from the course, organized by lecture topics and problem names. Each problem is implemented in Python and stored in its own folder, reflecting the skills learned in the corresponding lecture. My final project, **NetSage**, is hosted in a separate repository, linked below.

This project represents my journey from a beginner to a confident Python programmer, applying concepts like functions, conditionals, loops, exceptions, libraries, unit tests, file I/O, regular expressions, object-oriented programming, and more.

---

## 📚 Course Overview

CS50’s Introduction to Programming with Python is a beginner-friendly course that covers the fundamentals of programming using Python. The course is structured around 10 lectures, each accompanied by a problem set to reinforce the concepts:

1. **Functions, Variables**
2. **Conditionals**
3. **Loops**
4. **Exceptions**
5. **Libraries**
6. **Unit Tests**
7. **File I/O**
8. **Regular Expressions**
9. **Object-Oriented Programming**

Each problem set contains multiple challenges that test the skills introduced in the respective lecture. Below, I describe each problem set and the individual problems within them, organized by their folder names in this repository.

---

## 📂 Repository Structure

The repository is organized with each problem in its own folder, named after the problem. Each folder contains the corresponding `.py` file(s) with the solution. Test files for problems requiring unit tests are also included in their respective folders or in a dedicated `test` folder. The structure is as follows:

```
CS50P-Problem-Sets/
├── adieu/
├── bank/
├── bitcoin/
├── camel/
├── coke/
├── deep/
├── einstein/
├── emojize/
├── extensions/
├── faces/
├── figlet/
├── fuel/
├── game/
├── grocery/
├── indoor/
├── interpreter/
├── jar/
├── lines/
├── meal/
├── numb3rs/
├── nutrition/
├── pizza/
├── plates/
├── playback/
├── professor/
├── response/
├── scourgify/
├── seasons/
├── shirt/
├── shirtificate/
├── taqueria/
├── test/
├── test_bank/
├── test_fuel/
├── test_plates/
├── test_twttr/
├── tip/
├── twttr/
├── um/
├── watch/
├── working/
```

---

## 🛠️ Problem Sets and Solutions

### Problem Set 0: Functions, Variables
This problem set introduces basic Python syntax, focusing on functions and variables.

- **indoor/** (`indoor.py`): Prompts the user for input and outputs it in lowercase, preserving punctuation and whitespace.
- **playback/** (`playback.py`): Takes user input and replaces spaces with "...", simulating slowed-down speech.
- **faces/** (`faces.py`): Converts text-based emoticons `:-)` to 🙂 and `:-(` to 🙁 using a `convert` function, with a `main` function to prompt and print the result.
- **einstein/** (`einstein.py`): Calculates energy (in Joules) from mass (in kilograms) using Einstein’s formula \( E = mc^2 \), where \( c = 300,000,000 \) m/s.
- **tip/** (`tip.py`): Implements a tip calculator that converts a dollar amount (e.g., `$50.00`) and percentage (e.g., `15%`) to floats and calculates the tip amount.

### Problem Set 1: Conditionals
This set focuses on conditional statements to control program flow.

- **deep/** (`deep.py`): Checks if the user’s input is `42`, `forty-two`, or `forty two` (case-insensitive) and outputs `Yes` or `No` accordingly.
- **bank/** (`bank.py`): Outputs `$0` for greetings starting with `hello`, `$20` for greetings starting with `h` (but not `hello`), and `$100` otherwise, ignoring case and leading whitespace.
- **extensions/** (`extensions.py`): Maps file extensions (e.g., `.gif`, `.jpg`, `.pdf`) to their corresponding MIME types, defaulting to `application/octet-stream` for unknown extensions.
- **interpreter/** (`interpreter.py`): Evaluates arithmetic expressions in the format `x y z` (e.g., `1 + 1`) and outputs the result as a float to one decimal place.
- **meal/** (`meal.py`): Takes a time in 24-hour format (e.g., `7:30`) and outputs whether it’s `breakfast time`, `lunch time`, or `dinner time` based on predefined time ranges.

### Problem Set 2: Loops
This set emphasizes loops for repetitive tasks.

- **camel/** (`camel.py`): Converts camelCase variable names (e.g., `firstName`) to snake_case (e.g., `first_name`).
- **coke/** (`coke.py`): Simulates a vending machine that accepts 25¢, 10¢, or 5¢ coins until at least 50¢ is inserted, then outputs change owed.
- **twttr/** (`twttr.py`): Removes vowels (A, E, I, O, U) from user input, mimicking Twitter’s original name.
- **plates/** (`plates.py`): Validates vanity license plates based on Massachusetts rules (e.g., starts with two letters, max 6 characters, numbers at the end).
- **nutrition/** (`nutrition.py`): Outputs calorie counts for fruits based on the FDA’s poster, handling case-insensitive input.

### Problem Set 3: Exceptions
This set focuses on handling errors and exceptions.

- **fuel/** (`fuel.py`): Converts a fraction (e.g., `3/4`) to a percentage, outputting `E` for ≤1%, `F` for ≥99%, or the percentage otherwise, handling `ValueError` and `ZeroDivisionError`.
- **taqueria/** (`taqueria.py`): Calculates the total cost of items ordered from Felipe’s Taqueria menu, prompting for items until `Ctrl+D` and displaying the running total.
- **grocery/** (`grocery.py`): Creates an alphabetically sorted grocery list in uppercase, counting occurrences of each item until `Ctrl+D`.
- **outdated/** (`outdated.py`): Converts dates from month-day-year (e.g., `9/8/1636` or `September 8, 1636`) to ISO 8601 format (`YYYY-MM-DD`), re-prompting for invalid inputs.

### Problem Set 4: Libraries
This set introduces the use of Python libraries.

- **emojize/** (`emojize.py`): Converts emoji codes (e.g., `:thumbs_up:` or `:thumbsup:`) to their corresponding emoji (e.g., 👍) using a library.
- **figlet/** (`figlet.py`): Outputs text in a specified or random FIGlet font, exiting with an error for invalid command-line arguments.
- **adieu/** (`adieu.py`): Formats a list of names (entered until `Ctrl+D`) with proper punctuation, e.g., `Adieu, adieu, to Liesl, Friedrich, and Louisa`.
- **game/** (`game.py`): Implements a number-guessing game where the user guesses a random number between 1 and a chosen level, with feedback like `Too small!` or `Too large!`.
- **professor/** (`professor.py`): Simulates a math game generating 10 addition problems based on a chosen level (1, 2, or 3 digits), tracking the score and allowing up to three tries per problem.
- **bitcoin/** (`bitcoin.py`): Queries the CoinCap v3 API to calculate the cost of a specified number of Bitcoins in USD, handling invalid inputs and API errors.

### Problem Set 5: Unit Tests
This set focuses on writing unit tests using `pytest`.

- **test_twttr/** (`test_twttr.py`): Tests the `shorten` function from `twttr.py`, ensuring vowels are correctly removed.
- **test_bank/** (`test_bank.py`): Tests the `value` function from `bank.py` for correct greeting value assignments.
- **test_plates/** (`test_plates.py`): Tests the `is_valid` function from `plates.py` for vanity plate validation.
- **test_fuel/** (`test_fuel.py`): Tests the `convert` and `gauge` functions from `fuel.py` for fraction-to-percentage conversion and output formatting.

### Problem Set 6: File I/O
This set involves reading and writing files.

- **lines/** (`lines.py`): Counts lines of code in a Python file, excluding comments and blank lines, with error handling for invalid inputs.
- **pizza/** (`pizza.py`): Converts a CSV file of pizza prices into an ASCII art table using the `tabulate` library’s grid format.
- **scourgify/** (`scourgify.py`): Splits a CSV file’s `name` column into `first` and `last` names, writing to a new CSV file.
- **shirt/** (`shirt.py`): Overlays a shirt image onto a user-provided photo, resizing and cropping the input to match, and saves the result.

### Problem Set 7: Regular Expressions
This set focuses on using regular expressions for pattern matching.

- **numb3rs/** (`numb3rs.py`, `test_numb3rs.py`): Validates IPv4 addresses using a `validate` function, with tests to ensure correctness.
- **watch/** (`watch.py`): Extracts YouTube URLs from HTML iframe `src` attributes and converts them to `youtu.be` format.
- **working/** (`working.py`, `test_working.py`): Converts 12-hour time ranges (e.g., `9:00 AM to 5:00 PM`) to 24-hour format, raising `ValueError` for invalid inputs, with tests.
- **um/** (`um.py`, `test_um.py`): Counts occurrences of “um” as a standalone word in text, case-insensitively, with tests.
- **response/** (`response.py`): Validates email addresses using `validator-collection` or `validators`, printing `Valid` or `Invalid`.

### Problem Set 8: Object-Oriented Programming
This set introduces object-oriented programming concepts.

- **seasons/** (`seasons.py`, `test_seasons.py`): Calculates a user’s age in minutes from their birth date, outputting it in words (e.g., `five hundred twenty-five thousand six hundred`), with tests.
- **jar/** (`jar.py`, `test_jar.py`): Implements a `Jar` class to manage cookies with methods for depositing, withdrawing, and checking capacity and size, with tests.
- **shirtificate/** (`shirtificate.py`): Generates a personalized CS50 shirtificate PDF using `fpdf2`, overlaying the user’s name on a shirt image.

---

## 🌟 Final Project

My final project for CS50P, **[NetSage](Network-Monitor-Tool-CS50P-Final-Project/)**, is a command-line network monitoring tool . 

The updated version of it with CLI and GUI, is hosted in a separate repository:

🔗 [NetSage-Network-Monitoring-Tool](https://github.com/HossamJa/NetSage-Network-Monitoring-Tool)

NetSage allows users to monitor internet speed, Wi-Fi signal strength, ISP information, and more, with features like data visualization and PDF export. The CLI version was submitted for CS50P, while the GUI version is an ongoing enhancement.

---

## 🚀 How to Run

Each problem can be run individually by navigating to its folder and executing the Python script. For example:

```bash
cd indoor
python indoor.py
```

For problems requiring dependencies (e.g., `tabulate`, `pyfiglet`, `fpdf2`, `Pillow`), install them using:

```bash
pip install <package-name>
```

For problems with unit tests, run:

```bash
pytest test_<problem>.py
```

Ensure you have Python and `pytest` installed. Some problems (e.g., `bitcoin.py`) require an API key from [CoinCap](https://coincap.io/).

---

## 📝 Reflections

Completing CS50P was a transformative experience. Starting with no programming knowledge, I learned to write Python code to solve real-world problems. Each problem set built on the previous one, reinforcing concepts through practical application. Highlights include:

- Mastering string manipulation and conditionals in Problem Set 0 and 1.
- Learning to handle user input and errors robustly in Problem Set 3.
- Exploring Python libraries and APIs in Problem Set 4.
- Gaining confidence in testing and debugging with Problem Set 5.
- Working with files and regular expressions in Problem Sets 6 and 7.
- Applying object-oriented programming to create reusable classes in Problem Set 8.

The final project, NetSage, was a culmination of these skills, allowing me to build a fully functional application. This repository is a testament to my growth as a programmer and my enthusiasm for continuing to learn and build.

---

## 🙏 Acknowledgments

Thanks to the CS50 team, led by Professor David J. Malan, for creating an engaging and accessible course. The problem sets were challenging yet rewarding, and the community support on platforms like Discord and Reddit was invaluable.

---

Feel free to explore the code, provide feedback, or reach out with questions!
