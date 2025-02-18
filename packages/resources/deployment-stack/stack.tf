locals {
  codebuild_name = "ime-frontend-automated-tests"
}

resource "aws_codebuild_project" "ime_frontend_automated_tests" {
  name          = local.codebuild_name
  description   = "CodeBuild to deploy and Run the Frontend Automated tests"
  build_timeout = 180
  service_role  = aws_iam_role.service_role.arn

  artifacts {
    type = "NO_ARTIFACTS"
  }
  cache {
    type = "NO_CACHE"
  }

  environment {
    compute_type                = "BUILD_GENERAL1_SMALL"
    image                       = "aws/codebuild/amazonlinux2-x86_64-standard:3.0"
    type                        = "LINUX_CONTAINER"
    image_pull_credentials_type = "CODEBUILD"

    environment_variable {
      name  = "STAGE"
      value = var.stage
    }
    environment_variable {
      name  = "REGION"
      value = var.region
    }
    environment_variable {
      name  = "TARGET_ACCOUNT_ID"
      value = data.aws_caller_identity.current.account_id
    }

    environment_variable {
      name  = "DOMAIN"
      value = "ime"
    }

     environment_variable {
      name  = "REPORTS_BUCKET"
      value = aws_s3_bucket.reports_bucket.bucket
    }
  }

  logs_config {
    cloudwatch_logs {}
  }

  source {
    type            = "GITHUB"
    location        = "https://github.com/ime-uk/frontend-automated-tests.git"
    git_clone_depth = 1
    git_submodules_config {
      fetch_submodules = false
    }
    report_build_status = true
  }
  source_version = "master"

  concurrent_build_limit = 1
  tags                   = local.tags
}

resource "aws_iam_policy" "code_build" {
  name        = "CodeBuildBasePolicy-${local.codebuild_name}-${data.aws_region.current.name}"
  path        = "/service-role/"
  description = "Policy used in trust relationship with CodeBuild"

  policy = jsonencode({
    Version : "2012-10-17",
    Statement : [
      {
        Effect : "Allow",
        Action : [
          "codeartifact:GetAuthorizationToken",
          "codeartifact:GetRepositoryEndpoint",
          "codeartifact:ReadFromRepository",
          "codeartifact:PublishPackageVersion"
        ],
        Resource : "*"
      },
      {
        Effect : "Allow",
        Action : "sts:GetServiceBearerToken",
        Resource : "*",
        Condition : {
          StringEquals : {
            "sts:AWSServiceName" : "codeartifact.amazonaws.com"
          }
        }
      },
       {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:ListBucket"
            ],
            "Resource": [
                "arn:aws:s3:::${aws_s3_bucket.reports_bucket.bucket}",
                "arn:aws:s3:::${aws_s3_bucket.reports_bucket.bucket}/*"
            ]
        }

    ]
  })
}

resource "aws_iam_role" "service_role" {
  name               = "Ime-Frontend-Automated-Tests-Role"
  assume_role_policy = data.aws_iam_policy_document.service_role_assume_role_policy.json
  managed_policy_arns = [
    "arn:aws:iam::aws:policy/AdministratorAccess",
    aws_iam_policy.code_build.arn
  ]
}

resource "aws_iam_role_policy" "service_role" {
  role   = aws_iam_role.service_role.name
  policy = data.aws_iam_policy_document.service_role_inline_policy.json
}

data "aws_iam_policy_document" "service_role_assume_role_policy" {
  version = "2012-10-17"
  statement {
    effect = "Allow"
    principals {
      type        = "Service"
      identifiers = ["codebuild.amazonaws.com"]
    }
    actions = ["sts:AssumeRole"]
  }
}

data "aws_iam_policy_document" "service_role_inline_policy" {
  version = "2012-10-17"
  statement {
    effect = "Allow"
    not_actions = [
      "organizations:*",
      "account:*"
    ]
    resources = ["*"]
  }
}

resource "aws_codebuild_webhook" "ime_frontend_automated_tests" {
  project_name = aws_codebuild_project.ime_frontend_automated_tests.name
  build_type   = "BUILD"
  filter_group {
    filter {
      type    = "EVENT"
      pattern = "PUSH"
    }

    filter {
      type    = "HEAD_REF"
      pattern = "master"
    }
  }

  filter_group {
    filter {
      type    = "EVENT"
      pattern = "PUSH"
    }

    filter {
      type    = "HEAD_REF"
      pattern = "staging"
    }
  }
}

output "build_project_name" {
  value = aws_codebuild_project.ime_frontend_automated_tests.name
}

