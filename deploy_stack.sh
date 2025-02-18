#!/bin/bash

# Set default values for optional arguments
# Use at own risk, open to suggestions for later improvement
DEPLOYMENT_TOOL=""
ROOT_DIR=$(/bin/pwd)
echo $ROOT_DIR
# Define usage message
usage() {
  echo "Usage: deploy.sh [--deploy <serverless|terraform>]"
  exit 1
}

# Parse arguments
while [[ "$#" -gt 0 ]]; do
  case $1 in
  --deploy)
    DEPLOYMENT_TOOL="$2"
    shift
    ;;
  *) usage ;;
  esac
  shift
done

# Check if stage argument is provided
if [ -z "$DEPLOYMENT_TOOL" ]; then
  usage
fi

# Deploy infrastructure using the specified deployment tool
if [ "$DEPLOYMENT_TOOL" = "terraform" ]; then
  cd $ROOT_DIR
  echo "Deploying infrastructure using Terraform for stage $STAGE"
  cd packages/resources/deployment-stack
  terraform init
  terraform apply -input=false
  terraform output -json >../../service/webhooks/resources/terraform.json

fi

if [ "$DEPLOYMENT_TOOL" = "serverless" ]; then
  echo "Deploying webhooks using Serverless framework"

  cd $ROOT_DIR
  cd packages/resources/deployment-stack
  echo "Outputing infrastructure variables using Terraform"
  terraform init
  terraform output -json >../../service/webhooks/resources/terraform.json

  cd $ROOT_DIR
  cd packages/service/webhooks
  aws codeartifact login --tool pip --domain ime --domain-owner 365445763138 --repository tools
  serverless deploy --region eu-central-1
fi