from rest_framework.test import APITestCase
import requests
# Create your tests here.
class wetherTestCase(APITestCase):

    def test_api(self):
        res = requests.get('http://127.0.0.1:8000/api/')
        res = res.json()
        print(res)
        self.assertEquals(res , 'sucess')
