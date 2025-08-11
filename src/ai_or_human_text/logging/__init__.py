import logging
import os 
import sys 

#assign format
log_str="[%(asctime)s : %(levelname)s : %(module)s : %(message)s]"


# create directory for project logs
cur_dir=os.path.abspath(os.path.dirname(__file__))
log_dir=os.path.join(cur_dir,"logs")
log_path=os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

#logging config
logging.basicConfig(
    level=logging.INFO,
    format=log_str,
    handlers=[
        logging.FileHandler(log_path),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger("ai_human_text")