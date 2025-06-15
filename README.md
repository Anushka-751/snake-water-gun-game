# 🐍 Snake-Water-Gun Game (Python)

This is a simple command-line based game written in Python that simulates the classic **Snake-Water-Gun** game — a fun alternative to Rock-Paper-Scissors. The user plays against the computer by choosing one of the three options.

## 🎮 How to Play

- **s** = Snake  
- **w** = Water  
- **g** = Gun

The rules:
- Snake drinks water → Snake wins  
- Gun shoots snake → Gun wins  
- Water douses gun → Water wins

## 🧠 Logic Mapping

| User Choice | Computer Choice | Result     |
|-------------|------------------|------------|
| s           | w                | Win        |
| w           | g                | Win        |
| g           | s                | Win        |
| w           | s                | Lose       |
| g           | w                | Lose       |
| s           | g                | Lose       |
| Same        | Same             | Draw       |

## 💻 Code Overview

```python
import random

computer = random.choice([-1, 0, 1])
youstring = input("Enter your choice (s for Snake, w for Water, g for Gun): ")
youdict = {"s": 1, "w": -1, "g": 0}
reversedict = {1: "s", -1: "w", 0: "g"}

you = youdict[youstring]

print(f"You chose: {reversedict[you]} \nComputer chose: {reversedict[computer]}")

if computer == you:
    print("Draw")
else:
    if computer == -1 and you == 1:
        print("You win!")
    elif computer == -1 and you == 0:
        print("You win!")
    elif computer == 1 and you == -1:
        print("You lose!")
    elif computer == 1 and you == 0:
        print("You win!")
    elif computer == 0 and you == -1:
        print("You win!")
    elif computer == 0 and you == 1:
        print("You win!")
    else:
        print("Something went wrong")
