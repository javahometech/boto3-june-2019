import boto3
import json

s3Client = boto3.client('s3')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

s3_resp = s3Client.get_object(
    Bucket='javahome-src',
    Key = 'employees.json'
)

json_file_str = s3_resp['Body'].read().decode('utf-8')

employees = json.loads(json_file_str)

for emp in employees:
    print(emp)

    table.put_item(
        Item = {
            "emp_id": int(emp['emp_id']),
            'name': emp['name'],
            'location': emp['location'],
            'salary': emp['salary']
        }
    )