import os
import sys
import pandas
import logging
from pytubefix import YouTube

def move_music():
    base = os.getcwd()
    true_Dest = os.path.join(base, destination)
    
    if os.path.isdir(true_Dest) == False:
        os.makedirs(true_Dest)
    
    logging.info(f"Started moving all music to '{true_Dest}'")
    for file in os.listdir():
        if file.endswith(".m4a"):
            sorce_path = os.path.join(base, file)
            destination_path = os.path.join(true_Dest, file)
            try:
                os.rename(sorce_path, destination_path)
            except Exception as e:
                logging.error(f'Failed to move song {file}: {e}')
    logging.info(f"Finshed moving all music to '{true_Dest}'")

def main(url_list):
    logging.info(f'Starting Downloads')
    # These variables are used to calculate download stats
    downloaded = 0
    unavailable = 0
        
    for url in url_list:
        try:
            music = YouTube(url).streams.filter(only_audio=True).first()
            music.download()
            downloaded = downloaded + 1;
        except Exception as e:
             logging.error(f'Download failed: {e}')
             str_err = str(e)   # This is needed because 'e' has non str class
             if "is unavailable" in str_err:
                unavailable = unavailable + 1
    logging.info(f'Downloaded {downloaded} out of {len(url_list)}')
    logging.info(f'{unavailable} out of {len(url_list)} were unavailable')
    logging.info(f'Downloaded {100*(downloaded / (len(url_list) - unavailable))}% of available URLs')
    
    move_music()
    
def load_YT_dump(url_list):
    for file in file_list:
        try:
            csvFile = pandas.read_csv(file)
            logging.info(f'Loaded: {file}')
            for index, row in csvFile.iterrows():
                vid_id = row['Video ID']
                if vid_id != []:
                    temp = vid_id
                    temp = temp.replace(' ', '')    # This is needed because some video IDs have a space.
                    temp_url = f"https://www.youtube.com/watch?v={temp}"
                    url_list.append(temp_url)
        except(Exception) as e:
            logging.error(f'failed to open / load file: {e}')
    
    url_list = list(set(url_list))  # Gets rid of duplicate song URLs
    main(url_list)

if __name__ == '__main__':
    # This sets up the logger
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s: %(message)s',
        handlers=[
            logging.FileHandler('main.log'), logging.StreamHandler()
        ]
    )
    
    # This looks for all of the CSV files in the current directory and puts them in 'file_list' list.
    file_list = []
    for file in os.listdir():
        if file.endswith(".csv"):
            logging.info(f'found csv: {file}')
            file_list.append(file)
    
    url_list = []
    
    destination = 'music'   # The diectory where all the music files get moved to
    load_YT_dump(url_list)
