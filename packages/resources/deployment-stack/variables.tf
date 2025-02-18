locals {
  tags = merge(var.tags,
    {
      Terraform = true
      Service   = var.service
      Stage     = var.stage
      CreatedBy = var.created_by
  })
 domain          = "tools.aws.interviewme.tech"

}
variable "region" {
  type        = string
  description = "AWS region to deploy to"
  default     = "eu-central-1"
}

variable "second_region" {
  type        = string
  description = "Secondary deploy region"
  default     = "us-west-2"
}

variable "service" {
  type        = string
  default     = "ime-frontend-automated-tests"
  description = "Service name, common accross Terraform and Serverless"
}

variable "stage" {
  type        = string
  default     = "staging"
  description = "The stage to deploy: dev, staging, uat, prod"

  validation {
    condition     = can(regex("staging|uat", var.stage))
    error_message = "The stage value must be a valid stage: dev, staging, uat, prod."
  }
}


variable "created_by" {
  type        = string
  description = "Company or vendor name followed by the username part of the email address "
  default     = "pipeline"
}

variable "tags" {
  type        = map(string)
  description = "Key/Value pairs of default tags"
  default     = {}
}