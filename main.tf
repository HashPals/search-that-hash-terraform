# Provisions a dynamoDB
resource "aws_dynamodb_table" "basic-dynamodb-table" {
  name           = "hash_lookup"
  billing_mode   = "PROVISIONED"
  read_capacity  = 20
  write_capacity = 20
  hash_key       = "Hash"

  attribute {
    name = "Hash"
    type = "S"
  }


  tags = {
    Name        = "dynamodb-table-1"
    Environment = "production"
  }
}