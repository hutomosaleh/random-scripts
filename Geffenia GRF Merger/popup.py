import sys
import os
import css
import json

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5 import QtCore, QtTest


directory = 'Files/'


def save_json(filename, file):
    with open(directory + filename, 'w') as f:
        json.dump(file, f, indent=2, sort_keys=False)


def read_json(filename):
    with open(f'{directory}{filename}', 'r') as f:
        savefile = json.load(f)
    return savefile


class Popup(QWidget):
    def __init__(self):
        super().__init__()
        self.savefile = read_json('settings.json')
        self.resize(300, 80)
        self.popup_confirmation()
        self.show()

    def popup_confirmation(self):
        self.setStyleSheet(css.popup())
        self.lbl_text1 = QLabel('Please locate your Nova RO folder!')
        self.lbl_text1.setStyleSheet(css.lbl_btn())
        self.lbl_text1.setAlignment(QtCore.Qt.AlignCenter)
        self.btn_locate = QPushButton("Locate")
        self.btn_locate.setStyleSheet(css.btn())
        self.btn_locate.clicked.connect(self.file_open)
        container_lyt_confirm = QWidget()
        self.lyt_submain = QVBoxLayout(container_lyt_confirm)
        self.lyt_submain.addWidget(self.lbl_text1)
        self.lyt_submain.addWidget(self.btn_locate)

        self.lbl_text2 = QLabel('Succesfully changed the settings!')
        self.lbl_text2.setStyleSheet(css.lbl())
        self.lbl_text2.setAlignment(QtCore.Qt.AlignCenter)
        container_lyt_done = QWidget()
        container_lyt_done.setStyleSheet(css.container())
        self.lyt_submain2 = QVBoxLayout(container_lyt_done)
        self.lyt_submain2.addWidget(self.lbl_text2)

        self.lbl_text3 = QLabel('Choose a NovaRO Folder!')
        self.lbl_text3.setStyleSheet(css.lbl())
        self.lbl_text3.setAlignment(QtCore.Qt.AlignCenter)
        container_lyt_error = QWidget()
        container_lyt_error.setStyleSheet(css.container())
        self.lyt_submain2 = QVBoxLayout(container_lyt_error)
        self.lyt_submain2.addWidget(self.lbl_text3)

        self.stack = QStackedWidget()
        self.stack.addWidget(container_lyt_confirm)
        self.stack.addWidget(container_lyt_done)
        self.stack.addWidget(container_lyt_error)
        self.lyt_main = QVBoxLayout()
        self.lyt_main.addWidget(self.stack)
        self.setLayout(self.lyt_main)

        if self.savefile["directory"] != "":
            self.setWindowTitle('Success')
            self.stack.setCurrentIndex(1)
            QtTest.QTest.qWait(2000)
            self.close()
        else:
            self.setWindowTitle('Confirmation')

    def file_open(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Folder"))
        if "NovaRO" in path:
            self.savefile["directory"] = path
            save_json('settings.json', self.savefile)
            self.stack.setCurrentIndex(1)
        elif path == "":
            pass
        else:
            self.stack.setCurrentIndex(2)
            QtTest.QTest.qWait(2000)
            self.file_open()

    def overwrite_file(self):
        original_name = self.savefile["data"]
        path_data = "Files/data.ini"
        if os.path.exists(self.savefile["directory"]) and self.savefile["directory"] != "":
            os.remove(self.savefile["directory"])
            os.rename(self.savefile["data"], path_data)
            self.savefile["data"] = path_data
            copy2("Files/data.ini", self.savefile["directory"])
            os.rename(self.savefile["data"], original_name)


def clearLayout(layout):
    while layout.count():
        child = layout.takeAt(0)
        if child.widget():
            child.widget().deleteLater()
