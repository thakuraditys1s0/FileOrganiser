import os
import shutil
import threading
import time
import json
from tkinter import Tk, Button, Label, filedialog, messagebox

# File type categories
FILE_TYPES = {
    "Images": [".png", ".jpg", ".jpeg", ".gif", ".bmp", ".svg", ".webp"],
    "Videos": [".mp4", ".mkv", ".flv", ".avi", ".mov", ".wmv"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx", ".odt"],
    "Audio": [".mp3", ".wav", ".aac", ".flac", ".ogg"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Code": [".py", ".js", ".html", ".css", ".cpp", ".java", ".c", ".json"],
    "Executables": [".exe", ".msi", ".apk", ".bat", ".sh"],
    "Others": []
}

log_file = "organizer_log.json"
auto_thread = None
auto_running = False
selected_folder = None

def get_category(filename):
    ext = os.path.splitext(filename)[1].lower()
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    if not os.path.exists(folder_path):
        messagebox.showerror("Error", "The selected folder does not exist.")
        return

    log = []
    files_moved = 0

    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        if os.path.isfile(item_path):
            category = get_category(item)
            target_dir = os.path.join(folder_path, category)

            if not os.path.exists(target_dir):
                os.makedirs(target_dir)

            try:
                new_path = os.path.join(target_dir, item)
                shutil.move(item_path, new_path)
                log.append({"from": item_path, "to": new_path})
                files_moved += 1
            except Exception as e:
                print(f"Failed to move {item}: {e}")

    with open(log_file, "w") as f:
        json.dump(log, f, indent=2)

    messagebox.showinfo("Completed", f"Organized {files_moved} files into folders.")

def undo_last_operation():
    if not os.path.exists(log_file):
        messagebox.showwarning("Undo Failed", "No log file found.")
        return

    try:
        with open(log_file, "r") as f:
            log = json.load(f)

        for entry in reversed(log):
            if os.path.exists(entry["to"]):
                shutil.move(entry["to"], entry["from"])

        os.remove(log_file)
        messagebox.showinfo("Undo", "Successfully reverted last operation.")
    except Exception as e:
        messagebox.showerror("Error", f"Undo failed: {e}")

def auto_run():
    global auto_running
    while auto_running:
        organize_files(selected_folder)
        time.sleep(3600)  # 1 hour

def start_auto_run():
    global auto_running, auto_thread, selected_folder
    if not selected_folder:
        messagebox.showwarning("No Folder", "Please select a folder first.")
        return

    if auto_running:
        messagebox.showinfo("Already Running", "Auto-run is already active.")
        return

    auto_running = True
    auto_thread = threading.Thread(target=auto_run, daemon=True)
    auto_thread.start()
    messagebox.showinfo("Auto-Run Started", "Folder will be organized every hour.")

def stop_auto_run():
    global auto_running
    auto_running = False
    messagebox.showinfo("Stopped", "Auto-run has been stopped.")

def select_folder():
    global selected_folder
    selected_folder = filedialog.askdirectory(title="Select Folder to Organize")
    if selected_folder:
        folder_label.config(text=f"Selected: {selected_folder}")

# GUI Setup
root = Tk()
root.title("File Organizer")
root.geometry("400x300")
root.resizable(False, False)

Label(root, text="🗂 File Organizer", font=("Arial", 18, "bold")).pack(pady=10)
folder_label = Label(root, text="No folder selected", fg="gray")
folder_label.pack(pady=5)

Button(root, text="📂 Select Folder", command=select_folder, width=25).pack(pady=5)
Button(root, text="🚀 Organize Now", command=lambda: organize_files(selected_folder) if selected_folder else messagebox.showerror("Error", "No folder selected"), width=25).pack(pady=5)
Button(root, text="↩ Undo Last Operation", command=undo_last_operation, width=25).pack(pady=5)
Button(root, text="⏱ Start Auto-Run (Hourly)", command=start_auto_run, width=25).pack(pady=5)
Button(root, text="🛑 Stop Auto-Run", command=stop_auto_run, width=25).pack(pady=5)
Button(root, text="❌ Exit", command=root.destroy, width=25).pack(pady=15)

root.mainloop()