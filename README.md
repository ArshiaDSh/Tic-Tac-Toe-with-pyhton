# 🎮 Tic Tac Toe

A feature-rich Tic-Tac-Toe game built in Python with AI opponents, multiplayer support, user management, and persistent game history.

---

## ✨ Features

### 🎯 Game Modes

- **🤖 Single Player vs AI** with 3 difficulty levels:
  - 🟢 Easy: Random moves
  - 🟡 Medium: Basic strategy with blocking
  - 🔴 Hard: Monte Carlo Tree Search (MCTS) implementation
- **👥 Two Player (1v1)** local multiplayer

### 🛠️ Core Features

- 👤 User Management - Create and manage player profiles
- 📜 Game History - View complete game histories with move-by-move replay
- 🏆 Leaderboard - Track player statistics including wins, losses, ties, and win rates
- ⚙️ Settings - Customizable game options
- 💾 Auto-save - Automatically save game progress
- ↩️ Undo/Replay - Undo moves or replay completed games
- 🎭 Guest Mode - Play without creating a user profile

---

## 🚀 Installation

### 📋 Prerequisites

- Python 3.6 or higher
- pip (Python package manager)

### 📝 Steps

1. Clone the repository
```bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the game
```bash
python main.py
```

---

## 📁 Project Structure

```
tic-tac-toe/
├── main.py              # Main game file
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── DB/                  # Database directory
    ├── users.txt        # User profiles
    ├── games.txt        # Game history
    ├── setting.txt      # Game settings
    └── instruction.txt  # Instructions text
```

---

## 🎯 How to Play

### 📋 Main Menu Options

1. 🆕 New Game - Start a new match
2. 👥 Users - Manage player profiles
3. 🏆 Leaderboard - View player rankings
4. 📜 Game History - Review past games
5. ⚙️ Settings - Customize game options
6. 📖 Instruction - View game rules
7. ℹ️ About Us - Credits
8. 🚪 Exit - Quit the game

### 🎮 Controls

- Enter **1-9** to place your mark on the corresponding board position
- Press **U** to undo your last move (if enabled in settings)
- Press **R** to replay a move (if enabled in settings)
- Press **B** to go back to previous menu

### 📊 Board Layout

```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

---

## ⚙️ Settings

| Setting | Options | Description |
|---------|---------|-------------|
| Primary Mark | ❌, ⭕ | Choose your starting symbol |
| Auto-save | On, Off | Automatically save game progress |
| Show Board Numbers | On, Off | Display position numbers on board |
| Turn Duration | 15s, 20s, 25s, 30s | Time limit per move |
| Undo & Replay | On, Off | Enable undo and replay features |
| Reset Game | - | Clear all data and reset settings |

---

## 🏆 Leaderboard

Players are ranked based on:
1. Number of wins (primary)
2. Win rate percentage
3. Number of ties
4. Total games played

Rankings:
- 🥇 1st place: Gold
- 🥈 2nd place: Silver
- 🥉 3rd place: Bronze

---

## 💾 Data Storage

The game uses text files for data persistence:

| File | Purpose |
|------|---------|
| DB/users.txt | Stores player names |
| DB/games.txt | Stores game history with all moves |
| DB/setting.txt | Stores game settings |
| DB/instruction.txt | Game rules and instructions |

### Game History Format

```
start_mark|winner_id|loser_id|sequence|timestamp|result
```

- sequence: Comma-separated list of moves
- result: 'T' for tie, empty for win/loss

---

## 🛠️ Technical Details

### 📦 Dependencies

- colorama - Cross-platform colored terminal text
- pyfiglet - ASCII art banner generation
- random - AI move selection and guest naming
- time - Timer functionality and timestamps
- os - System operations and file management

### 🔑 Key Classes

- page - Main menu and navigation controller
- fetch - Data management layer (CRUD operations)
- game - Game logic engine

---

## 🐛 Troubleshooting

### Common Issues

**ModuleNotFoundError: No module named 'colorama'**
```bash
pip install colorama
```

**ModuleNotFoundError: No module named 'pyfiglet'**
```bash
pip install pyfiglet
```

**Permission denied when writing to DB files**
```
Ensure the DB directory has write permissions
```

---

## 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

### Areas for Improvement

- 🌐 Add network multiplayer
- 🧠 Implement more sophisticated AI algorithms
- 🔊 Add sound effects
- 🖥️ Create GUI version
- 🏆 Add tournament mode
- ✅ Add unit tests
- 🗄️ Implement database storage (SQLite)

---

## 📝 License

This project is open source and available under the MIT License.

---

## 👥 Authors

Arshia D.sheibani - [GitHub](https://github.com/arshiadsh)

---

## 🙏 Acknowledgments

- Inspired by classic Tic-Tac-Toe games
- Built with ❤️ using Python
- Thanks to the open-source community

---

## 📞 Support

- Open an issue on GitHub
- Contact: arshiasheibani@gmail.com

---

## ⚡ Quick Start

```bash
git clone https://github.com/yourusername/tic-tac-toe.git
cd tic-tac-toe
pip install -r requirements.txt
python main.py
```

---

## 📄 Requirements

```
colorama
pyfiglet>=1.0.4
```

---

**Enjoy the game! 🎮**