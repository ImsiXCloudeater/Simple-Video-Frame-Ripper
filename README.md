Video Frame Ripper
Overview
The Video Frame Ripper application allows you to extract frames from video files at specified intervals and save them as images. The application provides options for naming the output frames and includes a progress bar to monitor the extraction process.

Features
Select Video File: Choose a video file from your computer.
Select Output Folder: Specify the folder where extracted frames will be saved.
Frame Interval: Define the interval at which frames are extracted.
Naming Formats: Choose from various naming formats for output files.
Progress Bar: View the progress of frame extraction.
Stop Button: Cancel the extraction process if needed.
Requirements
Python 3.x
tkinter
opencv-python
ttkthemes
pillow
Installation
Running the Installer
Run the Installer: Execute the install_py.py script to install all necessary dependencies.

bash
Copy code
python install_py.py
Launch the Application: After installation, run the vfr.pyw script to start the application.

bash
Copy code
python program/vfr.pyw
Manual Installation (if needed)
If you prefer to manually install dependencies, you can use the following commands:

bash
Copy code
pip install opencv-python
pip install ttkthemes
pip install pillow
Usage
Open the Application: Run vfr.pyw to launch the application.
Select Video File: Click on the "Browse" button next to "Select Video File" to choose your video.
Select Output Folder: Click on the "Browse" button next to "Select Output Folder" to choose where to save the frames.
Set Frame Interval: Enter the interval at which frames should be extracted.
Choose Naming Format: Select your preferred naming format for the output images.
Start Conversion: Click "Convert" to begin extracting frames. Use the "Stop" button to halt the process if necessary.
Troubleshooting
Missing Dependencies: If you encounter missing module errors, ensure all required packages are installed. Run install_py.py to automatically install them.
Application Issues: If the application does not start or crashes, check the installation of dependencies and ensure you are using a compatible Python version.
