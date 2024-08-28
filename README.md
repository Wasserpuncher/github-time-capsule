# GitHub Time Capsule

## Overview

The GitHub Time Capsule project is a unique tool that allows users to create "time capsules" within a GitHub repository. These capsules are sealed until a specified future date, after which they can be opened to reveal their contents. The tool uses encryption to ensure that the contents remain secure until the designated date.

## Features

- **Sealed Capsules**: Create a sealed capsule with a specified opening date.
- **Secure Encryption**: The capsule's contents are encrypted using a secret key.
- **Future Proof**: Capsules cannot be opened before the specified date, ensuring the data remains a surprise.
- **Key Management**: A secret key is generated and provided to the user to decrypt the capsule when the time comes.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Wasserpuncher/github-time-capsule.git
   cd github-time-capsule
Install the required dependencies
 ```bash
pip install -r requirements.txt
 ```

## Usage

Create a Time Capsule
To create a new time capsule:

Run the script:

python kapsel.py


Select the option to create a new capsule ([v]ersiegeln).

Follow the prompts to set the opening date, capsule name, and data to be sealed.

Save the provided secret key; you will need it to open the capsule in the future.

Open a Time Capsule
To open a time capsule after the designated date:

Run the script:

python kapsel.py


Select the option to open a capsule ([ö]ffnen).

Provide the capsule name and secret key.

If the date has passed, the contents of the capsule will be revealed.

Testing
To run the tests:

python -m unittest discover -s tests


## Contribution
Feel free to contribute to this project by forking the repository and submitting pull requests.

## License
This project is licensed under the MIT License.
