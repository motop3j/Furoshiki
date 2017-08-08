# vim: set fileencoding=utf-8

import furoshikiconfig as CONFIG
import random
import logging
import logging.config
import yaml
import os

logger = None

def init():
    CONFIG.SYSTEM_NAME = "Furoshiki"
    init_log()

def init_log():
    global logger
    p = os.path
    f = p.dirname(p.abspath(__file__))
    f = p.join(f, "config/logging.yaml")
    if not os.path.isfile(f):
        return
    logging.config.dictConfig(yaml.load(open(f).read()))
    logger = logging.getLogger()
    logger.debug("logger start.")
    logger.debug(os.getcwd())



def is_initialized():

    return False

def create_password():
    passwd = list()
    src = list("abcdefghijkmnpqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ")
    random.shuffle(src)
    passwd.extend(src[:8])
    src = list("23456789")
    random.shuffle(src)
    passwd.extend(src[:2])
    src = list("!#$%&-=@*+<>?/()[]{}")
    random.shuffle(src)
    passwd.extend(src[:2])
    random.shuffle(passwd)
    return "".join(passwd)

init()