from gridtrader.gateway.binances import BinancesGateway
from gridtrader.event import Event, EventEngine

def test_rest_client():
    futures_settings = {
        "key": "41GkmjbBhBUylGvlghfHdAczo2mMBZcpjfAWq4mLEjIU3pv5O39V1fkO7TIqTl43",
        "secret": "N9wl8yJ2CyQmwcPQJWKYck5CVmATwOwyILckLe1gVHMBkmLxC3zCnOoZs9uk2xJm",
        "futures_type": "USDT",
        "proxy_host": "",
        "proxy_port": 0
    }
    engine = EventEngine()
    gw = BinancesGateway(engine)
    gw.connect(futures_settings)
    res = gw.rest_api.set_leverage("BTCUSDT", 20)
    print(res)
    # import pdb; pdb.set_trace()

