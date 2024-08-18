import subprocess
import sys

def install_dependencies():
    # List of dependencies to be installed
    dependencies = [
        'opencv-python',
        'ttkthemes'
        # Add any other required packages here
    ]
    
    for package in dependencies:
        try:
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package])
        except subprocess.CalledProcessError:
            print(f"Failed to install {package}")
            sys.exit(1)  # Exit if any package fails to install

if __name__ == "__main__":
    install_dependencies()
