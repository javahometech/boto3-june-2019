import boto3

s3Client = boto3.client('s3')

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table('employees')

s3_resp = s3Client.get_object(
    Bucket='javahome-src',
    Key = 'employees.csv'
)

csv_file = s3_resp['Body'].read().decode('utf-8')
employees = csv_file.split('\r\n')
for emp in employees:
    print(emp)
    emp = emp.split(',')
    table.put_item(
        Item = {
            "emp_id": int(emp[0]),
            'name': emp[1],
            'location': emp[2],
            'salary': emp[3]
        }
    )