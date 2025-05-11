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
