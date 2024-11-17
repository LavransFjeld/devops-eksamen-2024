from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.utilities.typing import LambdaContext
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools import Logger, Tracer, Metrics
from aws_lambda_powertools.metrics import MetricUnit
from generate_image import generate_image_from_prompt
import json
import boto3
import os

app = APIGatewayRestResolver()
tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")

# Set up the S3 client
s3_client = boto3.client('s3')

# Remove the hello endpoint
# Add only the /generate_image endpoint
@app.post("/generate_image")
@tracer.capture_method
def generate_image():
    # Parse the prompt from the JSON body of the request
    try:
        body = app.current_event.json_body
        prompt = body.get('prompt')
        candidate_number = "30"
        logger.info(f"Received request body: {body}")
    
        # Check if prompt was provided
        if not prompt:
            logger.error("No prompt provided in the request")
            return {"statusCode": 400, "body": json.dumps({"error": "Prompt is required"})}
    
        # Generate the image (use the function from generate_image.py)
        logger.info("Calling generate_image_from_prompt with prompt")
        image_data = generate_image_from_prompt(prompt)
        logger.info("Image generated successfully")
    
        # Define S3 bucket and file path
        
        bucket_name = os.environ['BUCKET_NAME']
        
        if not bucket_name:
            logger.error("BUCKET_NAME environment variable is missing")
            return {"statusCode": 500, "body": json.dumps({"error": "S3 bucket name not set"})}
    
        
        file_path = f"{candidate_number}/{prompt}.png"
        logger.info(f"Uploading image to bucket: {bucket_name}, path: {file_path}")
    
        # Upload image to S3
        try:
            s3_client.put_object(Bucket=bucket_name, Key=file_path, Body=image_data)
            logger.info(f"Image uploaded successfully to s3://{bucket_name}/{file_path}")
            return {"statusCode": 200, "body": json.dumps({"message": "Image generated and saved to S3"})}
        except Exception as e:
            logger.error(f"Error uploading image to S3: {str(e)}")
            return {"statusCode": 500, "body": json.dumps({"error": "Failed to upload image to S3"})}
    
    except Exception as e:
        logger.error(f"Unhandled exception in generate_image function: {str(e)}")
        return {"statusCode": 500, "body": json.dumps({"error": "Failed to process request"})}

# Main Lambda handler
@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
@metrics.log_metrics(capture_cold_start_metric=True)
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
