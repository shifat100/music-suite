# xyz-music-suite
# 🎵 KaiTune Pro — KaiOS Music & Ringtone Suite

![KaiOS](https://img.shields.io/badge/Platform-KaiOS%202.5%20%7C%203.0-00d2ff)
![License](https://img.shields.io/badge/License-MIT-green)
![Web Audio API](https://img.shields.io/badge/Engine-Web%20Audio%20API-blueviolet)

**KaiTune Pro** is an open-source, hardware-optimized music player, ringtone cutter, and audio equalizer designed specifically for KaiOS and Smart Feature Phones.

---

## ✨ Features
- 🎧 **Web Audio Engine:** Real-time spectrum visualizer with 3 themes (Cyan, Fire, Emerald).
- 🎚️ **3-Band Equalizer & FX:** Bass Boost, Treble adjustment, and 0.75x–2.0x playback speed.
- ✂️ **Precision Ringtone Cutter:** Real-time red playhead, `*` (Start) & `#` (End) key markers, clip preview, and direct WAV export.
- 📑 **Queue & Playlists:** "Play Next" queue management and custom Favorites storage.
- 🖼️ **KaiOS Storage Wallpapers:** Set background image directly from device storage or gallery via `DeviceStorage` / `MozActivity`.
- 🕹️ **D-Pad & Keypad Compliance:** Full hardware navigation with context-aware J2ME-style Options menus.

---

## ⌨️ Keypad Controls

| Key | Action |
| :--- | :--- |
| **SoftLeft / Escape / F1** | Open Context Options Menu |
| **Center / Enter** | Play / Pause / Select / Open |
| **SoftRight / F2 / Backspace** | Back / Close Menu / Exit |
| **[ 1 ]** | Focus Search Bar |
| **[ 2 ]** | Toggle Shuffle Mode (ON/OFF) |
| **[ 3 ]** | Toggle Repeat Mode (ALL/ONE/OFF) |
| **[ 4 ]** | Save/Download Current Track |
| **[ 5 ]** | Add Focused Track to Queue (Play Next) |
| **[ * ]** | Set Start Point on Cutter Timeline |
| **[ # ]** | Set End Point on Cutter Timeline |
| **Left / Right** | 5s Seek (Player) / 2s Seek (Cutter) |

---

## 🚀 How to Install on KaiOS

1. **Via WebIDE / GerdaOS / OmniSD:**
   - Clone or download this repository as a `.zip` file.
   - Connect your KaiOS phone via USB and enable debugging (`*#*#33284#*#*`).
   - Open WebIDE in Firefox / Pale Moon, select the folder, and click **Install and Run**.

2. **Web Browser / Desktop Testing:**
   - Simply open `index.html` in any modern web browser or KaiOS simulator.

---

## 📄 License
This project is licensed under the [MIT License](LICENSE).
