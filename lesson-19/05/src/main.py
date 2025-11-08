#############################
# Logging
#############################
from aws_lambda_powertools import Logger
logger = Logger()


#############################
# Main
#############################
@logger.inject_lambda_context(log_event=True)
def lambda_handler(event, context):
    logger.info("This is an info log")
    logger.debug("This is a debug log")
    logger.warning("This is a warning log")
    logger.error("This is an error log")
