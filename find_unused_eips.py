import boto3

client = boto3.client('ec2')

eips_resp = client.describe_addresses()
unused_eips = set()
for address in eips_resp["Addresses"]:
    if 'InstanceId' not in address:
        unused_eips.add(address['AllocationId'])

print(unused_eips)

