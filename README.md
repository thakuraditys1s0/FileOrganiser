# 🗂️ File Organizer GUI

A simple and intuitive desktop application built with Python that helps you automatically organize files in any selected folder by file type. Includes a **user-friendly GUI**, **Undo/Revert** functionality, and runs as a standalone `.exe` on Windows.

---

## 🧠 Features

- 📂 Automatically organizes files by extension (e.g., `.jpg`, `.pdf`, `.zip`)
- 🔙 One-click **Undo** to revert all changes
- 🕒 Automatically runs every hour (background task)
- 🖥️ GUI interface built with `tkinter`
- 🧪 Built into a standalone `.exe` — no Python required!

---

## 📸 Screenshot

> _Add a screenshot here once you capture one from the app's GUI_

---

## ⚙️ How to Use

### 🔧 Run from Python (source code)
```bash
python file_organizer_gui.py
```

### 📦 Run from compiled `.exe` (no Python needed)
Double-click:
```
dist/file_organizer_gui.exe
```

---

## 🔍 Folder Structure

```
FileOrganiser/
├── file_organizer_gui.py         # Main application (GUI + logic)
├── file_organizer_icon.ico       # Custom app icon
├── dist/                         # Contains final .exe after build
├── file_organizer_gui.spec       # PyInstaller build config
└── README.md                     # This file
```

---

## 🔨 Technologies Used

- Python 3.11+
- `tkinter` (GUI)
- `shutil`, `os`, `time`, `threading` (core logic)
- `PyInstaller` (for `.exe` packaging)
- `Pillow` (icon support in PyInstaller)

---

## ✨ Future Enhancements (Optional)

- 📁 Drag-and-drop folder selection
- 🌓 Dark mode toggle
- 🧠 File-type learning (organize by content, not just extension)
- 🌐 Cloud sync with Dropbox or Google Drive

---

## 👤 Author

**aD (thaku)**  
💼 Aspiring Developer & Data Analyst  
📍 India  
🧑‍💻 Project deployed using PyInstaller on Windows

---

## 📜 License

This project is licensed under the MIT License — use it freely!