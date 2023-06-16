import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


counting = []
n = 5

if __name__ == "__main__":
    patterns = ["*"]
    ignore_patterns = None
    ignore_directories = False
    case_sensitive = True
    my_event_handler = PatternMatchingEventHandler(patterns, ignore_patterns, ignore_directories, case_sensitive)

def on_created(event):
    counting.append(1)
    print('do OCR')
    print('do upload')
    print('do delete')
def on_deleted(event):
    counting.append(1)
    print("succes delete") 

my_event_handler.on_created = on_created
my_event_handler.on_deleted = on_deleted


path = "D:\program files\yolov3tensorflow.v2\LicenseCAM_\ROI"
go_recursively = True
my_observer = Observer()
my_observer.schedule(my_event_handler, path, recursive=go_recursively)

my_observer.start()
try:
    while True:
        time.sleep(1)
        integer = int(time.time())
        print(integer[:1])
        print(len(counting),"terdektesi")
        counting.clear()
except KeyboardInterrupt:
    my_observer.stop()
    my_observer.join()
