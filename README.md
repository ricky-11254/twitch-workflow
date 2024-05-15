
---

# Twitch-Workflow

Twitch-Workflow is a command-line tool designed for Twitch streamers to seamlessly download their videos and upload them to YouTube. This workflow automates the process, ensuring efficiency and preventing duplicate uploads.

## Features

- **Download Twitch Videos**: Extract and download videos from your Twitch account.
- **Upload to YouTube**: Automatically upload downloaded videos to your YouTube channel.
- **Duplicate Prevention**: Track downloaded and uploaded videos to prevent duplicates.

## Prerequisites

- Python 3.x
- `requests` library
- `google-auth` library
- `google-api-python-client` library

## Setup

1. **Clone the Repository**:
    ```sh
    git clone https://github.com/yourusername/twitch-workflow.git
    cd twitch-workflow
    ```

2. **Configure API Tokens**:
    - Obtain your [Twitch API token](https://dev.twitch.tv/docs/authentication).
    - Obtain your [YouTube API token](https://developers.google.com/youtube/v3/getting-started).
    - Create a [Google Console Project](https://console.cloud.google.com/) and enable the YouTube Data API.

3. **Save Video Information**:
    - Save your video information in a JSON file (`twitch_videos.json`).
    - Direct the output of your script or API call to this JSON file.

## Usage

1. **Extract and Download Videos**:
    - Run the `extract_and_download.sh` script to extract video URLs from `twitch_videos.json` and download the videos.
    ```sh
    ./extract_and_download.sh
    ```

2. **Upload Videos to YouTube**:
    - Use the `upload_video.py` script to upload the downloaded videos to your YouTube channel.
    ```sh
    python upload_video.py
    ```

## File Descriptions

- **`videos/`**: Directory where all downloaded videos are stored.
- **`downloaded_videos.txt`**: File containing URLs of all downloaded videos.
- **`uploaded_videos.txt`**: File containing URLs of all uploaded videos.
- **`extract_and_download.sh`**: Script to extract URLs from `twitch_videos.json` and download the videos.
- **`twitch_videos.json`**: JSON file containing video information from Twitch.
- **`upload_video.py`**: Script to upload videos to YouTube.
- **`extract.py`**: Script to extract video URLs from `twitch_videos.json`.
- **`README.md`**: This file.

## Directory Structure

```
twitch-workflow/
├── videos/                       # Directory for storing videos
├── downloaded_videos.txt         # Contains URLs of downloaded videos
├── uploaded_videos.txt           # Contains URLs of uploaded videos
├── extract_and_download.sh       # Script to extract and download videos
├── twitch_videos.json            # JSON file with video information
├── upload_video.py               # Script to upload videos to YouTube
├── extract.py                    # Script to extract video URLs from JSON
└── README.md                     # Project documentation
```

## Notes

- Ensure that `downloaded_videos.txt` and `uploaded_videos.txt` are up-to-date to prevent re-downloading or re-uploading the same videos.
- Follow the API documentation for detailed steps on obtaining and configuring your API tokens.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please submit a pull request or open an issue to discuss any changes.

## Contact

For any questions or issues, please open an issue on GitHub.

---

