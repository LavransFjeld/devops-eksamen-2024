provider "aws" {
  region = var.aws_region
}

resource "aws_sqs_queue" "image_processing_queue" {
  name                      = var.sqs_queue_name
  visibility_timeout_seconds = 30
  delay_seconds             = 0
  message_retention_seconds = 86400
}

resource "aws_lambda_function" "image_processor_lambda" {
  function_name    = var.lambda_function_name
  s3_bucket        = var.s3_bucket
  s3_key           = "lambda_sqs.zip"
  handler          = "lambda_function.lambda_handler"
  runtime          = "python3.9"
  timeout          = 30
  memory_size      = 128
  role             = aws_iam_role.lambda_execution_role.arn

  environment {
    variables = {
      SQS_QUEUE_URL = aws_sqs_queue.image_processing_queue.id
      BUCKET_NAME   = var.s3_bucket
    }
  }
}
