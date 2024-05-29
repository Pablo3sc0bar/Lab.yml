from helper import *
from datetime import datetime


class Log:

    @classmethod
    def info(self, text):
        print("[" + Y + datetime.now().strftime(
            "%H:%M:%S") + N + "] [" + G + "INFO Инофрмационные блок" + N + "] " + text)

    @classmethod
    def warning(self, text):
        print("[" + Y + datetime.now().strftime("%H:%M:%S") + N + "] [" + Y + "WARNING Внимание" + N + "] " + text)

    @classmethod
    def high(self, text):
        print("[" + Y + datetime.now().strftime(
            "%H:%M:%S") + N + "] [" + R + "CRITICAL Критическое место" + N + "] " + text)
