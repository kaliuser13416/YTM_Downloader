# YTM_Downloader
A Python script that imports export data from YouTube Music and downloads the songs. This script is specifically made for the CSV files from a 'Google TakeOut'. All of the songs that couldn't downloaded are logged. After all the songs are downloaded, they are moved to a sub-directory called 'music'.

## Setup
Download Main.py, install the requirements with pip3, move the CSV files from the Google Takeout to the same directory, then run Main.py.

## Requirements
Pyhton 3.10+
- os
- pandas
- pytubefix

## Google Takeout
- Step 1, Visit https://myaccount.google.com/dashboard
- Step 2, Under the YouTube section, hit download. By defualt all your YouTube data will be selected
- Step 3, De-select all non-relvent data
- Step 4, Hit next step. Set up a destination, by defualt it will send you download links via email. Then hit 'create export'
- Step 5, Wait. This will usually take less than a day
- Step 6, Download & extract the CSV files then move them into the same directory as Main.py then run Main.py

## Disclaimer
Copyright infringement is a crime under the Digital Millennium Copyright Act of 1998. This tool should only be used to download public domain, creative commons, and or non-copyright content.
