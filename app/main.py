from fastapi import FastAPI, File, UploadFile, Form, APIRouter, Request,Response
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from logger import Logger
from utils import ocr_util, openai_util,wx_util
import logging
import shutil
import os
import uvicorn as uvicorn

from my_cmd import *

IMAGES_PATH = '/images'


logger = logging.getLogger(__name__)

config_path = Path(__file__).with_name("logging_config.json")

uri = os.environ.get("URI",'/dev')

router = APIRouter(prefix=uri)
# router.mount("/static", StaticFiles(directory="static"), name="static")


def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    app.include_router(router)
    logger = Logger.make_logger(config_path)
    app.logger = logger
    return app


app = create_app()


@router.post("/upload/{func_id}")
def upload(func_id: str,request: Request, file: UploadFile = File(...)):
    request.app.logger.info("== upload file start , func : {} ===" , func_id)
    dst_file = os.path.join(IMAGES_PATH, file.filename)
    try:
        with open(dst_file, 'wb') as f:
            shutil.copyfileobj(file.file, f)
    except Exception as error:
        request.app.exception("message")
        return {"message": "There was an error uploading the file"}
    finally:
        file.file.close()
    ocr_result = ocr_util.paddle_ocr_text(dst_file)
    request.app.logger.info("ocr result : {} ", ocr_result)
    func_result = ""
    match func_id:
        case "ielts":
            func_result = ielts_cmd(ocr_result)
        case "ocr":
            func_result =  ocr_cmd(ocr_result)
        case "fanyi":
            func_result = fanyi_cmd(ocr_result)
        case _:
            func_result = todo_cmd(ocr_result)


    request.app.logger.info("== upload file end ===")
    return {'code': 200, 'message': func_result}

@router.get("/requestSubscribeMessage")
def requestSubscribeMessage(req: Request):
    req.app.logger.info("== requestSubscribeMessage start ===")
    if wx_util.checkSignature(req.query_params):
        return Response(content=req.query_params['echostr'])
    else:
        return "error"
    
@router.get("/code2session")
def wx_code2session(req: Request,code: str):
    req.app.logger.info("req code : {} " , code)
    openid = wx_util.get_openid(code)
    req.app.logger.info("openid : {} " , openid)
    return {'openid':openid}

@router.get("/")
async def root():
    return {"message": "Hello World"}



if __name__ == '__main__':
    uvicorn.run(app=app, reload=True)
