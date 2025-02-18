terraform {
  required_providers {
       aws = {
      source  = "hashicorp/aws"
      version = "5.14.0"
    }

    github = {
      source = "integrations/github"
    }
  }
  required_version = "1.2.7"
}

provider "aws" {
  region = var.region
}

data "aws_caller_identity" "current" {}
data "aws_region" "current" {}
data "aws_route53_zone" "selected" {
  name = local.domain
}