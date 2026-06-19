XO Game - Python Tic-Tac-Toe

A feature-rich Tic-Tac-Toe game built in Python with AI opponents, multiplayer support, user management, and persistent game history.
🎮 Features
Game Modes

    Single Player vs AI with 3 difficulty levels:

        Easy: Random moves

        Medium: Basic strategy with blocking

        Hard: Monte Carlo Tree Search (MCTS) implementation

    Two Player (1v1) local multiplayer

Core Features

    User Management: Create and manage player profiles

    Game History: View complete game histories with move-by-move replay

    Leaderboard: Track player statistics including wins, losses, ties, and win rates

    Settings: Customizable game options

    Auto-save: Automatically save game progress

    Undo/Replay: Undo moves or replay completed games

    Guest Mode: Play without creating a user profile

AI Intelligence

The AI uses three levels of sophistication:

    Easy: Random move selection

    Medium: Strategic blocking and winning moves

    Hard: Monte Carlo Tree Search algorithm for optimal play

🚀 Installation
Prerequisites

    Python 3.6 or higher

    pip (Python package manager)

Step 1: Clone the Repository
bash

git clone https://github.com/yourusername/xo-game.git
cd xo-game

Step 2: Install Dependencies
bash

pip install -r requirements.txt

Step 3: Run the Game
bash

python main.py

📁 Project Structure
text

xo-game/
├── main.py              # Main game file
├── requirements.txt     # Python dependencies
├── README.md           # This file
└── DB/                  # Database directory
    ├── users.txt        # User profiles
    ├── games.txt        # Game history
    ├── setting.txt      # Game settings
    └── instruction.txt  # Instructions text

🎯 How to Play
Starting the Game

    Run the game and you'll see the main menu

    Choose from options:

        New Game: Start a new match

        Users: Manage player profiles

        Leaderboard: View player rankings

        Game History: Review past games

        Settings: Customize game options

        Instruction: View game rules

        About Us: Credits

Game Controls

    Enter 1-9 to place your mark on the corresponding board position

    U to undo your last move (if enabled in settings)

    R to replay a move (if enabled in settings)

    B to go back to previous menu

Board Layout
text

 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9

⚙️ Settings
Available Settings

    Primary Mark: Choose X or O as your starting symbol

    Auto-save: Enable/disable automatic game saving

    Show Board Numbers: Toggle board position numbers

    Turn Duration: Set time limit for moves (15s, 20s, 25s, 30s)

    Undo & Replay: Enable/disable undo and replay features

    Reset Game: Clear all data and reset settings to default

📊 Statistics & Leaderboard

The leaderboard ranks players based on:

    Number of wins (primary)

    Win rate percentage

    Number of ties

    Total games played

Leaderboard Display

    🥇 Gold: 1st place

    🥈 Silver: 2nd place

    🥉 Bronze: 3rd place

💾 Data Storage

The game uses simple text files for data persistence:

    DB/users.txt: Stores player names (one per line)

    DB/games.txt: Stores game history with all moves and metadata

    DB/setting.txt: Stores game settings in key=value format

    DB/instruction.txt: Game rules and instructions

Game History Format
text

start_mark|winner_id|loser_id|sequence|timestamp|result

Where:

    sequence: Comma-separated list of moves

    result: 'T' for tie, empty for win/loss

🎨 Visual Design

    Colorful Terminal Output: Using the Colorama library for vibrant displays

    ASCII Art Banner: Welcome screen with "XO" in stylized text

    Intuitive UI: Clear menus with numbered options

🔧 Technical Details
Dependencies

    colorama: Cross-platform colored terminal text

    pyfiglet: ASCII art banner generation

    random: AI move selection and guest naming

    time: Timer functionality and timestamps

    os: System operations and file management

Key Classes

    page: Main menu and navigation controller

    fetch: Data management layer (CRUD operations)

    game: Game logic engine

🐛 Troubleshooting
Common Issues

Issue: ModuleNotFoundError: No module named 'colorama'
bash

Solution: pip install colorama

Issue: ModuleNotFoundError: No module named 'pyfiglet'
bash

Solution: pip install pyfiglet

Issue: Permission denied when writing to DB files
text

Solution: Ensure the DB directory has write permissions

Quick Fix

If you encounter any issues, try:
bash

pip install --upgrade colorama pyfiglet

🤝 Contributing

Contributions are welcome! Here's how you can help:

    Fork the repository

    Create a feature branch (git checkout -b feature/AmazingFeature)

    Commit your changes (git commit -m 'Add some AmazingFeature')

    Push to the branch (git push origin feature/AmazingFeature)

    Open a Pull Request

Areas for Improvement

    Add network multiplayer

    Implement more sophisticated AI algorithms

    Add sound effects

    Create GUI version

    Add tournament mode

    Add unit tests

    Implement database storage (SQLite)

📝 License

This project is open source and available under the MIT License.
👥 Arshia D.Sheibani

🙏 Acknowledgments

    Inspired by classic Tic-Tac-Toe games

    Built with love for Python programming

    Thanks to the open-source community

📞 Support

For questions or feedback:

    Open an issue on GitHub

    Contact: [arshiasheibani@gmail.com]

📋 Quick Start Commands
bash

# Clone the repository
git clone https://github.com/yourusername/xo-game.git

# Navigate to directory
cd xo-game

# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py

Enjoy the game! 🎮