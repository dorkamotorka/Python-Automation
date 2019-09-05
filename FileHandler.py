from watchdog.events import FileSystemEventHandler, FileSystemEvent
from watchdog.observers import Observer

import time
import os


input_folder = "/Users/Teo/Desktop/PROGRAMIRANJE"
output_python_folder = "/Users/Teo/Desktop/PYTHON"
output_C_folder = "/Users/Teo/Desktop/C"
output_java_folder = "/Users/Teo/Desktop/JAVA"

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
            root, ext = os.path.splitext(filename)
            ext_dict = {
                ".py" : output_python_folder,
                ".c" : output_C_folder,
                ".java" : output_java_folder
            }
            destination = ext_dict[ext] + "/" + filename
            os.rename(source, destination)

    def on_created(self, event) :
        for filename in os.listdir(input_folder) :
            source = input_folder + "/" + filename
            root, ext = os.path.splitext(filename)
            ext_dict = {
                ".py" : output_python_folder,
                ".c" : output_C_folder,
                ".java" : output_java_folder
            }
            destination = ext_dict[ext] + "/" + filename
            os.rename(source, destination)
    

files_handler = MyHandler()
Obs = Observer()
Obs.schedule(files_handler, input_folder, recursive=True)
Obs.start()

try :
    while True :
        time.sleep(10) #file transfer lag
except KeyboardInterrupt :
    Obs.stop()
Obs.join()