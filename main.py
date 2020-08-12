#!/usr/bin/python3
from azure.devops.connection import Connection
from azure.devops.credentials import BasicAuthentication
from  azure.devops.v5_1.work_item_tracking.models import JsonPatchOperation
from azure.devops.v5_1.work_item_tracking.models import Comment
from azure.devops.v5_1.work_item_tracking.models import CommentCreate

import pprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--buildid', required=True)
parser.add_argument('--token', required=True)
parser.add_argument('--comment', required=True)
parser.add_argument('--org', required=True)
parser.add_argument('--proj', required=True)

args = parser.parse_args()


# credentials = BasicAuthentication('', args.token)
credentials=BasicAuthentication('PAT', args.token)
connection = Connection(base_url=args.org, creds=credentials)

build_client = connection.clients_v5_1.get_build_client()
wis = build_client.get_build_work_items_refs(project=args.proj, build_id=args.buildid)
# wis = build_client.get_build_work_items_refs(project="Biology Editor", build_id=4388)

wit_5_1_client = connection.clients_v5_1.get_work_item_tracking_client()


for wi in wis:
    pprint.pprint(wi.id)
    wit_5_1_client.add_comment(project=args.proj,work_item_id=str(wi.id),request=CommentCreate(text=args.comment))
   
 
    
