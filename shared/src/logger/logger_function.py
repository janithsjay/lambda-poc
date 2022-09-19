import logging
import uuid

transactionIdVariable = None;
custom_values = {'functionName': 'jobFunction', 'transactionId': transactionIdVariable}


def getLogger():
    logger = logging.getLogger("application")
    syslog = logging.StreamHandler()
    formatter = logging.Formatter(
        '[%(asctime)s] [%(levelname)s] [%(threadName)s]  [%(process)d] [%(filename)s-%(lineno)d] - [functionName::%(functionName)s] [transactionId::%(transactionId)s]  %(message)s')
    syslog.setFormatter(formatter)
    logger.setLevel(logging.INFO)
    logger.addHandler(syslog)
    logger = logging.LoggerAdapter(logger, custom_values)
    return logger


def addTranscationId(logger, t_id):
    global transactionIdVariable
    if (t_id is None):
        transactionIdVariable = str(uuid.uuid4());
    else:
        transactionIdVariable = t_id
    custom_values["transactionId"] = transactionIdVariable
