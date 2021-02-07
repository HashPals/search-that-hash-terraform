# https://www.terraform.io/downloads.html

provider "aws" {
    region = "us-east-2"
}

resource "aws_s3_bucket" "S3Bucket" {
    bucket = "data-search-that-hash"
}

resource "aws_s3_bucket" "S3Bucket2" {
    bucket = "serverless-s3-dynamo"
}

resource "aws_s3_bucket" "S3Bucket3" {
    bucket = "wordlists-utf8"
}

resource "aws_lambda_function" "LambdaFunction" {
    description = ""
    function_name = "PutItemsIntoDynamo"
    handler = "lambda_function.lambda_handler"
    s3_bucket = "awslambda-us-east-2-tasks"
    s3_key = "/snapshots/268217122302/PutItemsIntoDynamo-7b84e597-cca2-484a-98ff-6116063f9fee"
    s3_object_version = "xC2YM0RgnEz5kNiVISNDNOrY4XQj.n21"
    memory_size = 128
    role = "arn:aws:iam::268217122302:role/sth"
    runtime = "python3.8"
    timeout = 3
    tracing_config {
        mode = "PassThrough"
    }
}

resource "aws_lambda_function" "LambdaFunction2" {
    description = ""
    function_name = "hash_lookup"
    handler = "lambda_function.A"
    s3_bucket = "awslambda-us-east-2-tasks"
    s3_key = "/snapshots/268217122302/hash_lookup-c6a00c74-81cd-4f9c-9c22-23e19fbbddc0"
    s3_object_version = "Wfl3g8ru0P5EuqgCskySy0VTn6u7jd7u"
    memory_size = 512
    role = "arn:aws:iam::268217122302:role/sth"
    runtime = "python3.8"
    timeout = 3
    tracing_config {
        mode = "PassThrough"
    }
}

resource "aws_lambda_function" "LambdaFunction3" {
    description = ""
    function_name = "s3_to_dynamo"
    handler = "sth_s3_to_dynamo.lambda_handler"
    s3_bucket = "awslambda-us-east-2-tasks"
    s3_key = "/snapshots/268217122302/s3_to_dynamo-96aef0ec-f5db-40b3-96ae-5f5a607fbc3b"
    s3_object_version = "ut.u6SmGsJ2i0j0oesPbATrCeg2ZRjLe"
    memory_size = 1324
    role = "arn:aws:iam::268217122302:role/sth"
    runtime = "python3.8"
    timeout = 60
    tracing_config {
        mode = "PassThrough"
    }
}

resource "aws_dynamodb_table" "DynamoDBTable" {
    attribute {
        name = "Hash"
        type = "S"
    }
    name = "hash_lookup"
    hash_key = "Hash"
    read_capacity = 5
    write_capacity = 5
}
