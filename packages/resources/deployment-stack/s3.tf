resource "aws_s3_bucket" "reports_bucket" {
  bucket = "ime-test-reports-${var.region}"

  tags = {
    Name        = "${var.service}-bucket-${var.region}"
  }
}

#resource "aws_s3_bucket_acl" "reports_acl" {
#  bucket = aws_s3_bucket.reports_bucket.id
#  acl    = "public-read"
#}
#
#resource "aws_s3_bucket_policy" "bucket_policy" {
#  bucket = aws_s3_bucket.reports_bucket.id
#
#  policy = jsonencode({
#    Version = "2012-10-17",
#    Statement = [
#      {
#        Sid       = "PublicReadGetObject",
#        Effect    = "Allow",
#        Principal = "*",
#        Action    = ["s3:GetObject"],
#        Resource  = ["arn:aws:s3:::${aws_s3_bucket.reports_bucket.id}/*"]
#      }
#    ]
#  })
#}

resource "aws_s3_bucket_public_access_block" "block" {
  bucket = aws_s3_bucket.reports_bucket.id

  block_public_acls       = false  # Do not block public ACLs
  block_public_policy     = false  # Do not block public bucket policies
  ignore_public_acls      = false  # Do not ignore public ACLs
  restrict_public_buckets = false  # Do not restrict public buckets
}

output "reports_bucket_arn" {
  value       = aws_s3_bucket.reports_bucket.arn
  description = "The Amazon Resource Number of the S3 bucket"
}

output "reports_bucket_name" {
  value       = aws_s3_bucket.reports_bucket.bucket
  description = "The Amazon Resource Number of the S3 bucket"
}