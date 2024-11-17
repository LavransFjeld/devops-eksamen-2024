terraform {
  required_version = ">= 1.9.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "5.74.0"
    }
  }
  backend "s3" {
    bucket         = "pgr301-2024-terraform-state"
    key            = "infra/terraform.tfstate"
    region         = "eu-west-1"
  }
}

resource "aws_sqs_queue" "image_processing_queue" {
  name                      = "image-processing-queue-30"
  visibility_timeout_seconds = 30 # Time for message lock to prevent reprocessing
  delay_seconds             = 0
  message_retention_seconds = 86400 # 1 day retention
}


provider "aws" {
  region = "eu-west-1"
}
