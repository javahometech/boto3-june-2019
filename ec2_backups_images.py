import boto3

client = boto3.client('ec2')

# Get instance in Production environment

instances_resp = client.describe_instances(
    Filters = [
        {
            "Name" : "tag:Env",
            "Values" : ["Prod"]
        }
    ]
)

for reservation in instances_resp['Reservations']:
    for instance in reservation['Instances']:
        print(instance['InstanceId'])
        # Take backups
        try:
            client.create_image(
                InstanceId=instance['InstanceId'],
                Name="JavahomeImage-" + instance['InstanceId'],
                Description="boto3-JavahomeImage-" + instance['InstanceId']
            )
        except:
            pass
