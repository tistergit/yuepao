from paddleocr import PaddleOCR
import logging

def paddle_ocr_text(img_path):
    logging.info("== ocr start ==")
    ocr = PaddleOCR(use_angle_cls=True, lang='ch')
    result = ocr.ocr(img_path, cls=True)
    for row in result[0]:
        concat_output = "\n".join(row[1][0] for row in result[0])
    logging.info("ocr result : {} " , concat_output)
    return concat_output



if __name__ == '__main__':
    img_path = '../images/01RX87Sx2UnU188e3cc938e47505c9d87ad0e50d5a1e.jpg'
    result = paddle_ocr_text(img_path)
    print(result)
