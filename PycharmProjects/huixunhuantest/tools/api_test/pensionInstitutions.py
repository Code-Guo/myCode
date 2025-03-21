# -*- coding: utf-8 -*-
import requests
import req
import time
import logging
import openpyxl

area = {
    "110000000000": {"北京": 608},
    "120000000000": {"天津": 435},
    "130000000000": {"河北": 2076},
    "140000000000": {"山西": 917},
    "150000000000": {"内蒙古": 614},
    "210000000000": {"辽宁": 2314},
    "220000000000": {"吉林": 1577},
    "230000000000": {"黑龙江": 1776},
    "310000000000": {"上海": 841},
    "320000000000": {"江苏": 2249},
    "330000000000": {"浙江": 1800},
    "340000000000": {"安徽": 2599},
    "350000000000": {"福建": 841},
    "360000000000": {"江西": 1538},
    "370000000000": {"山东": 2648},
    "410000000000": {"河南": 4236},
    "420000000000": {"湖北": 1899},
    "430000000000": {"湖南": 1803},
    "440000000000": {"广东": 1755},
    "450000000000": {"广西": 1051},
    "460000000000": {"海南": 140},
    "500000000000": {"重庆": 1721},
    "510000000000": {"四川": 2640},
    "520000000000": {"贵州": 169},
    "530000000000": {"云南": 851},
    "540000000000": {"西藏": 78},
    "610000000000": {"陕西": 926},
    "620000000000": {"甘肃": 343},
    "630000000000": {"青海": 99},
    "640000000000": {"宁夏": 97},
    "650000000000": {"新疆": 629},
    "660000000000": {"新疆兵团": 132}
}
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


def crawl_per():
    """

    :return:
    """

    for key, value in area.items():
        pageNumber = 1
        page = int(list(value.values())[0] / 10) + 1
        host = 'https://zwfw.mca.gov.cn'
        api = '/webglbiz/interface/service/callMethodV1'
        timestamp = str(int(time.time())) + '000'
        while pageNumber <= page:
            body = {
                "stringParams": {"access_key": "jmgc_yl", "timestamp": timestamp,
                                 "biz_content": {"axbe0003": "", "axbe0023": key, "pageNumber": pageNumber,
                                                 "pageSize": 10},
                                 "sign": "", "request_id": "aaa", "version": "1.0", "format": "json",
                                 "serviceid": "jmgc_yl_queryRecord"}
            }
            response = req.post_req(host=host, api=api, body=body)
            try:
                if response.status_code == 200:
                    result = response.json()
                    data_list = result.get('data').get('data').get('biz_data').get('data').get('pageBean').get('list')

                    for i in data_list:
                        address = i.get('axbe0013')
                        name = i.get('axbe0003')
                        areas = i.get('axbe0023')
                        credit_code = i.get('axbe0002')
                        bed_num = i.get('ahae2347')
                        sheet.append(
                            [areas, name, credit_code, address, bed_num])
                        logging.info(
                            [areas, name, credit_code, address, bed_num, pageNumber])
                        wb.save('养老机构数据.xlsx')

                pageNumber += 1
            except Exception as e:
                continue


if __name__ == '__main__':
    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet.append(
        ['地区', '机构名称', '统一社会信用代码', '地址', '床位数'])
    crawl_per()
