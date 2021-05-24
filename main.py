import _thread
import ddnsThread
import logging

try:
    _thread.start_new_thread(ddnsThread.run)
except:
    logging.error("Cannot create a thread")
