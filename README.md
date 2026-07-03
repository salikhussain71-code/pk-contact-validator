# Pakistani Contact & CNIC Validator

A command-line tool that validates Pakistani CNIC numbers and mobile phone numbers using regular expressions, raises custom exceptions on invalid input, and saves valid entries to a CSV file.

## Why I Built This

Most beginner validator projects use generic US phone or zip code formats. I wanted to work on something tied to a real, local problem instead. Pakistani CNIC numbers (13 digits) and mobile numbers (03XX prefix) follow specific formats that aren't covered by any built-in library, so I had to write my own regex patterns and figure out the validation logic myself rather than reuse something generic.

## What It Does

- Accepts a CNIC in either `12345-1234567-1` or `1234512345671` format
- Accepts a phone number in either `0300-1234567` or `03001234567` format
- Validates both using regular expressions
- Raises custom exceptions (`InvalidCNICError`, `InvalidPhoneError`) when the format is wrong, instead of letting the program crash with a generic Python error
- Saves valid, cleaned, and consistently formatted entries to `data/contacts.csv`

## How It Works

1. `validate_cnic()` strips out dashes and spaces, checks that the result is exactly 13 digits, then re-formats it consistently as `XXXXX-XXXXXXX-X`
2. `validate_phone()` strips formatting and checks it against the pattern `^03\d{9}$`, which matches any 11-digit number starting with `03`
3. If validation fails, a custom exception is raised with a clear error message. Keeping exception handling separate from the main logic makes the code easier to read and extend later
4. `save_to_csv()` appends a new row to `data/contacts.csv` using Python's built-in `csv` module
5. `main()` ties everything together: takes user input, runs it through validation, and exits cleanly with `sys.exit()` if something's wrong instead of crashing with a traceback

## Concepts Used (CS50P)

- Exception handling (custom exception classes, try/except, sys.exit)
- Regular expressions (re.match)
- File I/O (csv.writer, append mode)
- Functions with single responsibilities and docstrings

## How to Run
