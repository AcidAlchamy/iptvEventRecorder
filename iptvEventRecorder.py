import subprocess
import time
import signal
import sys

# Set your desired recording duration here (in minutes)
RUNTIME = 30

# Convert RUNTIME to seconds
RUNTIME = RUNTIME * 60

class GracefulInterruptHandler(object):
    def __init__(self, sig=signal.SIGINT):
        self.sig = sig
        self.interrupted = False
        self.released = False

    def __enter__(self):
        self.original_sigint = signal.getsignal(self.sig)
        signal.signal(self.sig, self.exit_gracefully)
        return self

    def exit_gracefully(self, signum, frame):
        self.release()
        self.interrupted = True

    def __exit__(self, type, value, tb):
        self.release()

    def release(self):
        if self.released:
            return False
        signal.signal(self.sig, self.original_sigint)
        self.released = True

def download_stream():
    with GracefulInterruptHandler() as h:
        while not h.interrupted:
            try:
                command = [
                    'ffmpeg',
                    '-i', 'https://your_stream_url_here',
                    '-t', str(RUNTIME),
                    '-c', 'copy',
                    'output_file.mp4'
                ]
                subprocess.run(command, check=True)
                break
            except Exception as e:
                print(f"Error occurred: {str(e)}. Trying to reconnect in 5 seconds.")
                time.sleep(5)
        if h.interrupted:
            print('\nInterrupted! Stopping download...')

download_stream()
