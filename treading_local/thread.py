import threading
import logging
from _threading_local import local

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-0s) %(message)s',)


def add_log(local):
    try:
        local.val = local.val + "w"
        print(f"LOG = {local.val}")
    except AttributeError:
        local.val = "poczatek"
        logging.debug('No value yet')
    else:
        logging.debug('value=%s', local.val)


def logs(local):
    print("logs")
    # add_log(local)
    add_log(local)
    # print(f"l.log = {l.log}")


def start_log():
    local = threading.local()
    return local
