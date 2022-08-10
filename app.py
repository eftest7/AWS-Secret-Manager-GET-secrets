import boto3 
import json 

client = boto3.client('secretsmanager')

response = client.get_secret_value(
    SecretId='test003'
)

database_secrets = json.loads(response['SecretString'])


print("----------------------")
print(database_secrets)
print("----------------------")
#print(database_secrets['APIKey'])
#print(database_secrets['biUsername'])
print(database_secrets['test003'])
