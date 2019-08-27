from watchdog.events import FileSystemEventHandler, FileSystemEvent
from watchdog.observers import Observer

import time
import os


input_folder = "/Users/Teo/Desktop/PROGRAMIRANJE"
output_folder = "/Users/Teo/Desktop/PYTHON"

class MyHandler(FileSystemEventHandler) :
    '''
    def on_modified(self, event) :
        for filename in os.listdir(input_folder) :
            source = input_folder + "/" + filename
            destination = output_folder + "/" + filename
            os.rename(source, destination)

    def on_deleted(self, event) :
        for filename in os.listdir(input_folder) :
            source = input_folder + "/" + filename
            destination = output_folder + "/" + filename
            os.rename(source, destination)
    '''
    def on_moved(self, event) :
        for filename in os.listdir(input_folder) :
            source = input_folder + "/" + filename
            destination = output_folder + "/" + filename
            os.rename(source, destination)

    def on_created(self, event) :
        for filename in os.listdir(input_folder) :
            source = input_folder + "/" + filename
            destination = output_folder + "/" + filename
            os.rename(source, destination)
    

files_handler = MyHandler()
Obs = Observer()
Obs.schedule(files_handler, input_folder, recursive=True)
Obs.start()

try :
    while True :
        time.sleep(10) #wait to the file is transferred
except KeyboardInterrupt :
    Obs.stop()
Obs.join()