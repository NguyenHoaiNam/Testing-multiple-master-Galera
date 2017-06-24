# Author: Nam Nguyen Hoai
# coding: utf-8

import string
import random

import config


def rand():
    """
    Generate random string to be url path
    """
    return ''.join(random.SystemRandom().choice(
        string.ascii_letters + string.digits)
                   for _ in range(config.RAND_DIR_LENGTH))
