import os
import rpy2.robjects as ro

def get_emiten_list():
    '''
    Executes an R web scaper script
    '''
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
