import json
import subprocess
import os
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--downloaded_file',type=str,default='downloaded_videos.txt')
parser.add_argument('--todo_file',type=str,default='channel_info.json')
args = parser.parse_args()
with open(args.todo_file, 'r') as file:
    data = json.load(file)

video_urls = [video['url'] for video in data['data']]

downloaded_urls = set()
if os.path.exists(args.downloaded_file):
    with open(args.downloaded_file, 'r') as file:
        downloaded_urls = set(file.read().splitlines())

for url in video_urls:
    if url not in downloaded_urls:
        subprocess.call(['youtube-dl', url])
        with open(args.downloaded_file, 'a') as file:
            file.write(url + '\n')
