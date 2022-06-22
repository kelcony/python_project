# import from aws library
import boto3

# specifying region
region = "eu-west-2"

# aws console up running

session = boto3.Session()

# avaliable resources from aws account
avaliable_resources = session.get_avaliable_resources()
print(avaliable_resources)

print("list of avavliable resources from my aws accoun")
for resources in avaliable_resources:
    print(resources)







