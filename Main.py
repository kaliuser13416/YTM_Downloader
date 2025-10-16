import os
import logging
import pandas
from pytubefix import YouTube

# logger set up
logging.basicConfig(
    level=logging.ERROR,
    format='%(asctime)s %(levelname)s: %(message)s',
    handlers=[
        logging.FileHandler('main.log'), logging.StreamHandler()
    ]
)

def Download_Music(url_list, playlist_name):
    print(f'Starting Downloads')
    # These variables are used to calculate download stats
    downloaded = 0
    unavailable = 0
    if os.path.isdir(playlist_name) == False:
        os.makedirs(playlist_name)
    for url in url_list:
        try:
            music = YouTube(url).streams.filter(only_audio=True).first()
            music.download(playlist_name)
            print(f'Downloaded URL: {url}')
            downloaded = downloaded + 1;
        except Exception as e:
            if ("is unavailable" in str(e)) or ("not available" in str(e) or (str(e) == "YouTube.vid_info_client.<locals>.call_innertube() missing 1 required positional argument: 'optional_client'")):
                logging.error(f'Song is unavailable: {url}')
                unavailable = unavailable + 1
            else:
                logging.error(f'Failed to download URL {url}: {e}')
    print(f'Downloaded {downloaded} out of {len(url_list)}')
    print(f'{unavailable} out of {len(url_list)} were unavailable')
    print(f'Downloaded {100*(downloaded / (len(url_list) - unavailable))}% of available URLs')

def Get_URLs():
    for file in file_list:
        playlist_name = os.path.splitext(os.path.basename(file))[0]
        url_list = []
        try:
            csvFile = pandas.read_csv(file)
            print(f'Loaded: {file}')
            for index, row in csvFile.iterrows():
                vid_id = row['Video ID']
                if vid_id != []:
                    temp = vid_id
                    temp = temp.replace(' ', '')    # This is needed because some video IDs have a space.
                    temp_url = f"https://www.youtube.com/watch?v={temp}"
                    url_list.append(temp_url)
            url_list = list(set(url_list))  # Gets rid of duplicate song URLs
            Download_Music(url_list, playlist_name)
        except(Exception) as e:
            logging.error(f'failed to open / load file {file}: {e}')

if __name__ == '__main__':
    # This looks for all of the CSV files in the current directory and puts them in the 'file_list' list.
    file_list = []
    for file in os.listdir():
        if file.endswith(".csv"):
            print(f'found csv: {file}')
            file_list.append(file)
    Get_URLs()
