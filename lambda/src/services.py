import boto3;
from logger.loggerFunction import getLogger, addTranscationId;

client = boto3.resource('dynamodb');
db_table = client.Table('job-test')
logger = getLogger();


def get_job(job_id):
    try:
        response = db_table.get_item(Key={'id': job_id})
        return response["Item"]
    except Exception as e:
        raise e
