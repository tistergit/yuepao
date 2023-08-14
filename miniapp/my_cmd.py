from utils import openai_util
from loguru import logger



def todo_cmd(org_text):
    return "todo"

def ocr_cmd(org_text):
    logger.info("ocr cmd  result : {} ", org_text)
    return org_text

def ielts_cmd(org_text):
    gpt_result = openai_util.ielts_coach(org_text)
    logger.info("gpt_result result : {} ", gpt_result)
    return gpt_result

def fanyi_cmd(org_text):
    return "aaa"