# import logging
from cmath import log
from arjuna import *
import webview

from contextlib import redirect_stdout
from io import StringIO
from api import ap
from app import traverse_folders

# logger = logging.getLogger(__name__)

def launch_server():
    ap.run(port=5001, use_evalex=False)

if __name__ == '__main__':

    window = webview.create_window('Arjuna IDE', url="http://localhost:5001", fullscreen=False, height=700, width=1000)
    window.expose(traverse_folders)
    log_info("Starting...")
    # print("starting...")
    webview.start()
    # webview.start(func=launch_server)