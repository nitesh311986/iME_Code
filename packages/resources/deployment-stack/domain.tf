locals {
  api_domain = "api.testing.${local.domain}"
}

resource "aws_acm_certificate" "automated_tests_service_acm" {
  domain_name       = local.api_domain
  validation_method = "DNS"
}

resource "aws_route53_record" "automated_tests_service_acm" {
  for_each = {
    for dvo in aws_acm_certificate.automated_tests_service_acm.domain_validation_options : dvo.domain_name => {
      name   = dvo.resource_record_name
      record = dvo.resource_record_value
      type   = dvo.resource_record_type
    }
  }

  allow_overwrite = true
  name            = each.value.name
  records         = [each.value.record]
  ttl             = 60
  type            = each.value.type
  zone_id         = data.aws_route53_zone.selected.zone_id

}

resource "aws_acm_certificate_validation" "automated_tests_service_acm" {
  certificate_arn         = aws_acm_certificate.automated_tests_service_acm.arn
  validation_record_fqdns = [for record in aws_route53_record.automated_tests_service_acm : record.fqdn]

}

output "automated_tests_service_acm_arn" {
  value = aws_acm_certificate.automated_tests_service_acm.arn
}

output "automated_tests_service_domain" {
  value = local.api_domain
}

output "automated_tests_service_hosted_zone_id" {
  value = data.aws_route53_zone.selected.zone_id
}
