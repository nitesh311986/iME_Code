data "aws_ssm_parameter" "reports_slack_webhook" {
  name            = "/cicd/automated_tests_slack_webhook"
  with_decryption = true

}

output "reports_slack_webhook" {
  value = data.aws_ssm_parameter.reports_slack_webhook.value
  sensitive = true
}