import ctypes
import platform
import sys
import traceback
import types

import qdarkstyle
from PyQt5 import QtGui, QtWidgets, QtCore

from .mainwindow import MainWindow
from ..setting import SETTINGS
from ..utility import get_icon_path

qapp = None


def excepthook(exctype: type, value: Exception, tb: types.TracebackType) -> None:
    """
    Raise exception under debug mode, otherwise
    show exception detail with QMessageBox.
    """
    sys.__excepthook__(exctype, value, tb)

    msg = "".join(traceback.format_exception(exctype, value, tb))
    # qapp.signal_exception.emit(msg)

    sys.stderr.write(msg)


from PyQt5 import QtCore, QtGui, QtWidgets
import qdarkstyle
import platform
import ctypes


# Singleton class for the Qt application
class QtAppSingleton:
    _instance = None

    def __new__(cls, app_name="BeeBot-Binance Grid"):
        if cls._instance is None:
            cls._instance = super(QtAppSingleton, cls).__new__(cls)
            cls._instance._initialized = False
        return cls._instance

    def __init__(self, app_name="BeeBot-Binance Grid"):
        if self._initialized:
            return
        self._initialized = True

        self.qapp = None
        self.create_qapp(app_name)

    def create_qapp(self, app_name):
        sys.excepthook = excepthook

        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)

        self.qapp = QtWidgets.QApplication(sys.argv)
        self.qapp.setStyleSheet(qdarkstyle.load_stylesheet_pyqt5())

        font = QtGui.QFont(SETTINGS["font.family"], SETTINGS["font.size"])
        self.qapp.setFont(font)

        icon = QtGui.QIcon(get_icon_path(__file__, "vnpy.ico"))
        self.qapp.setWindowIcon(icon)

        if "Windows" in platform.uname():
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(app_name)

        return self.qapp
