# -*- coding: utf-8 -*-

import logging
import openpyxl
import barcode
from barcode.writer import ImageWriter
import qrcode
from PIL import Image

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s: %(message)s')


def write_3csku() -> None:
    """
    写3csku的文件
    :return:
    """
    wb = openpyxl.Workbook()
    sheet = wb.active
    i = 1000000000
    j = 2000000000
    imei1 = 3000000000
    imei2 = 'N/A'
    sku_69 = 60000000000
    sort = 0
    while i < 1000010000:
        i += 1
        j += 1
        sku_69 += 1
        sort += 1
        imei1 += 1
        sheet.append(
            [sort, i, j, imei1, imei2, sku_69, '荣耀', 'A荣耀200Pro-16+1T月影白ELP-AN00', '智能手机', 'A荣耀200Pro',
             'SKU唯一标识', '2025-03-05', '山东省聊城市', '百大三联中心店', '未激活', '200.00', '2025-01-05'])
        logging.info(
            [sort, i, j, imei1, imei2, sku_69, '荣耀', 'A荣耀200Pro-16+1T月影白ELP-AN00', '智能手机', 'A荣耀200Pro',
             'SKU唯一标识', '2025-03-05', '山东省聊城市', '百大三联中心店', '未激活', '200.00', '2025-01-05'])

    wb.save(r'E:\3C生产企业SKU商品目录模板 (1).xlsx')


def invoice() -> None:
    """
    生成发票
    :return:
    """


def _barcode() -> None:
    """
    生成条形码
    :return:
    """
    print(f"python-barcode支持的条形码格式：\n{barcode.PROVIDED_BARCODES}")
    EAN = barcode.get_barcode_class('code128')  # gs1_128  gs1

    # 条形码内容
    sn = '24H00285010716'
    _69 = '6939400204821'
    imei = '861262073663400'

    # 创建条形码对象
    ean = EAN(sn, writer=ImageWriter())
    ean_69 = EAN(_69, writer=ImageWriter())
    ean_imei = EAN(imei, writer=ImageWriter())

    # 保存条形码图片，并且返回路径
    ean.save(r"file/sn条形码")
    ean_69.save("file/69条形码")
    ean_imei.save("file/imei条形码")


def QrCode(uid: str) -> None:
    """
    生成二维码
    :return:
    """
    # 配置二维码参数
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # 添加数据
    qr.add_data(f"http://wl.bbqk.com/{uid}/0.html")
    qr.make(fit=True)

    # 创建二维码图像并自定义颜色
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图片
    img.save(r"file/二维码.png")


def QrCode_New(productId: str, tenantId: str, productTypeCode: str) -> None:
    """
    生成新能效二维码
    :return:
    """
    # 配置二维码参数
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_H,
        box_size=10,
        border=4,
    )

    # 添加数据
    # https://www.energylabel.com.cn/signDetails?productId=633881710439&tenantId=854&productTypeCode=32&isOld=1
    qr.add_data(
        f"https://www.energylabel.com.cn/signDetails?productId={productId}&tenantId={tenantId}&productTypeCode={productTypeCode}&isOld=1")
    qr.make(fit=True)

    # 创建二维码图像并自定义颜色
    img = qr.make_image(fill_color="black", back_color="white")

    # 保存图片
    img.save(r"file/新能效二维码.png")


if __name__ == '__main__':
    uid = "t25zkw1280"  # "w25bch"
    productId = "633881725803"   # 633881747322   19一级  633881747164  # 633881747573   # 633881747431  洗碗机 03
    tenantId = ""
    productTypeCode = "28"
    QrCode(uid=uid)
    QrCode_New(productId=productId, tenantId=tenantId, productTypeCode=productTypeCode)

    _barcode()
