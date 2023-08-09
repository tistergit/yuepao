from utils import openai_util
from loguru import logger



def todo_cmd(org_text):
    return

def ocr_cmd(org_text):
    logger.info("ocr cmd  result : {} ", org_text)
    return ocr_cmd

def ielts_cmd(org_text):
    gpt_result = openai_util.openai_trans(org_text)
    logger.info("gpt_result result : {} ", gpt_result)
    return gpt_result