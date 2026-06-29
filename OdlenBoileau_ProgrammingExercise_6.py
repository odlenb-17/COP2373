import re

# Validate the phone number entered by the user.
def validate_phone(phone):
    pattern=r"^(\(\d{3}\)\s\d{3}-\d{4}|\d{3}-\d{3}-\d{4})$"
    return re.fullmatch(pattern,phone) is not None

# Validate the Social Security Number entered by the user.
def validate_ssn(ssn):
    return re.fullmatch(r"^\d{3}-\d{2}-\d{4}$",ssn) is not None

# Validate the ZIP code entered by the user.
def validate_zip(zip_code):
    return re.fullmatch(r"^\d{5}(-\d{4})?$",zip_code) is not None

# Run the program.
def main():
    phone=input("Enter a phone number (123-456-7890 or (123) 456-7890): ")
    ssn=input("Enter a Social Security Number (123-45-6789): ")
    zip_code=input("Enter a ZIP code (12345 or 12345-6789): ")

    print("\nValidation Results")
    print("------------------")
    print("Phone Number:", "Valid" if validate_phone(phone) else "Invalid")
    print("Social Security Number:", "Valid" if validate_ssn(ssn) else "Invalid")
    print("ZIP Code:", "Valid" if validate_zip(zip_code) else "Invalid")

if __name__=="__main__":
    main()
