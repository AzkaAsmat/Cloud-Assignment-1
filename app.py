
"""
THIS CODE FILE CONTAINS THE CODE FOR MAIN APP OF THE WEB STORAGE APP.

THIS FILE DEFINES A main() FUNCTION THAT WILL BE EXECUTED WHEN THE APP RUNS. INSIDE THIS FUNTION ALL THE OTHER MENU TABS OF THE APP IS CALLED.
"""
import subprocess

# Define the list of packages to install
packages = ["matplotlib", "mysql-connector-python", "sqlalchemy"]

# Use pip to install each package
for package in packages:
    try:
        subprocess.check_call(["pip", "install", package])
        print(f"{package} has been successfully installed.")
    except subprocess.CalledProcessError:
        print(f"Error: Failed to install {package}.")

from dependancies import *
from home import *
from login import *

from about import *


def main():
    # st.set_page_config(
    #     page_title="Cloud Based Web Storage App",
    #     page_icon="home",
    #     layout="wide",
    # )

    st.title("Cloud Based Web Storage App")


    st.sidebar.title("Menu")
    app_mode = st.sidebar.selectbox('Get Started:', ['User', 'Home',  'About'])

    if app_mode == 'User':
        login()
        

    elif app_mode == 'About':
        about()
        
        
    #else:
     #   home()

if __name__ == "__main__":
    try:
        main()
    except SystemError:
        pass
