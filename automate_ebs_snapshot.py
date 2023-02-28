## Automate aws EBS SNAPSHOTS and NOTIFY via EMAIL by using python boto3 script
# import boto3
#
# ec2 = boto3.resource('ec2')
# tagfilter = [
#         {
#             'Name': 'tag:Env',
#             'Values': ['Production']
#         }
#     ]
# snapshot_list=[] # empty list
#
# for instance in ec2.instances.filter(Filters=tagfilter):
#     print(instance.instance_id)

## How to create volume ID on ec2 instance?
# import boto3
#
# ec2 = boto3.resource('ec2')
# tagfilter = [
#         {
#             'Name': 'tag:Env',
#             'Values': ['Production']
#         }
#     ]
# snapshot_list=[] # empty list
#
# for instance in ec2.instances.filter(Filters=tagfilter):
#     for volume in instance.volumes.all():
#         print(volume.volume_id)

# ## ## How to create a snapshot  on an ec2 instance?
#
# import boto3
#
# ec2 = boto3.resource('ec2')
# tagfilter = [
#         {
#             'Name': 'tag:Env',
#             'Values': ['Production']
#         }
#     ]
# snapshot_list=[] # empty list
#
# for instance in ec2.instances.filter(Filters=tagfilter):
#
#     for volume in instance.volumes.all():
#         snapshot=volume.create_snapshot(Description='Snapshot created via boto3')
#         snapshot_list.append(snapshot.snapshot_id)
#         print(snapshot_list)

## How to create a snapshot on an UAT ec2 instance?
# import boto3
#
# ec2 = boto3.resource('ec2')
# tagfilter = [
#         {
#             'Name': 'tag:Env',
#             'Values': ['UAT']
#         }
#     ]
# snapshot_list=[] # empty list
#
# for instance in ec2.instances.filter(Filters=tagfilter):
#     print(instance.instance_id)
#     for volume in instance.volumes.all():
#         snapshot=volume.create_snapshot(Description='Snapshot created via boto3')
#         snapshot_list.append(snapshot.snapshot_id)
#         print(snapshot_list)

# # How to create a snapshot on an UAT ec2 instance?
# import boto3
#
# ec2 = boto3.resource('ec2')
# client = boto3.client('sns')
# tagfilter = [
#         {
#             'Name': 'tag:Env',
#             'Values': ['Production']
#         }
#     ]
# snapshot_list=[] # empty list
#
# for instance in ec2.instances.filter(Filters=tagfilter):
#     print(instance.instance_id)
#     for volume in instance.volumes.all():
#         snapshot=volume.create_snapshot(Description='Snapshot created via boto3')
#         snapshot_list.append(snapshot.snapshot_id)
#         print(snapshot_list)
#
# sns_client.publish(
#     TopicArn='arn:aws:sns:us-east-1:o45728217032:notify-snapshot-creation'
#     Subject= 'EBS-Snapshots-Boto3',
#     Message=str(snapshot_list)
# )

# # How to create a snapshot on an UAT & DEV ec2 instance?
# import boto3
#
# ec2 = boto3.resource('ec2')
# client = boto3.client('sns')
# tagfilter = [
#         {
#             'Name': 'tag:Env',
#             'Values': ['UAT']
#         }
#         {
#             'Name': 'tag:Env',
#             'Values': ['DEV']
#         }
#     ]
# snapshot_list = []  # empty list
#
# for instance in ec2.instances.filter(Filters=tagfilter):
#     print(instance.instance_id)
#     for volume in instance.volumes.all():
#         snapshot = volume.create_snapshot(Description='Snapshot created via Both')
#         snapshot_list.append(snapshot.snapshot_id)
#         print(snapshot_list)
#
# sns_client.publish(
#     TopicArn='arn:aws:sns:us-east-1:o45728217032:notify-snapshot-creation'
#     Subject = 'EBS-Snapshots-Boto3',
#     Message = str(snapshot_list)
# )

# ## Automate EBS Snapshot Deletion For Orphan Snapshot
# from datetime import datetime,timedelta, timezone
# import boto3
# ec2 = boto3.resource('ec2')
# tagfilter=[
#         {
#             'Key': 'tag:Env',
#             'Value': ['Production']
#     }
# ]
# snapshots = ec2.snapshots.filter(Filter=tagfilter)
# print(snapshots)

# ## Automate EBS Snapshot Deletion For Orphan Snapshot
# from datetime import datetime,timedelta, timezone
# import boto3
# ec2 = boto3.resource('ec2')
# tagfilter=[
#         {
#             'Key': 'tag:Env',
#             'Value': ['Production']
#     }
# ]
# snapshots = ec2.snapshots.filter(Filters=tagfilter)
# print(snapshots)
#
# for snapshot in snapshots:
#     create_time=snapshots.start_time
#     #delete_time=datetime.now(tz=timezone.utc) - timedelta(minutes=360)
#     delete_time = datetime.now(tz=timezone.utc) - timedelta(minutes=1)
#     #delete_time = datetime.now(tz=timezone.utc) - timedelta(days=10)
#     if delete_time > create_time:
#         print('Create time of snapshot is {} And Delete time of snapshot is {}'.format(create_time,delete_time))
#     else:
#         print('Existing snapshot {} is not less than 1 minute old'.format(snapshot.snapshot_id))

# ## Automate EBS Snapshot Deletion For Orphan Snapshot
# from datetime import datetime,timedelta, timezone
# import boto3
# ec2 = boto3.resource('ec2')
# tagfilter=[
#         {
#             'Key': 'tag:Env',
#             'Value': ['Production']
#     }
# ]
# snapshots = ec2.snapshots.filter(Filters=tagfilter)
# print(snapshots)
#
# for snapshot in snapshots:
#     create_time=snapshots.start_time
#
#     delete_time = datetime.now(tz=timezone.utc) - timedelta(minutes=1)
#
#     if delete_time > create_time:
#         snapshot.delete()
#         print('{} has been delete'.format(snapshot.snapshot_id))
#     else:
#         print('Existing snapshot {} is not less than 1 minute old'.format(snapshot.snapshot_id))