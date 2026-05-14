# 🎮 Python Mini Games Collection

This repository contains eight fun and beginner-friendly Python projects:

1. **Number Guessing Game (with difficulty levels)**
2. **Rock Paper Scissors**
3. **Dice Probability Game**
4. **Random Password Generator**
5. **Password Strength Validator**
6. **OTP Generator**
7. **Pangram Checker**
8. **Message Encoder**

These projects are great for learning basic Python concepts like loops, conditionals, user input, and random number generation.

---

# 🔢 Number Guessing Game

A simple and fun Python game where the computer randomly selects a number, and the player tries to guess it within a limited number of attempts.

---

## 📌 Features

* Random number generation 🎲
* User input with hints (too high / too low)
* Limited attempts for challenge
* Beginner-friendly logic

---

## 🧠 How It Works

* The program generates a random number within a given range
* The player keeps guessing the number
* After each guess, feedback is provided:

  * Too high 📈
  * Too low 📉
* The game ends when:

  * The player guesses correctly 🎉
  * OR runs out of attempts ❌

---

## 🎮 Usage

* Enter guesses when prompted
* Follow the hints to reach the correct number
* Try to guess within the allowed attempts

---

## 🛠️ Code Overview

* `random.randint()` → generates random number
* Loop → handles repeated guesses
* Conditional statements → check user input and provide hints

---

# ✊✋✌️ Rock Paper Scissors Game

A simple Python implementation of the classic Rock, Paper, Scissors game where you play against the computer.

---

## 📌 Features

* Play against computer 🤖
* Random computer choices
* Instant result (Win / Lose / Draw)
* Option to play multiple rounds 🔁
* Beginner-friendly code

---

## 🧠 How It Works

* The player selects:

  * Rock ✊
  * Paper ✋
  * Scissors ✌️
* The computer randomly selects one option
* Rules:

  * Rock beats Scissors
  * Scissors beats Paper
  * Paper beats Rock
* The winner is decided based on these rules

---

## 🎮 Usage

* Enter your choice: `rock`, `paper`, or `scissors`
* The computer will make its choice
* The result will be displayed instantly
* Choose to play again or exit

---

## 🛠️ Code Overview

* `get_computer_choice()` → randomly selects move
* `random.choice()` → generates computer’s move
* `get_user_choice()` → takes user input
* Conditional statements → decide winner
* Loop → enables multiple rounds

---

# 🎲 Dice Probability Game

A simple Python program that calculates and displays the probability of getting a specific sum when rolling two dice.

---

## 📌 Features

* Calculates probability of sums from **2 to 12**
* Simulates rolling two dice 🎲
* Displays result instantly
* Beginner-friendly Python code

---

## 🧠 How It Works

* Each die has 6 faces → total outcomes = **36**
* The program checks all possible combinations of two dice
* Counts how many combinations match the chosen sum
* Uses the formula:

```
Probability = Favorable Outcomes / Total Outcomes
```

---

## 🎮 Usage

* Enter a number between **2 and 12**
* The program will:

  * Show the probability of getting that sum
  * Roll two dice
  * Tell you if you won or not

---

## 📈 Probability Reference Table

| Sum | Probability   |
| --- | ------------- |
| 2   | 1/36 (2.78%)  |
| 3   | 2/36 (5.56%)  |
| 4   | 3/36 (8.33%)  |
| 5   | 4/36 (11.11%) |
| 6   | 5/36 (13.89%) |
| 7   | 6/36 (16.67%) |
| 8   | 5/36 (13.89%) |
| 9   | 4/36 (11.11%) |
| 10  | 3/36 (8.33%)  |
| 11  | 2/36 (5.56%)  |
| 12  | 1/36 (2.78%)  |

---

## 🛠️ Code Overview (Dice Probability Game)

* `calculate_probability()` → calculates probability of a given sum
* Nested loops → check all 36 possible dice combinations
* `roll_dice()` → generates two random numbers (dice rolls)
* `random.randint()` → simulates each die (1 to 6)
* `dice_game()` → controls the game flow
* Conditional statements → validate input and check win/loss

---

# 🔐 Random Password Generator

A simple Python program that generates strong and secure random passwords based on user preferences.

---

## 📌 Features

* Generates random passwords 🔑
* Customizable password length
* Includes letters, numbers, and symbols
* Strong and secure output
* Beginner-friendly code

---

## 🧠 How It Works

* The user specifies the desired password length
* The program combines:

  * Uppercase and lowercase letters
  * Numbers
  * Special characters
* A random selection is made to create a secure password

---

## 🎮 Usage

* Enter the desired password length
* The program generates and displays a random password
* Run again to generate a new password

---

## 🛠️ Code Overview

* `generate_password()` → creates random password
* `random.choice()` → selects random characters
* Character sets → letters, digits, symbols
* Loop → builds password of given length

---

# 🔒 Password Strength Validator

A simple Python program that checks the strength of a password based on common security rules.

---

## 📌 Features

