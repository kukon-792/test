##create ec2 instance
import boto3

client = boto3.client('ec2')
response = client.run_instances(
    ImageId='ami-00eeedc4036573551', # from amazon linux
    InstanceType='t2.micro',
    MinCount=1,
    MaxCount=1,
    KeyName='CustomVPC'
)
print(response)
for instance in response['Instances']:
    print("Instance ID created is : {} Instance Type is :{}".format(instance['Instance_Id'],instance['InstanceType']))
