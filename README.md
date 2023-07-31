# IPTV Event Recorder

This Python script, 'iptvEventRecorder.py', allows you to record a live IPTV stream for a specified duration and saves the recording as an MP4 file. You can easily modify the code to customize the script according to your needs.

## Prerequisites

This script uses the `ffmpeg` software which needs to be installed and available in your system's PATH. You can download it from [here](https://ffmpeg.org/download.html). The script has been tested with Python 3.8, but it should work with other Python 3 versions as well.

## How to Use

1. Download the 'iptvEventRecorder.py' file or clone the entire repository.

2. Open 'iptvEventRecorder.py' in any text editor.

3. Look for this line in the code: `'-i', 'https://your_stream_url_here',`

4. Replace `'https://your_stream_url_here'` with your IPTV stream's URL.

5. To specify a recording duration, go to the top of the script and find this line: `RUNTIME = 30`

6. Replace `30` with your desired recording duration in minutes.

7. Save and close the file.

8. Open a terminal/command prompt.

9. Navigate to the directory where 'iptvEventRecorder.py' is located using the `cd` command.

10. Run the script by typing: `python iptvEventRecorder.py`

The script will then start recording the stream and save it as 'output_file.mp4'. You can stop the recording at any time by pressing Ctrl+C in the terminal where the script is running.

## Customizing the Script

You can customize the script according to your needs by modifying the code.

* **Changing the Output File Name and Format:** The script currently saves the recording as 'output_file.mp4'. You can change this by modifying the `'output_file.mp4'` part of the command array in the code.

* **Changing the Recording Duration:** The script currently records for 30 minutes by default. You can change this by modifying the `RUNTIME` variable at the top of the script.

## Troubleshooting

If you encounter any issues while using the script, try the following steps:

* **Check the Stream URL:** Make sure the stream URL you've entered in the script is correct and working. You can test it by opening the URL in VLC or another media player that supports streaming.

* **Check Your Internet Connection:** Make sure your internet connection is stable and fast enough to handle the stream.

* **Update `ffmpeg` and Python:** Make sure you're using the latest versions of `ffmpeg` and Python.

If you're still having issues, feel free to open an issue on GitHub.

## License

This script is released under the MIT License. See the `LICENSE` file for more details.
