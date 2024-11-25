resource "aws_sns_topic" "sqs_delay_alarm_topic" {
  name = "Cand30-sqs_delay_alarm_topic"
}

resource "aws_sns_topic_subscription" "email_subscription" {
  topic_arn = aws_sns_topic.sqs_delay_alarm_topic.arn
  protocol  = "email"
  endpoint  = var.alarm_email
}

resource "aws_cloudwatch_metric_alarm" "sqs_age_alarm" {
  alarm_name          = "Cand30-MessageAgeTooHigh"
  comparison_operator = "GreaterThanThreshold"
  evaluation_periods  = 1
  metric_name         = "ApproximateAgeOfOldestMessage"
  namespace           = "AWS/SQS"
  period              = 60
  statistic           = "Maximum"
  threshold           = var.alarm_threshold

  dimensions = {
    QueueName = aws_sqs_queue.image_processing_queue.name
  }

  alarm_actions = [aws_sns_topic.sqs_delay_alarm_topic.arn]
}