import boto3
import yaml

with open('vars.yml', 'r', encoding='utf-8') as fp:
    data = yaml.safe_load(fp)

ubuntu_img_id = data['ubuntu_img_id']
awsLinux_img_id = data['awsLinux_img_id']

client = boto3.client('ec2')

response = client.describe_instances(
    Filters=[{
        'Name': 'instance-state-name',
        'Values': ['running']
    }]
)

with open('inventory.ini', 'w') as fp:
    for instance in response['Reservations']:
        image_id, public_ip = instance['Instances'][0]['ImageId'], instance['Instances'][0]['PublicIpAddress']
    
        if image_id == ubuntu_img_id:
            user = 'ubuntu'
        elif image_id == awsLinux_img_id:
            user = 'ec2-user'
        
        fp.write(f'{user}@{public_ip}\n')
    

    


