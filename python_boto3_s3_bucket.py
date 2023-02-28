
# ## How to verify how many bucket on the aws s3
# import boto3
#
# client = boto3.client('s3')
# response = client.list_buckets()
# for name in response['Buckets']:
#     print(name['Name'])
#
# ## How to delete s3 bucket
# import boto3
#
# client = boto3.client('s3')
# response = client.delete_bucket(
#     Bucket='kukon-bucket105',
# )
#
# print(response)

# ### How to delete object file from s3 bucket
# import boto3
# client = boto3.client('s3')
# client.delete_object(Bucket='kukon-bucket105', key='kukon.txt')

# # ## How to delete s3 object file
# import boto3
# s3_resource = boto3.client('s3')
# s3_resource.delete_object(Bucket='kukon-bucket105', Key='kukon.txt')

# ## How to create s3bucket
# import boto3
# s3 = boto3.client('s3')
# s3.create_bucket(Bucket='kukon-bucket105',
#     CreateBucketConfiguration={'LocationConstraint': 'us-east-2'})

# # how to create s3 bucket
# import boto3
#
# aws_resource = boto3.resource("s3")
# bucket = aws_resource.Bucket("kukons3")
# response = bucket.create(
#     ACL='public-read',
#     CreateBucketConfiguration={
#         'LocationConstraint': 'us-east-2'
#     },
#
# )
#
# ## How to uploads a file into s3 bucket
# import boto3
# s3 = boto3.resource('s3')
# s3.meta.client.upload_file(r'C:\Users\kukon\OneDrive\Desktop\sample.txt', 'kukon-bucket105', 'kukon.txt')

#
# ## How to delete multyple file from s3 bucket
# import boto3
# import os
# s3_resource = boto3.client('s3')
# objects=s3_resource.list_objects(Bucket="kukons3")["Contents"]
# len(objects)
# for object in objects:
#     s3_resource.delete_object(Bucket="kukons3", Key=object["Key"])
#
# ## How to delete multyple file from s3 bucket
# import boto3
# import os
# s3_resource = boto3.client('s3')
# objects=s3_resource.list_objects(Bucket="kukons3")["Contents"]
# len(objects)
# for object in objects:
#     s3_resource.delete_object(Bucket="kukons3", Key=object["Key"])
#     print(objects)


### how to delete s3 bucket
# import boto3
#
# client = boto3.client('s3')
# response = client.delete_bucket(
#     Bucket='kukon-bucket105',
# )
# print(response)
