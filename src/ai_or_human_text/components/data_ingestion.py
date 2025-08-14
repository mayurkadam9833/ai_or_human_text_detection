import os
import zipfile
from urllib.request import urlretrieve
from src.ai_or_human_text.logging import logger
from src.ai_or_human_text.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self,config:DataIngestionConfig):
        self.config=config 

    def download_file(self):
        try:
            if not os.path.exists(self.config.local_data_file):
                filename,header=urlretrieve(
                    url=self.config.source_url,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded sucessfully from following header:\n {header}")

            else:
                logger.info(f"file is already exists...")
        
        except Exception as e:
            raise e
    
    def extract_file(self):
        unzip_path=self.config.unzip_dir
        os.makedirs(unzip_path,exist_ok=True)
        with zipfile.ZipFile(self.config.local_data_file,"r")as zipref:
            zipref.extractall(unzip_path)