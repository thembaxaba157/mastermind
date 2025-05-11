# 🔐 Mastermind – Codebreaker Game in Python

A terminal-based Mastermind-style number guessing game. The player has 12 chances to guess a **4-digit secret code** with unique digits (1–8). After each guess, the program gives feedback on digits guessed correctly and their positions.

---

## 🧠 How It Works

- The game generates a **random 4-digit code** made up of non-repeating digits from 1 to 8.
- You have **12 attempts** to guess the code.
- After each guess, the program tells you:
  - How many digits are correct **and** in the correct position
  - How many digits are correct but in the **wrong** position

This follows the logic of the classic **Mastermind** game — but with numbers instead of colored pegs.

---

## 🎮 Example Gameplay

```
4-digit Code has been set. Digits in range 1 to 8. You have 12 turns to break it.
Input 4 digit code: 1234
Number of correct digits in correct place:     1
Number of correct digits not in correct place: 2
Turns left: 11
Input 4 digit code: 1586
Number of correct digits in correct place:     2
Number of correct digits not in correct place: 0
Turns left: 10
...
Congratulations! You are a codebreaker!
The code was: [1, 5, 8, 6]
```

---

## 📁 Project Structure

```text
mastermind/
├── mastermind.py         # Main game script
├── tests/
│   └── test_main.py      # Unit tests for core functions
└── README.md             # Project documentation
```

---

## ▶️ How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/thembaxaba157/mastermind.git
   cd mastermind
   ```

2. Run the game:
   ```bash
   python3 mastermind.py
   ```

3. Follow the prompts in the terminal to play.

---

## 🧪 How to Test

To run all unit tests:
```bash
python3 -m unittest tests/test_main.py
```

---

## 🧩 Features

- Randomized 4-digit code with unique digits (1–8)
- Validates player input (must be 4 digits)
- Clear turn-by-turn feedback
- Win condition and code reveal
- Clean CLI interface
- Easy to test and extend

---

## 📜 License

MIT License — feel free to use, modify, or fork for fun or learning.

---

## 👨‍💻 Author

Built by [@thembaxaba157](https://github.com/thembaxaba157)

---

⭐️ *Star this repo if you like classic logic games reimagined in Python!*
