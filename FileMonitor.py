import time
import logging
import sys

from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler


class myFileWatchHandler(PatternMatchingEventHandler):
    def __init__(self, patterns):
        super().__init__(patterns=patterns)

    def on_created(self, event):
        return logging.warning(event.src_path + '文件被创建！')

    def on_deleted(self, event):
        return logging.warning(event.src_path + '文件被删除！')

    def on_moved(self, event):
        return logging.warning(event.src_path + '文件被移动为' + event.dest_path)

    def on_modified(self, event):
        return logging.warning(event.src_path + '文件被修改！')


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = '.'
    patterns = ['*.html', '*.php', '*.exe']
    # path = sys.argv[1]
    # patterns = sys.argv[2]

    logging.info('监控程序开始运行...开始对当前目录及子目录进行监控')
    event_handler = myFileWatchHandler(patterns=patterns)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    finally:
        observer.stop()
        observer.join()
