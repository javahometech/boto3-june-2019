import boto3

client = boto3.client('ec2')
sns = boto3.client('sns')

eips_resp = client.describe_addresses()
unused_eips = set()
for address in eips_resp["Addresses"]:
    if 'InstanceId' not in address:
        unused_eips.add(address['AllocationId'])

print(unused_eips)

# Delete EIPS

for allocationid in unused_eips:
    response = client.release_address(
        AllocationId=allocationid,
        DryRun = False
    )

# If you have unused eips send mail alert

if unused_eips:
    sns.publish(
        TopicArn = "arn:aws:sns:ap-south-1:797415129573:dynamodb",
        Subject = "Unused EIPs Found and Released",
        Message = str(unused_eips)
    )




