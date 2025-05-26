import os
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
import sys

def get_emiten_list():
    '''
    Executes an R web scaper script
    '''
    try:
        ip = get_ipython()
        if ip is not None:
            ip.run_line_magic('load_ext', 'rpy2.ipython')
            print("rpy2 IPython extension loaded.")
        else:
            print("Not in IPython environment. Skipping %load_ext.")
    except NameError:
        print("Not in IPython environment. Skipping %load_ext.")
        print("Ensure rpy2 is installed (`pip install rpy2`) if running standalone.")

    scraper_path = "/content/Portfolio-Tracker/data/utils/get_emiten.R"
    if os.path.exists(scraper_path): 
        print(f"Attempting to source R script: '{scraper_path}'...")
        try:
            ro.r(f"source('{scraper_path}')")
            print(f"R script '{scraper_path}' sourced successfully!")
        except Exception as e:
            print(f"Error sourcing R script '{scraper_path}': {e}")
    else:
        print(f"Error: The file '{scraper_path}' DOES NOT exist at the specified path.") 
