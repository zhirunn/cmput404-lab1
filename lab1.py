import requests

response = requests.get('https://raw.githubusercontent.com/zhirunn/cmput404-lab1/master/lab1.py')
print (response.text)
