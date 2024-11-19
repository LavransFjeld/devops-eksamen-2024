variable "aws_region" {
  description = "AWS region to deploy resources in"
  type        = string
  default     = "eu-west-1"
}

variable "candidate_number" {
  description = "Candidate number to ensure unique resource naming"
  type        = string
  default     = "30"
}

variable "s3_bucket" {
  description = "S3 bucket to store Lambda deployment packages"
  type        = string
  default     = "pgr301-couch-explorers"
}

variable "sqs_queue_name" {
  description = "Name of the SQS queue for image processing"
  type        = string
  default     = "image-processing-queue-30"
}

variable "lambda_role_name" {
  description = "IAM role name for the Lambda function"
  type        = string
  default     = "lambda_execution_role_30"
}

variable "lambda_function_name" {
  description = "Name of the Lambda function"
  type        = string
  default     = "image_processor_lambda_30"
}

variable "alarm_email" {
  description = "Email address for CloudWatch alarm notifications"
  type        = string
  default = "cand30@gmail.com"
}

variable "alarm_threshold" {
  description = "Threshold for ApproximateAgeOfOldestMessage in seconds"
  default     = 60
}
