import logging 
from datetime import datetime
import os 

logger=logging.Logger(__name__)
logger.setLevel(logging.INFO)

formatter=logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(lineno)s - %(message)s')
log_file=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

file_path=os.path.join(os.getcwd(),'logs')
os.makedirs(file_path,exist_ok=True)

log_file_path=os.path.join(file_path,log_file)

file_handler=logging.FileHandler(log_file_path)
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


if __name__=="__main__":
   logger.info('logging has started')

