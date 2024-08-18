import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os
import cv2
import threading

# Global variable to control the processing
processing = True

def update_progress(current_frame, total_frames):
    progress['value'] = (current_frame / total_frames) * 100
    root.update_idletasks()

def format_timestamp(frame_time):
    seconds = int(frame_time)
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return f"{hours:02d}h{minutes:02d}m{seconds:02d}s"

def video_to_images(video_path, output_folder, frame_interval, name_format):
    global processing
    cap = cv2.VideoCapture(video_path)
    
    if not cap.isOpened():
        messagebox.showerror("Error", "Error opening video file")
        return
    
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    frame_number = 0
    os.makedirs(output_folder, exist_ok=True)
    
    while True:
        if not processing:
            break
        
        ret, frame = cap.read()
        
        if not ret:
            break
        
        if frame_number % frame_interval == 0:
            timestamp = format_timestamp(cap.get(cv2.CAP_PROP_POS_MSEC) / 1000)
            if name_format == "sequential":
                frame_filename = os.path.join(output_folder, f"frame_{frame_number:04d}.jpg")
            elif name_format == "timestamp":
                frame_filename = os.path.join(output_folder, f"frame_{timestamp}.jpg")
            elif name_format == "custom":
                prefix = custom_prefix_var.get()
                frame_filename = os.path.join(output_folder, f"{prefix}_{frame_number:04d}.jpg")
            elif name_format == "sequential_timestamp":
                frame_filename = os.path.join(output_folder, f"frame_{frame_number:04d}_{timestamp}.jpg")
            else:
                frame_filename = os.path.join(output_folder, f"frame_{frame_number:04d}.jpg")

            cv2.imwrite(frame_filename, frame)
        
        frame_number += 1
        update_progress(frame_number, total_frames)
    
    cap.release()
    messagebox.showinfo("Success", f"Done! Extracted frames at interval of {frame_interval}.")
    progress['value'] = 0

def select_video():
    file_path = filedialog.askopenfilename(
        title="Select Video File", 
        filetypes=[("Video Files", "*.mp4 *.avi *.mov *.mkv")]
    )
    video_path_var.set(file_path)

def select_output_folder():
    folder_path = filedialog.askdirectory(title="Select Output Folder")
    output_folder_var.set(folder_path)

def start_conversion():
    global processing
    processing = True
    
    video_path = video_path_var.get()
    output_folder = output_folder_var.get()
    frame_interval = frame_interval_var.get()
    name_format = name_format_var.get()
    
    if not video_path or not output_folder:
        messagebox.showwarning("Input Required", "Please select both a video file and an output folder.")
        return
    
    if frame_interval <= 0:
        messagebox.showwarning("Input Error", "Frame interval must be a positive integer.")
        return

    # Run video processing in a separate thread to keep the GUI responsive
    processing_thread = threading.Thread(
        target=video_to_images,
        args=(video_path, output_folder, frame_interval, name_format)
    )
    processing_thread.start()

def stop_conversion():
    global processing
    processing = False

# Initialize Tkinter window
root = tk.Tk()
root.title("Simple Video Frame Ripper")

# Variables to hold paths and frame interval
video_path_var = tk.StringVar()
output_folder_var = tk.StringVar()
frame_interval_var = tk.IntVar(value=1)  # Default to every frame
name_format_var = tk.StringVar(value="sequential")  # Default naming format
custom_prefix_var = tk.StringVar(value="prefix")  # Default prefix

# Create GUI elements
tk.Label(root, text="Select Video File:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=video_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_video).grid(row=0, column=2, padx=10, pady=10)

tk.Label(root, text="Select Output Folder:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=output_folder_var, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(root, text="Browse", command=select_output_folder).grid(row=1, column=2, padx=10, pady=10)

tk.Label(root, text="Frame Interval:").grid(row=2, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=frame_interval_var, width=10).grid(row=2, column=1, padx=10, pady=10)

# Naming options
tk.Label(root, text="Naming Format:").grid(row=3, column=0, padx=10, pady=10)
tk.OptionMenu(root, name_format_var, "sequential", "timestamp", "custom", "sequential_timestamp").grid(row=3, column=1, padx=10, pady=10)

# Custom prefix entry
tk.Label(root, text="Custom Prefix:").grid(row=4, column=0, padx=10, pady=10)
tk.Entry(root, textvariable=custom_prefix_var, width=20).grid(row=4, column=1, padx=10, pady=10)

# Progress bar
progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.grid(row=5, column=1, pady=10)

tk.Button(root, text="Convert", command=start_conversion, width=20).grid(row=6, column=0, pady=20, padx=10)
tk.Button(root, text="Stop", command=stop_conversion, width=20).grid(row=6, column=2, pady=20, padx=10)

# Run the application
root.mainloop()
