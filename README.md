# Debit/Credit Card Validator

This Python program validates debit/credit card numbers using the Luhn algorithm.

## Overview

The Luhn algorithm, also known as the "modulus 10" or "mod 10" algorithm, is a simple checksum formula used to validate a variety of identification numbers, such as credit card numbers, IMEI numbers, and National Provider Identifier numbers. The algorithm is widely used to ensure the integrity of credit card numbers and prevent accidental errors or fraud.

This program provides a simple command-line interface for users to input their card numbers and determine whether they are valid according to the Luhn algorithm.

## Features

- Validates debit/credit card numbers based on the Luhn algorithm.
- Handles leading or trailing whitespace characters in the input.
- Supports card numbers with lengths ranging from 13 to 19 digits.

## Usage

1. Clone the repository to your local machine:

```
git clone https://github.com/yourusername/debit-credit-card-validator.git
```

2. Navigate to the project directory:

```
cd debit-credit-card-validator
```

3. Run the program:

```
python validator.py
```

4. Follow the prompts to input your card number.

5. The program will output whether the card number is valid or invalid.

## Example

```
Enter your card number: 4111111111111111
Valid card number.
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributions

Contributions are welcome! Please feel free to open an issue or submit a pull request with any improvements or bug fixes.
