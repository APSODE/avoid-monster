import os
import traceback
import json
import sys

from AvoidMonster import PROJECT_ROOT_PATH
from datetime import datetime


class ErrorChecker:
    def __init__(self, target_func):
        self.func = target_func

    def __call__(self, *args, **kwargs):
        try:
            self.func(*args, **kwargs)
        except Exception as binded_error_message:
            error_date = datetime.now()
            error_date_str = f"{error_date}".replace(":", "-")
            error_log_dir = PROJECT_ROOT_PATH + "\\error_log\\error data - " + f"{error_date_str}.json"
            exc_type, exc_value, exc_traceback = sys.exc_info()
            error_data = {
                "error_data": {
                    "date": str(error_date),
                    "message": str(binded_error_message),
                    "traceback": traceback.format_exception(exc_value)
                }
            }

            if not os.path.exists(PROJECT_ROOT_PATH + "\\error_log\\"):
                os.mkdir(PROJECT_ROOT_PATH + "\\error_log\\")

            with open(f"{error_log_dir}", "w", encoding = "utf-8") as error_log_file:
                json.dump(error_data, error_log_file, indent = 4)
