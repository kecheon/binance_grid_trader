from gridtrader.gateway.binances import BinancesGateway
from gridtrader.event import Event, EventEngine


def test_rest_client():
    # "key": "41GkmjbBhBUylGvlghfHdAczo2mMBZcpjfAWq4mLEjIU3pv5O39V1fkO7TIqTl43",
    # "secret": "N9wl8yJ2CyQmwcPQJWKYck5CVmATwOwyILckLe1gVHMBkmLxC3zCnOoZs9uk2xJm",
    futures_settings = {
        "key": "8d9f18e1a0eb2272fd132afe11bd80b03f349d8fea4065f00fe5cbb3211594e5",
        "secret": "44b8c27caf37eb8886849d32db0de6f15b90e583e156710317894bfb2655bc36",
        "futures_type": "USDT",
        "proxy_host": "",
        "proxy_port": 0,
    }
    engine = EventEngine()
    gw = BinancesGateway(engine, testnet=True)
    gw.connect(futures_settings)
    # res = gw.rest_api.set_leverage("BTCUSDT", 20)
    import pdb

    pdb.set_trace()
