#!/usr/bin/python
# -*- coding: utf-8 -*-
import base64
import requests

url = '1'

def sample(password):
    return base64.b64encode(password)


if __name__ == "__main__":
    crypted = sample(password=requests.get(url))
