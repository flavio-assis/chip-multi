import os
import time
from datetime import datetime


class Logger():
    """Create file, directories and log errors."""

    def __init__(self):
        self.time = datetime.utcfromtimestamp(int(time.time())).strftime('%d-%m-%Y %H:%M:%S')
        self.directory = "./log/sf_chip_multi"
        self.log_file = os.path.join(str(self.directory), "sf_chip_multi.log")

    def check_dir(self):
        """Check if log directory exists and create if not."""

        if not os.path.isdir(self.directory):
            os.mkdir(self.directory, 755)
        if not os.path.exists(self.log_file):
            from pathlib import Path
            Path(self.log_file).touch()

    def send(self, msg_error):
        """Log errors into file sf_chip_multi.log in the directory /log/sf_chip_multi."""

        self.check_dir()
        with open(self.log_file, "a") as logger_file:
            logger_file.write("{}, {}\n".format(self.time, msg_error))