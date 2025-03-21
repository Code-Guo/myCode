# -*- coding: utf-8 -*-

import requests
import json
from requests.adapters import HTTPAdapter
import urllib3
from fake_useragent import UserAgent

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

s = requests.Session()
ua = UserAgent()


def post_req(host: str, api: str, body: dict, ticket='') -> requests.Response:
    url = host + api
    header = {
        "content-type": "application/json; charset=utf-8", # application/json; charset=utf-8
        "user-agent": ua.random
    }
    if ticket:
        header["Authori-zation"] = ticket

    try:
        response = s.post(url=url,
                          headers=header,
                          data=json.dumps(body),
                          verify=False,
                          timeout=30
                          )
        s.keep_alive = True
        return response


    except Exception as e:
        print(e)


def get_req(host: str, api: str, param: dict, ticket='') -> requests.Response:
    url = host + api
    header = {
        "content-type": "application/json;charset=UTF-8"
    }
    if ticket:
        header["Authori-zation"] = ticket

    try:
        response = s.get(url=url,
                         headers=header,
                         params=param,
                         verify=False,
                         timeout=5
                         )

        return response

    except Exception as e:
        return e
