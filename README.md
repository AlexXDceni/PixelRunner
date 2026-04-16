# Pixel Runner

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python">
  <img src="https://img.shields.io/badge/Pygame-2.0+-green.svg" alt="Pygame">
  <img src="https://img.shields.io/badge/Status-Complete-brightgreen.svg" alt="Status">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Genre-Endless%20Runner-purple" alt="Genre">
  <img src="https://img.shields.io/badge/Theme-Pixel%20Art-orange" alt="Theme">
</p>

> 🏃‍♂️ An exciting 2D side-scrolling endless runner game! Dodge obstacles, survive as long as you can, and beat your high score!

---

## 🎮 Game Preview

```
    ╔═══════════════════════════════════════════════════════════╗
    ║                                                           ║
    ║   PIXEL RUNNER                        ⭐ HIGH: 125        ║
    ║                                                           ║
    ║                                                           ║
    ║       🦇                          🐌                     ║
    ║   ════════════════════════════════════════════════════    ║
    ║       🧍                                                  ║
    ║   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ║
    ║                                                           ║
    ║   SCORE: 42                              ⏸️ [ESC] Pause   ║
    ╚═══════════════════════════════════════════════════════════╝
```

---

## ✨ Features

### 🎯 Core Gameplay
- **Endless Runner** - Survive as long as possible!
- **Progressive Difficulty** - Game gets faster the longer you play
- **Persistent High Scores** - Your best score is saved locally
- **Two Types of Enemies** - Bats (flying) and Snails (ground)

### 🎨 Visual Design
- **Pixel Art Style** - Nostalgic retro graphics
- **Smooth Animations** - Character flips based on movement direction
- **Dynamic Background** - Atmospheric game world

### 🔊 Audio
- **Background Music** - Immersive gameplay soundtrack
- **Jump Sound Effects** - Satisfying audio feedback

### 🕹️ Controls
| Action | Keys |
|--------|------|
| **Jump** | `SPACE` or `W` |
| **Move Left** | `A` or `←` |
| **Move Right** | `D` or `→` |
| **Pause** | `ESC` |

---

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/AlexXDceni/PixelRunner.git
cd PixelRunner
```

2. **Install dependencies**
```bash
pip install pygame
```

3. **Run the game**
```bash
python main.py
```

---

## 🎮 How to Play

### Game States

#### 1. 🏠 Start Menu
- View your current high score
- Press `SPACE` to start the game
- Access settings from the menu

#### 2. ▶️ Gameplay
- Your knight runs automatically
- **Jump** over ground obstacles
- **Move left/right** to dodge enemies
- Avoid collisions at all costs!
- Watch the difficulty increase over time

#### 3. ⏸️ Paused
- Game freezes when you press `ESC`
- Press `ESC` again to resume

#### 4. 💀 Game Over
- Displayed when you hit an enemy
- Shows your final score
- Option to restart and try again

---

## 🏆 Scoring System

| Time Survived | Score |
|---------------|-------|
| 1 second | +1 point |
| Difficulty increases over time |
| Bats and snails move faster as you progress |

### High Score
- Automatically saved to `save_file.txt`
- Persists between game sessions
- Displayed on the start menu

---

## 🐛 Enemies

### Bat 🦇
- Flies at mid-air height
- Faster than snails
- Requires precise jumping to avoid

### Snail 🐌
- Moves along the ground
- More common spawn rate (3x more frequent than bats)
- Jump to avoid!

---

## 📁 Project Structure

```
PixelRunner/
├── main.py              # 🎮 Main game loop and event handling
├── config.py            # ⚙️  Game constants and configuration
├── textures.py          # 🎨 All visual assets and UI elements
├── game_states.py       # 🔄 Game state management
├── player_sprite.py    # 🧍 Player character class
├── enemy_sprite.py     # 🐛 Enemy classes and spawning
├── sources/             # 📦 Game assets
│   ├── images/         # 🖼️  Sprite images
│   ├── music/          # 🎵 Background music
│   └── sounds/         # 🔊 Sound effects
├── save_file.txt       # 💾 High score storage
├── README.md           # 📖 This file
└── requirements.txt    # 📦 Dependencies
```

---

## 🛠️ Technical Details

| Property | Value |
|----------|-------|
| **Engine** | Pygame |
| **Resolution** | 800 x 400 pixels |
| **Frame Rate** | 60 FPS |
| **Language** | Python 3.8+ |
| **Genre** | Endless Runner |
| **Art Style** | Pixel Art |

### Physics
- **Gravity**: Constant downward acceleration
- **Jump Force**: -20 vertical velocity
- **Movement Speed**: 5 pixels per frame
- **Speed Increase**: +0.005 per frame

---

## 🎨 Screenshots

### Start Menu
```
┌─────────────────────────────────────┐
│                                     │
│         ████  PIXEL RUNNER  ████    │
│                                     │
│              HIGH: 125              │
│                                     │
│        [⚙️ Settings]                │
│                                     │
│     Press SPACE to Start            │
│                                     │
│   SPACE: Jump | A/D: Move | ESC:    │
│                                     │
└─────────────────────────────────────┘
```

### Gameplay
```
┌─────────────────────────────────────┐
│  SCORE: 42        ⭐ HIGH: 125      │
│                                     │
│       🦇                            │
│                                     │
│    🧍        🐌                    │
│   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     │
└─────────────────────────────────────┘
```

---

## 🔮 Future Features

- [ ] More enemy types
- [ ] Power-ups and collectibles
- [ ] Multiple levels/environments
- [ ] Leaderboard system
- [ ] Custom character skins
- [ ] Mobile touch controls

---

## 🤝 Contributing

Contributions are welcome! Feel free to:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🙏 Acknowledgments

- Built with [Pygame](https://www.pygame.org/)
- Pixel art assets inspired by classic 8-bit games
- Background music creates an immersive experience

---

<p align="center">
  Made with ❤️ by <a href="https://github.com/AlexXDceni">AlexXDceni</a>
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Thank%20You-Playing-blue" alt="Thank You">
</p>
