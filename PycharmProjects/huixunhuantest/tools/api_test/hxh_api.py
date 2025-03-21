# -*- coding: utf-8 -*-
import requests
import req

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJ0ZXN0LTEuaHVpeHVuaHVhbi5jbiIsImF1ZCI6InRlc3QtMS5odWl4dW5odWFuLmNuIiwiaWF0IjoxNzM5Nzk3MDEzLCJuYmYiOjE3Mzk3OTcwMTMsImV4cCI6MTczOTg4MzQxMywianRpIjp7ImlkIjoyLCJ0eXBlIjoib3V0In19.1x51ye0vNFJ8pYz98q1pzYnXFWbRQ2QCeXKIRbQnsg8"


def get_token() -> None:
    host = "https://test-1.huixunhuan.cn"
    api = "/outapi/get_token"
    body = {
        "appid": "huaweitest",
        "appsecret": "D6mnxGjrRFmy2brYdfseiE7pFWBsx46c"
    }
    response = req.post_req(host=host, api=api, body=body)

    print(response.text)


def import_product():
    host = "https://mfg-test.huixunhuan.cn"
    api = "/externalapi/import/product"
    body = {
        "activity": "3c",
        "data": """[{
            "sn": "123",
            "imei": "123",
            "imei2": "123",
            "product_code": "123",
            "brand": "123",
            "title": "123",
            "cate": "123",
            "model": "123",
            "energy_level": "无",
            "out_stock_date": "2025-01-30",
            "region": "山东省聊城市",
            "price": 3699,
            "produce_date": "2024-12-01"
        }]"""
    }
    response = req.post_req(host=host, api=api, body=body, ticket=token)

    print(response.json())
    if response.json():
        return response.json()['data']['import_id']


def import_activity() -> None:
    host = "https://mfg-test.huixunhuan.cn"
    api = "/externalapi/import/activity"
    body = {
        "activity": "3c",
        "data": """[{"sn":"AASDASD13123123","active_status":"已激活","active_time":"2025-01-11","active_location":"山东省聊城市东昌湖胡迪公园"}]"""
    }
    response = req.post_req(host=host, api=api, body=body, ticket=token)
    print(response.json())


def import_status(import_id):
    host = "https://mfg-test.huixunhuan.cn"
    api = "/externalapi/import/status"
    params = {"import_id": import_id}

    response = req.get_req(host=host, api=api, param=params, ticket=token)
    print(response.json())


def products():
    import_id = import_product()
    import_status(import_id=import_id)


if __name__ == "__main__":
    import_activity()
