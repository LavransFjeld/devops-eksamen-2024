import json
import boto3
import os

s3_client = boto3.client('s3')

def lambda_handler(event, context):
    for record in event['Records']:
        body = json.loads(record['body'])
        prompt = body.get('prompt')

        if not prompt:
            print("No prompt provided, skipping...")
            continue

        # Simulate image processing logic
        image_data = f"Image data for prompt: {prompt}".encode('utf-8')

        # Upload the processed "image" to S3
        bucket_name = os.environ['BUCKET_NAME']
        file_path = f"{prompt}.txt"  # Simulating text files for images

        s3_client.put_object(Bucket=bucket_name, Key=file_path, Body=image_data)
        print(f"Uploaded {file_path} to {bucket_name}")

    return {"statusCode": 200, "body": "Messages processed"}
