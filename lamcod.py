import os
import json
import boto3
import base64
import gzip

s3 = boto3.client('s3')
S3_BUCKET = os.getenv("S3_BUCKET", "pdff1-tkr")

def lambda_handler(event, context):
    try:
        print("received event:", json.dumps(event, indent=4))
        if "awslogs" not in event:
            print("aws logs not found")
            return {"statusCode": 400, "body": "Invalid event format"}
        log_data = event['awslogs']['data']
        decoded_data = gzip.decompress(base64.b64decode(log_data)).decode('utf-8')
        log_events = json.loads(decoded_data)
        print("decoded event logs: ", json.dumps(log_events, indent=4))
        s3_key = f"logs/{context.aws_request_id}.json"
        s3.put_object(Bucket=S3_BUCKET, Key=s3_key, Body=json.dumps(log_events, indent=4))
        return {"statusCode": 200, "body": f"403 error log uploaded to {s3_key}"}
    except Exception as e:
        print(f"Error processing Logs{str(e)}")
        return {"statusCode": 500, "body": f"Error: {str(e)}"}

        

