import requests
import json


class Incident:
    url = 'https://dev98448.service-now.com/api/now/table/incident'
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    payload = {"description": "money deducted", "short_description": "ticket creation testing from python"}

    def __init__(self, user, pwd):
        self.user = user
        self.pwd = pwd

    def m1(self):
        response = requests.post(self.url, auth=(self.user, self.pwd), headers=self.headers,
                                 data=json.dumps(self.payload))
        if response.status_code == 201:
            response_result = response.json()
            print("success", response_result)
            print(response_result['result']['number'])
            print(response_result['result']['sys_id'])
        else:
            print("failure","unable to create ticket")
            

i = Incident("admin", "wTh/h1-HKv2U")
i.m1()

