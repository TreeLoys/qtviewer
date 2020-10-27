#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
ToDo libglvnd-dev
Created by treeloys at 24.04.20
"""

import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow
from PyQt5.QtWebEngineWidgets import QWebEngineView, QWebEngineSettings, QWebEnginePage
from PyQt5.QtCore import QUrl, QThread, QObject
import threading

sys.argv.append("--disable-web-security")
sys.argv.append("--remote-debugging-port=5000")


class Browser(QWebEngineView):
    def __init__(self, pa, weight, height):
        super().__init__(pa)
        self.setFixedHeight(height)
        self.setFixedWidth(weight)


class WebUIWidget(QMainWindow):
    def __init__(self, title="QT Viewer", url="localhost", port=3333, width=800, height=600):
        super().__init__()
        self.setFixedWidth(width)
        self.setFixedHeight(height)

        self.url = "http://{}:{}".format(url, port)

        self.view = Browser(self, width, height)
        self.page = QWebEnginePage()
        self.page.setUrl(QUrl(self.url))
        self.view.setPage(self.page)

        change_setting = self.view.page().settings().setAttribute
        settings = QWebEngineSettings
        change_setting(settings.LocalStorageEnabled, True)
        change_setting(settings.PluginsEnabled, True)

        # TODO: These settings aren't implemented in QWebEngineSettings (yet)
        #change_setting(settings.DeveloperExtrasEnabled, True)
        #change_setting(settings.OfflineStorageDatabaseEnabled, True)
        #change_setting(settings.OfflineWebApplicationCacheEnabled, True)
        self.setWindowTitle(title)
        print("Done init")
        self.show()

class WebUI(object):
    def __init__(self, *args, **kwargs):
        self.appGui = QApplication(sys.argv)
        ex = WebUIWidget(*args, **kwargs)
        sys.exit(self.appGui.exec_())


if __name__ == "__main__":
    pass