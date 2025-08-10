import os
import platform
import subprocess
import shutil
import sys

def install_packages():
    """Install required packages from requirements.txt."""
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '-r', 'requirements.txt'])

def copy_library(os_choice):
    """Copy the appropriate library.py file based on the OS choice."""
    if os_choice == 'win32':
        shutil.copy('linux/library.py', 'library.py')
    elif os_choice == 'linux':
        shutil.copy('linux/library.py', 'library.py')
    else:
        print("Invalid choice. Please choose either 'linux' or 'windows'.")
def importing_db():
    pass
def main():
    print("Welcome to the Library Management System Installer!")
    os_choice =  sys.platform

    # Install packages
    print("Installing required packages...")
    install_packages()

    # Copy the appropriate library file
    print(f"Copying library file for {os_choice}...")
    copy_library(os_choice)

    print("Installation complete! You can now run the library management system.")

if __name__ == "__main__":
    main()