* Evaluates password strength 🔍
* Checks for length, letters, numbers, and symbols
* Provides feedback (Weak / Medium / Strong)
* Helps improve password security
* Beginner-friendly code

---

## 🧠 How It Works

* The user enters a password
* The program checks for:

  * Minimum length
  * Uppercase and lowercase letters
  * Numbers
  * Special characters
* Based on these checks, it classifies the password strength

---

## 🎮 Usage

* Enter a password when prompted
* The program analyzes it
* Displays strength level

---

## 🛠️ Code Overview

* `check_strength()` → evaluates password strength
* Conditional statements → check different criteria
* String methods → detect letters, digits, symbols
* Length check → ensures minimum security requirement

---

# 🔐 OTP Generator

A simple Python program that generates secure One-Time Passwords (OTPs) for authentication and verification purposes.

---

## 📌 Features

* Generates random OTPs 🔢
* Supports numeric OTP generation
* Customizable OTP length
* Fast and lightweight program
* Beginner-friendly code

---

## 🧠 How It Works

* The program generates a random OTP
* It uses Python’s random module
* The OTP can contain:

  * Numbers
  * (Optional) letters and symbols or can be added in the future
* The generated OTP is displayed to the user

---

## 🎮 Usage

* Run the program
* Enter the desired OTP length (hardcoded, desired length is optional)
* The program generates an OTP
* Use the OTP for verification or testing purposes

---

## 🛠️ Code Overview

* `generate_otp()` → creates a random OTP
* Random module → generates secure random values
* Loops → build OTP of desired length
* String handling → combine characters into final OTP

---

# ✍️ Pangram Checker

A simple Python program that checks whether a sentence is a pangram or not.

---

## 📌 Features

* Detects pangram sentences 🔍
* Checks all alphabet letters from a-z
* Works with uppercase (optional) and lowercase letters
* Fast and lightweight program
* Beginner-friendly code

---

## 🧠 How It Works

* The user enters a sentence
* The program analyzes the text
* It checks whether the sentence contains:

  * All letters from a to z
* Based on the check, it determines if the sentence is a pangram

---

## 🎮 Usage

* Enter a sentence when prompted
* The program analyzes the sentence
* Displays whether it is a pangram or not

---

## 🛠️ Code Overview

* `check_pangram()` → verifies the sentence
* Loops → iterate through alphabet letters
* String methods → process and compare text
* Conditional statements → determine pangram status

---

# 🔐 Message Encoder

A simple Python program that encodes messages to make them secure and unreadable without decoding.

---

## 📌 Features

* Encodes secret messages 🔒
* Supports basic text encryption techniques
* Converts readable text into encoded format
* Simple and lightweight program
* Beginner-friendly code

---

## 🧠 How It Works

* The user enters a message
* The program processes the text
* It applies an encoding technique such as:

  * Character shifting
  * ASCII conversion
  * Custom encoding logic
* The encoded message is displayed to the user

---

## 🎮 Usage

* Enter a message when prompted
* The program encodes the message
* Displays the encoded output

---

## 🛠️ Code Overview

* `encode_message()` → converts text into encoded form
* Loops → process each character
* String methods → manipulate text data
* Conditional statements → apply encoding rules

---

## 🛠️ Technologies Used

* Python 3
* Built-in module:

  * `random`

---

## 🚀 Getting Started

### Prerequisites

* Python 3 installed on your system

### Installation & Run

1. Clone this repository:

```bash
git clone https://github.com/aneeshkumaryadav/PythonProjects.git
```

2. Navigate to the project folder:

```bash
cd PythonProjects/Projects
```

3. Run any file (example):

```bash
python DiceRolling.py
```

> Replace `DiceRolling.py` with any file you want to run.

---

## 📂 Project Structure

```
PythonProjects/
├── Projects/
│   ├── NumberGuessing.py
│   ├── RockPaperScissor.py
│   ├── DiceRolling.py
│   ├── PasswordGenerator.py
│   ├── PasswordValidator.py
│   ├── OTP_Generator.py
│   ├── PangramChecker.py
│   └── EncodeMessage.py
└── README.md
```

---

## 🎓 Learning Outcomes

After completing these projects, you will be able to:

* Understand basic Python programming concepts
* Use `random` module for simulations and game logic
* Work with loops to repeat actions and handle gameplay
* Apply conditional statements to make decisions
* Take and validate user input effectively
* Calculate basic probability using logic and iteration
* Understand combinations through dice simulations
* Build simple interactive command-line games 🎮
* Work with strings and character sets
* Generate secure random passwords 🔐
* Validate input using rules and conditions
* Design modular programs using functions
* Break problems into smaller reusable parts
* Improve problem-solving and logical thinking skills
* Build confidence in creating beginner-level projects
* Prepare for more advanced Python concepts and projects 🚀

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

* Fork the repository
* Create a new branch
* Submit a pull request

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 🙌 Acknowledgements

Inspired by beginner Python practice projects to build logic and problem-solving skills.

---

Happy Coding! 🚀
**Aneesh Kumar Yadav**
