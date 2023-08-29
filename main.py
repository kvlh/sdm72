import sdm_modbus
import boto3
import requests
import time
import os
from dotenv import load_dotenv

number_of_devices=3
devices=[]

def import_env():
    load_dotenv()
    global aws_access_key_id 
    aws_access_key_id = os.getenv('aws_access_key_id')
    global aws_secret_access_key 
    aws_secret_access_key = os.getenv('aws_secret_access_key')

def cnd(number_of_devices):
  for i in range(1,1+number_of_devices):
      try:
          devices[i] = sdm_modbus.SDM72(devices="/dev/ttyUSB0", baud=9600, unit=i)
          devices[i].connected()
      except:
          print("error on device: " + str(i))
     
  return devices
def cn_db():
  client = boto3.client('dynamodb',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='eu-central-1')

  dynamodb = boto3.resource('dynamodb',aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key, region_name='eu-central-1')
  ddb_exceptions = client.exceptions
  # r = dynamodb.T
  response = dynamodb.Table('sdm72').scan()
  for i in response['Items']:
      print(i)

import_env()
devices=cnd(number_of_devices)
cn_db()