# Pakistani Contact & CNIC Validator

A command-line tool that validates Pakistani CNIC numbers and mobile phone numbers using regular expressions, raises custom exceptions on invalid input, and saves valid entries to a CSV file.

## Why I Built This

Most beginner validator projects use generic US phone/zip formats. I wanted something tied to a real, local problem: Pakistani CNIC and mobile number formats are specific (13-digit CNIC, 03XX mobile prefix) and aren't covered by any standard library. This forced me to write my own regex patterns instead of copying a generic one.

## What It Does

- Accepts a CNIC in either `12345-1234567-1` or `1234512345671` format
- Accepts a phone number in either `0300-1234567` or `03001234567` format
- Validates both using regex
- Raises `InvalidCNICError` or `InvalidPhoneError` (custom exception classes) when the format is wrong, instead of letting the program crash with a generic error
- Saves valid, cleaned, and consistently formatted entries to `data/contacts.csv`

## How It Works

1. `validate_cnic()` strips dashes/spaces, checks the result is 13 digits, and re-formats it consistently
2. `validate_phone()` strips formatting and checks it against the regex pattern `^03\d{9}$`, which matches any 11-digit number starting with `03`
3. If validation fails, a custom exception is raised with a clear message — this keeps error handling separate from the main program logic
4. `save_to_csv()` appends a new row to `data/contacts.csv` using Python's built-in `csv` module
5. `main()` ties it together: takes input, runs validation, exits cleanly with `sys.exit()` on bad input instead of crashing

## Concepts Used (CS50P)

- Exception handling (custom exception classes, try/except)
- Regular expressions (`re.match`)
- File I/O (`csv.writer`, append mode)
- Functions with docstrings and single responsibilities
- `sys.exit()` for clean error termination

## How to Run

\`\`\`bash
python validator.py
\`\`\`

## How to Test

\`\`\`bash
pytest test_validator.py
\`\`\`

## Project Info

- Built: June 21–27, 2026
- Language: Python 3
- Tools: VS Code, pytest, Git
