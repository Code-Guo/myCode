import requests
import req


class TaxRate(object):
    def __init__(self, page, pageSize):
        self.url = 'http://gss.customs.gov.cn'
        self.body = {
            "__RequestVerificationToken": "GCMp5pRiXlAGpnp57dbT6oeKrbM7VB1v_qpImavdwCTeS42rMdOLpxRsETam1RVlgXavNOMjshYAjAyP4ZnmfgQbNbzyBgJF0LtZ-feabQA1",
            "page": page,
            "pageSize": pageSize,
            "Code_Ts_S": "",
            "G_Name": "",
        }

    def get_tax_rate(self):
        response = req.post_req(host=self.url, body=self.body, api='/CLSouter2020/TariffContent/GetQueryTaxNum')
        print(response.text)


if __name__ == '__main__':
    tax_rate = TaxRate(1, 20)
    tax_rate.get_tax_rate()
