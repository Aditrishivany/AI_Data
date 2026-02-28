from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import subprocess

class ChangeHandler(FileSystemEventHandler):

    def on_modified(self, event):
        print("File changed:", event.src_path)
        subprocess.run(["python", "pipeline/pipeline.py"])

if __name__ == "__main__":

    path = "app"

    event_handler = ChangeHandler()
    observer = Observer()

    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    print("Monitoring started...")

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
