from gridtrader.event import EventEngine

from gridtrader.trader.engine import MainEngine
from gridtrader.trader.ui import MainWindow, QtAppSingleton


class CustomMainWindow(MainWindow):
    def __init__(self, qapp, main_engine, event_engine):
        super().__init__(main_engine, event_engine)
        self.qapp = qapp


if __name__ == "__main__":
    event_engine = EventEngine()
    main_engine = MainEngine(event_engine, testnet=True)

    qapp_instance = QtAppSingleton()
    qapp = qapp_instance.qapp

    # make context explicit
    main_window = CustomMainWindow(qapp, main_engine, event_engine)
    main_window.showMaximized()

    qapp.exec()
