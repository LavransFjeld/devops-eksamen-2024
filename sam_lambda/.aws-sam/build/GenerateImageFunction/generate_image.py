import base64
import boto3
import json
import random

bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

def generate_image_from_prompt(prompt):
    seed = random.randint(0, 2147483647)
    native_request = {
        "taskType": "TEXT_IMAGE",
        "textToImageParams": {"text": prompt},
        "imageGenerationConfig": {
            "numberOfImages": 1,
            "quality": "standard",
            "cfgScale": 8.0,
            "height": 1024,
            "width": 1024,
            "seed": seed,
        }
    }

    response = bedrock_client.invoke_model(modelId="amazon.titan-image-generator-v1", body=json.dumps(native_request))
    model_response = json.loads(response["body"].read())

    # Decode the base64 image
    base64_image_data = model_response["images"][0]
    return base64.b64decode(base64_image_data)