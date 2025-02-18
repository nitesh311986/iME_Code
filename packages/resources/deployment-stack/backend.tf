terraform {
  backend "s3" {
    bucket         = "terraform-state-365445763138-eu-central-1"
    key            = "ime-frontend-automated-tests.tfstate"
    region         = "eu-central-1"
    dynamodb_table = "terraform-state-lock-365445763138-eu-central-1"
  }
}