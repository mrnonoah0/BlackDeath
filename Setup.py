try:
    import sys
    import os
    import time

    if sys.platform.startswith('win'):
        os.system('cls')
        print("Installing packages needed for Black death to run...")
        print("Upgrading pip...")
        os.system("python -m pip install --upgrade pip")
        print("Finished Upgrading pip...")
        print("Downloading packages from Requirements.txt")
        os.system("python -m pip install -r Requirements.txt")
        print("\033[92mFinished downloading\033[0m")
        time.sleep(1)
        os.system("python Main.py")
  
except Exception as e:
    input(e)