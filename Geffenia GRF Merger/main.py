import asyncio
import os
import sys
import css
import json
import PyQt5

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtTest
from asyncqt import QEventLoop, asyncSlot
from shutil import copy2

from gui import MainWindow
from popup import Popup

directory = 'Files/'


def save_json(filename, file):
    with open(directory + filename, 'w') as f:
        json.dump(file, f, indent=2, sort_keys=False)


def read_json(filename):
    with open(f'{directory}{filename}', 'r') as f:
        savefile = json.load(f)
    return savefile


class MainWindow0(QMainWindow, MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setStyleSheet(css.gui_background())
        self.savefile = read_json('settings.json')
        self.ui(self)
        self.btn_apply.clicked.connect(self.popup)
        if self.savefile["data"] == "Files/data_geffenia.ini":
            self.cb_geffenia.setChecked(True)
        elif self.savefile["data"] == "Files/data_normal.ini":
            self.cb_normal.setChecked(True)
        self.cb_geffenia.toggled.connect(lambda: self.togglecb(self.cb_geffenia))
        self.cb_normal.toggled.connect(lambda: self.togglecb(self.cb_normal))

    @asyncSlot()
    async def popup(self):
        self.popup_window = Popup()
        self.overwrite_file()

    @asyncSlot()
    async def togglecb(self, state):
        self.savefile = read_json('settings.json')
        if state.text() == 'Geffenia':
            if state.isChecked():
                self.savefile["data"] = "Files/data_geffenia.ini"
        elif state.text() == 'Normal':
            if state.isChecked():
                self.savefile["data"] = "Files/data_normal.ini"
        save_json("settings.json", self.savefile)

    def overwrite_file(self):
        self.savefile = read_json('settings.json')
        original_name = self.savefile["data"]
        path_data = "Files/data.ini"
        if os.path.exists(self.savefile["directory"] + "/data.ini") and self.savefile["directory"] != "":
            os.remove(self.savefile["directory"] + "/data.ini")
            os.rename(self.savefile["data"], path_data)
            self.savefile["data"] = path_data
            copy2("Files/data.ini", self.savefile["directory"])
            copy2("Files/geffenia.grf", self.savefile["directory"])
            os.rename(self.savefile["data"], original_name)



def windowLauncher():
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon('Files/incubus.png'))
    app.setStyleSheet(css.window())
    loop = QEventLoop(app)
    asyncio.set_event_loop(loop)

    w = MainWindow0()
    w.show()
    loop.run_forever()


if __name__ == "__main__":
    windowLauncher()
