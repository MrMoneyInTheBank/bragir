import openai
from openai import AuthenticationError, OpenAI

from openai import AsyncOpenAI
from bragir.tracing.logger import logger


def initiate_client(api_key: str) -> OpenAI:
    logger.info("Initiating client")
    if not api_key:
        logger.error("Cannot initiate OpenAI client, please provide an API key.")
        exit(1)

    if not check_validity(api_key):
        logger.error("Invalid API key.")
        exit(1)

    return OpenAI(api_key=api_key)


def initate_async_client(api_key: str) -> AsyncOpenAI:
    logger.info("Initiating async client")
    if not api_key:
        logger.error("Cannot initiate OpenAI client, please provide an API key.")
        exit(1)

    if not check_validity(api_key):
        logger.error("Invalid API key.")
        exit(1)

    return AsyncOpenAI(api_key=api_key)


def check_validity(api_key: str) -> bool:
    logger.info("Checking validity of API key")
    try:
        openai.api_key = api_key
        openai.models.list()
    except AuthenticationError as _e:
        return False
    return True
