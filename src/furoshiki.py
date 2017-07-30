import furoshikiconfig as CONFIG
import random

def init_config():
    CONFIG.SYSTEM_NAME = "Furoshiki"

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

init_config()