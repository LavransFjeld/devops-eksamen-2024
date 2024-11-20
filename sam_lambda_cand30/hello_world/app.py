import base64
import boto3
import json
import random
import os

# Set up the AWS clients
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")
s3_client = boto3.client("s3")

MODEL_ID = "amazon.titan-image-generator-v1"
BUCKET_NAME = os.environ["BUCKET_NAME"]

def lambda_handler(event, context):
    print("Event received:", event)
    
    # Extract the POST request body
    body = json.loads(event["body"])
    prompt = body.get("prompt", "Default prompt if none provided")

    if not prompt:
        return {
            "statusCode": 400,
            "body": json.dumps({"error": "No prompt provided"})
        }

    seed = random.randint(0, 2147483647)
    s3_image_path = f"titan_{seed}.png"

    candidate_number = os.environ["CANDIDATE_NUMBER"]
    file_key = f"{candidate_number}/{s3_image_path}"
    
    # Prepare the request for the Bedrock model
    native_request = {
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {"text": prompt},
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "quality": "standard",
            "cfgScale": 8.0,
            "height": 512,
            "width": 512,
            "seed": seed,
        },
    }

    try:
        # Invoke the Bedrock model
        response = bedrock_client.invoke_model(
            modelId=MODEL_ID,
            body=json.dumps(native_request)
        )
        model_response = json.loads(response["body"].read())
        
        # Extract and decode the Base64 image data
        base64_image_data = model_response["images"][0]
        image_data = base64.b64decode(base64_image_data)
        
        # Upload the image to S3
        s3_client.put_object(Bucket=BUCKET_NAME, Key=file_key, Body=image_data)
        
        # Return the S3 path of the generated image
        return {
            "statusCode": 200,
            "body": json.dumps({
                "message": "Image generated successfully",
                "s3_image_path": f"s3://{BUCKET_NAME}/{file_key}"
            })
        }
    except Exception as e:
        print(f"Error: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps({"error": "Failed to process request"})
        }
