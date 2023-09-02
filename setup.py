from cx_Freeze import setup, Executable

setup(
    name="Beebot-grid",
    version="1.0",
    description="Binance Gridbot",
    executables=[Executable("main.py")]
)

