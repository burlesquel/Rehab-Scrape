# Rehab-Scrape

Rehab-Scrape is a Python module that is used for scraping the Rehab.com and saving each companies' information in the CSV format.

Requirements:
*Python (with pip)
*Google Chrome version 99
*selenium, requests and bs4 modules of Python. You can use pip to install those modules. (run "pip install modulename" in a terminal)


Usage:
*main.py file is the main file that will be executed to run the script. After running it, the script will open a browser and will start to add companies with their information to "companies.csv" file.
*It takes around one sec for each company. This time will depend on many factors including computer's technical properties, internet speed etc.
*For every 1000 companies it scrapes, it creates a seperate CSV file and named it as "data1.csv, data2.csv..."
*chromedriver.exe must be in the same path with the main.py file.
