resource "aws_lambda_function" "sqs_handler" {
  filename         = "lambda_sqs.zip"
  function_name    = "process-sqs-messages"
  role             = aws_iam_role.lambda_execution_role.arn
  handler          = "lambda_sqs.lambda_handler"
  runtime          = "python3.9"
  timeout          = 30
  source_code_hash = filebase64sha256("lambda_sqs.zip")

  environment {
    variables = {
      BUCKET_NAME = var.s3_bucket
      CANDIDATE_NUMBER = var.candidate_number
    }
  }
}

# Grant Lambda access to trigger from SQS
resource "aws_lambda_event_source_mapping" "sqs_event_source" {
  event_source_arn = aws_sqs_queue.image_processing_queue.arn
  function_name = aws_lambda_function.sqs_handler.arn
  batch_size       = 10
  enabled          = true
}
