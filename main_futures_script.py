from time import sleep
from logging import INFO

from gridtrader.event import EventEngine
from gridtrader.trader.setting import SETTINGS
from gridtrader.trader.engine import MainEngine, CtaEngine

SETTINGS["log.active"] = True
SETTINGS["log.level"] = INFO
SETTINGS["log.console"] = True



def run_futures_strategy():
    SETTINGS["log.file"] = True

    event_engine = EventEngine()
    main_engine: MainEngine = MainEngine(event_engine)

    main_engine.write_log("create main engine")

    main_engine.connect(futures_settings, "Futures")
    main_engine.write_log("Connect Binance Futures Api")

    sleep(10)

    cta_engine: CtaEngine = main_engine.get_engine('strategy')
    cta_engine.init_engine()
    main_engine.write_log("Init Strategy Engine.")

    cta_engine.init_all_strategies()
    sleep(60)  # Leave enough time to complete strategy initialization
    main_engine.write_log("Init All Strategies.")

    cta_engine.start_all_strategies()
    main_engine.write_log("Start All Strategies.")

    while True:
        sleep(10)


if __name__ == "__main__":
    # the futures script, no ui, if you want to use the window UI, please use the main.py
    # before running, remember to past your api here.

    futures_settings = {
        "key": "41GkmjbBhBUylGvlghfHdAczo2mMBZcpjfAWq4mLEjIU3pv5O39V1fkO7TIqTl43",
        "secret": "N9wl8yJ2CyQmwcPQJWKYck5CVmATwOwyILckLe1gVHMBkmLxC3zCnOoZs9uk2xJm",
        "futures_type": "USDT",
        "proxy_host": "",
        "proxy_port": 0
    }

    run_futures_strategy()
