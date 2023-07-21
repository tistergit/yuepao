import logging
from paddleocr import PaddleOCR

def ocr_text(img_path):
    logging.info("== ocr start ==")
    ocr = PaddleOCR(use_angle_cls=True, lang='en')
    result = ocr.ocr(img_path, cls=True)
    for row in result[0]:
        concat_output = "\n".join(row[1][0] for row in result[0])
    logging.info("ocr result : %s " , concat_output)
    return concat_output

if __name__ == '__main__':
    img_file = 'images/5T40gqYLhAJv188e3cc938e47505c9d87ad0e50d5a1e.jpg'
    ocr_text = ocr_text(img_file)
    print(ocr_text)