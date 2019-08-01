import boto3

from botocore.exceptions import NoCredentialsError, ClientError


#
# Author: U4ZX
# Date: 01/08/2019
#


def upload_file(file_name, ACCESS_KEY, SECRET_KEY, bucket, object_name=None):
    """Upload a file to an S3 bucket

    https://boto3.amazonaws.com/v1/documentation/api/latest/guide/s3-uploading-files.html

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    if object_name is None:
        object_name = file_name


    client = boto3.client('s3',  aws_access_key_id=ACCESS_KEY,
         aws_secret_access_key= SECRET_KEY)
    # Upload the file
    try:
        response = client.upload_file(file_name, bucket, object_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True


