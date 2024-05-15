#!/bin/bash
# getting the video info
todo_file="channel_info.json"
downloaded_file="downloaded_videos.txt"
curl -X GET 'https://api.twitch.tv/helix/videos?user_id=<user-id>' -H 'Authorization: Bearer <client-secret>' -H 'Client-Id: <client-id>' >> $todo_file
python extract.py --downloaded_file $downloaded_file --todo_file $todo_file

