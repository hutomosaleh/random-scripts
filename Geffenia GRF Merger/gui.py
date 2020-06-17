import sys
import time
import json
import css

from datetime import datetime
from PyQt5 import QtCore
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *


class MainWindow(object):
    def ui(self, MainWindow0):
        self.setWindowTitle('Geffenia GRF Activator')

        self.cb_geffenia = QRadioButton("Geffenia")
        self.cb_geffenia.setStyleSheet(css.radio())
        self.cb_normal = QRadioButton("Normal")
        self.cb_normal.setStyleSheet(css.radio())
        self.cb_normal.setChecked(True)

        self.btn_apply = QPushButton("Apply")
        self.btn_apply.setStyleSheet(css.btn())

        lyt_radiobutton = QHBoxLayout()
        lyt_radiobutton.addWidget(self.cb_geffenia)
        lyt_radiobutton.addWidget(self.cb_normal)
        container_lyt_main = QWidget()
        container_lyt_main.setStyleSheet(css.container())
        lyt_submain = QVBoxLayout(container_lyt_main)
        lyt_submain.addLayout(lyt_radiobutton)
        lyt_submain.addWidget(self.btn_apply)
        lyt_main = QVBoxLayout()
        lyt_main.addWidget(container_lyt_main)

        widget = QWidget()
        widget.setLayout(lyt_main)
        self.setCentralWidget(widget)

