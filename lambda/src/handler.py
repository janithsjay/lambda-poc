import json
import logging
import uuid
import os
import sys

sys.path.insert(1, 'src')

from models.job import Job
from models.httpResponse import HTTPResponse
from logger.loggerFunction import getLogger, addTranscationId
from constants import httpConstants
from services import get_job
from util.propertyReader import Config

TRANSACTION_ID = "Transaction-Id"
HEADERS = "headers"
BODY = "body"
PATH = "path"
HTTP_METHOD = "httpMethod"
STATUS_CODE = "statusCode"
QUERY_STRING_PARAMETERS = "queryStringParameters"

logger = getLogger()
config = Config(os.environ['env'])


def lambda_handler(event, context):
    logging.info(config.get_config("application", "env"))
    if TRANSACTION_ID in event[HEADERS]:
        transaction_id = event[HEADERS][TRANSACTION_ID]
    else:
        transaction_id = str(uuid.uuid4())

    addTranscationId(logger, transaction_id)

    if event[PATH] == '/jobs' and event[HTTP_METHOD] == httpConstants.GET:
        job_id = event[QUERY_STRING_PARAMETERS]['jobId'];
        try:
            response = get_job(job_id)
            return HTTPResponse(200, response, None, None).to_json()
        except Exception:
            return HTTPResponse(400, None, None, f"Could not find a job for id: {job_id}").to_json()
