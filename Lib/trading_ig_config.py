import os

class config(object):
    username = os.environ['IG_SERVICE_USERNAME']
    password = os.environ['IG_SERVICE_PASSWORD']
    api_key = os.environ['IG_SERVICE_API_KEY']
    acc_number = os.environ['IG_SERVICE_ACC_NUMBER']
    acc_type = "DEMO"

