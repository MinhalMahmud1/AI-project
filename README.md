# 🧠 AI-Powered Halma with Strategic AI

## 🎮 Project Overview
This project is a Python-based implementation of the board game **Halma**, enhanced with an intelligent AI opponent. The AI uses the **Minimax algorithm with Alpha-Beta Pruning** and a custom **heuristic evaluation function** to make strategic moves. The game features a graphical interface built using **Pygame**, enabling human players to challenge a smart and adaptive AI in real time.

## 🚀 Features
- **Minimax with Alpha-Beta Pruning** for efficient decision-making.
- **Heuristic evaluation** based on:
  - Distance to target zone
  - Board control and blocking
  - Piece activity (penalizes idle pieces)
- Interactive **Pygame GUI**
- Configurable AI difficulty by adjusting the search depth
- Smooth turn handling and win condition logic

## 🧠 AI Strategy
The AI evaluates moves using a custom heuristic:
- **Proximity to goal**: Rewards progress toward the opponent’s starting zone.
- **Zone control**: Prefers blocking enemy paths.
- **Piece activity**: Penalizes stagnant pieces.

## 🛠 How to Run

### ✅ Requirements
- Python 3.x
- Pygame library

### 🔧 Installation
Install Pygame using pip:

```bash
pip install pygame

▶️ Run the Game
python main.py

🎥 Demo Video:
📽️ Click here to watch the 2-minute demo video

📄 Project Report:
📝 Click here to view the full project report (PDF)

🧑‍🤝‍🧑 Team Members
Muhammad Minhal Mahmud (K21-3618)
Huzaifa Farraz (K21-3602)
Muhammad Abbas (K21-3592)
Arham Asher (K21-3578)

📚 References:
Russell, S., & Norvig, P. Artificial Intelligence: A Modern Approach
Pygame Documentation
Online Halma rules and strategy guides
Academic research on Minimax and Alpha-Beta Pruning (IEEE & journals)
