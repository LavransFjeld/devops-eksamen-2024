resource "aws_lambda_function" "sqs_handler" {
  filename         = "image_processor_lambda_30.zip"
  function_name    = "process-sqs-messages"
  role             = aws_iam_role.lambda_execution_role.arn
  handler          = "image_processor_lambda_30.lambda_handler"
  runtime          = "python3.9"
  timeout          = 30
  source_code_hash = filebase64sha256("image_processor_lambda_30.zip")

  environment {
    variables = {
      BUCKET_NAME = "pgr301-couch-explorers"
    }
  }
}

# Grant Lambda access to trigger from SQS
resource "aws_lambda_event_source_mapping" "sqs_event_source" {
  event_source_arn = aws_sqs_queue.image_processing_queue.arn
  function_name    = aws_lambda_function.image_processor_lambda.arn
  batch_size       = 10
  enabled          = true
}
