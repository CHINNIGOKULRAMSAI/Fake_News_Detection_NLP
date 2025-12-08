import os
import sys
from src.logger import logging


def error_detail_messages(error, error_details: sys):
    _, _, exc_tb = error_details.exc_info()
    filename = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error Occured in python scripts filename [{0}], line number [{1}] and the error is [{2}]".format(filename,exc_tb.tb_lineno, str(error))

    return error_message

class CustomException(Exception):
    def __init__(self, error_message, error_details:sys):
        super().__init__(error_message)
        self.error_message = error_detail_messages(error_message, error_details=error_details)

    def __str__(self):
        return self.error_message