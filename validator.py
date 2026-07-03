import re
import csv
import sys

class InvalidCnicError(Exception):
    pass

class InvalidPhoneError(Exception):
    pass

def main():
    print("=== Pakistani Contact Validator ===")
    try:
        cnic = input("Enter CNIC (xxxxx-xxxxxxx-x): ").strip()
        phone = input("Enter Phone (03xx-xxxxxxx): ").strip()
        validate_cnic(cnic)
        validate_phone(phone)
        save_to_csv(cnic, phone)
        print("Success: Valid CNIC and phone saved to data/contacts.csv")
    except InvalidCnicError:
        sys.exit("Error: CNIC must be in format xxxxx-xxxxxxx-x")
    except InvalidPhoneError:
        sys.exit("Error: Phone must be in format 03xx-xxxxxxx")

def validate_cnic(cnic):
    if not re.match(r"^\d{5}-\d{7}-\d{1}$", cnic):
        raise InvalidCnicError
    return True

def validate_phone(phone):
    if not re.match(r"^03\d{2}-\d{7}$", phone):
        raise InvalidPhoneError
    return True

def save_to_csv(cnic, phone):
    with open("data/contacts.csv", "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([cnic, phone])

if __name__ == "__main__":
    main()