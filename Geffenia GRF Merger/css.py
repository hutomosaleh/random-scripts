def gui_background():
    return """
    QMainWindow{
    background-color: #000000;
    }
    """


def window():
    return """
    QApplication{
    background-color: #000000;
    color: #E1AD27;
    }
    """


def normal():
    return """
    background-color:#FFFFFF;
    """


def lbl_btn():
    return """
    QLabel{
    background-color: #141414;
    border-style:outset;
    border-width:2px;
    border-radius:10px;
    border-color:#F09E20;
    color:#E1AD27;
    font:11px;
    padding:3px;
    min-width:6em;
    }

    QPushButton::hover{
    background-color: #343436;
    }

    QPushButton::pressed{
    background-color: #1A1A20;
    }

    """


def btn():
    return """
    QPushButton{
    background-color: #E1AD27;
    border-style:outset;
    border-width:2px;
    border-radius:10px;
    border-color:#F09E20;
    color:#000000;
    font:11px;
    font-weight:bold;
    padding:3px;
    min-width:6em;
    }

    QPushButton::hover{
    background-color: #FFD500;
    }

    QPushButton::pressed{
    background-color: #F09E20;
    }
    """


def tbl():
    return """
    QTableView{
    background-color: #1E1E1E;
    border-style:outset;
    border-width:2px;
    border-radius:10px;
    border-color:#F09E20;
    color:#E1AD27;
    font:11px;
    padding:3px;
    min-width:6em;
    }

    QTableCornerButton::section{
    background-color:#141414;
    }

    QTableWidget::item{
    border-left:4px solid #161616;
    border-radius:2px;
    }
    """


def scrollbar():
    return """
    QScrollBar:horizontal {
    background: #141414;
    }

    QScrollBar::handle:horizontal {
        background: #2B2D2F;
    }
    """


def lbl():
    return """
    QLabel{
    font:11px;
    color:#E1AD27;
    border-width:0px;
    border-radius:0px;
    }
    """


def radio():
    return """
    QRadioButton{
    font:11px;
    color:#E1AD27;
    border-width:0px;
    border-radius:0px;
    }
    """


def messagebox():
    return """
    QMessageBox{
    font:11px;
    color:#E1AD27;
    border-width:0px;
    border-radius:0px;
    }
    """


def lbl_refresh():
    return """
    QLabel{
    font:11px;
    color:#29D03C;
    border-width:0px;
    border-radius:0px;
    }
    """


def notif():
    return """
    background-color:#141414;
    font:11px;
    color:#E0DEDE;
    border-style:outset;
    border-width:2px;
    border-radius:10px;
    padding:3px;
    border-color:#F09E20;
    """


def header():
    return """
    QHeaderView{
    background-color:#141414;
    }

    QHeaderView::section{
    background-color:#141414;
    color:#E1AD27;
    font:11px;
    }

    QHeaderView{
    background-color:#141414;
    }
    """


def container():
    return """
    background-color:#141414;
    border-style:outset;
    border-width:2px;
    border-radius:10px;
    border-color:#F09E20;
    """


"""
    Add Item Popup
"""


def popup():
    return """
    QWidget{
    background-color: #141414;
    }
    """


def line_edit():
    return """
    QLineEdit{
    background-color: #1E1E1E;
    color: #E1AD21;
    border-style:outset;
    border-width:2px;
    border-radius:10px;
    padding:3px;
    border-color:#F09E20;
    }
    """


def lbl_popup():
    return """
    QLabel{
    font:11px;
    color:#E1AD27;
    border-width:0px;
    border-radius:0px;
    }
    """