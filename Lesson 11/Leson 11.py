#pip install lxml
#pip install requests
#pip install bautifulsoup4
#pip install fastapi

import requests
import json

class SirotinskyAPI:

        def __init__(self, user, passw):
            self.__mytoken = self.__get_token(user, passw)
            self.__jstoken = json.loads(self.__mytoken.text)

        def __get_token(self, username, password):
            data = {'grant_type': '',
                    'username': username,
                    'password': password,
                    'scope': '',
                    'client_id': '',
                    'client_secret': ''}
            __mytoken = requests.post('https://api.sirotinsky.com/token', data=data)
            return __mytoken

        def root(self):
            return requests.get('https://api.sirotinsky.com')

        def hello(self, name):
            return requests.get(f'https://api.sirotinsky.com/hello/{name}').text

        def efrsb_req(self, req_type, inn):
            reqdata = {'inn': inn, 'token': self.__jstoken}
            path = self.__jstoken['access_token']
            return requests.get(f'https://api.sirotinsky.com/{path}/efrsb/{req_type}/{inn}', data=reqdata)

        def dadata_party(self, inn):
            reqdata = {'inn': inn, 'token': self.__mytoken}
            path = self.__jstoken['access_token']
            return requests.get(f'https://api.sirotinsky.com/{path}/dadata/party/{inn}', data=reqdata)

nvar = SirotinskyAPI(user='HSE_student', passw='123123123')
#checks
print(nvar.root())
print(nvar.hello('cтудент-прогульщик'))
#print(nvar.mytoken.content)
#print(nvar.jstoken)
print('Manager - ' + nvar.efrsb_req('manager', '1111111').text)
print('Trader - ' + nvar.efrsb_req('trader', '1111111').text)
print('Organisation - ' + nvar.efrsb_req('organisation', '1111111').text)
print('DaData - ' + nvar.dadata_party('1111111').text)
