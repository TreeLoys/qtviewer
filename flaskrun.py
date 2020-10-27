#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created by treeloys at 25.04.20
"""
import socket
import sys
import threading
from contextlib import closing

from flask import Flask



from qtviewer.qtviewer import WebUI


def find_free_port():
    """Свободный порт получить"""
    with closing(socket.socket(socket.AF_INET, socket.SOCK_STREAM)) as s:
        s.bind(('', 0))
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        return s.getsockname()[1]


def flaskRun(app, host, port, debug):
    app.run(host, port, debug, use_reloader=False)


def appRun(app, host="127.0.0.1", port=None, debug=True, width=800, height=600, using_win32=False,
           title="My Flask app"):
    port = port if port else find_free_port()

    print(host)
    if using_win32:
        import pythoncom
        pythoncom.CoInitialize()
    # app.run(debug=debug, host=host, port=port, use_reloader=False)
    flask_thread = threading.Thread(target=flaskRun, args=(app, host, port, debug,))
    flask_thread.daemon = True
    flask_thread.start()
    print(host, port)
    wu = WebUI(title=title, url=host, port=port, width=width, height=height)




if __name__ == "__main__":
    app = Flask(__name__)
    @app.route("/")
    def index():
        return "<h1>Welkome to app</h1>"

    appRun(app, host="localhost", width=100, height=100)