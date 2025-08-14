import pandas as pd
from src.ai_or_human_text.entity.config_entity import DataValidationConfig
from src.ai_or_human_text.logging import logger


class DataValidation:
    def __init__(self,config:DataValidationConfig):
        self.config=config 

    def schema_validation(self):
        try:
            schema_status:None
            data=pd.read_csv(self.config.unzip_data_path)
            all_cols=list(data.columns)
            all_schema=self.config.all_schema.keys()

            for col in all_cols:
                if col not in all_schema:
                    schema_status=False
                    with open(self.config.STATUS_FILE_PATH,"w")as file:
                        file.write(f"schema status: {schema_status}")
                        logger.info(f"schema does not match with this columns:{[col]}")
                
                else: 
                    schema_status=True
                    with open(self.config.STATUS_FILE_PATH,"w")as file:
                        file.write(f"schema status: {schema_status}")
                return schema_status
        
        except Exception as e: 
            raise e
        
    def data_type_validation(self):
        try:
            data_type_status:None 
            data=pd.read_csv(self.config.unzip_data_path)
            all_data_type=list(data.dtypes)
            all_schema=self.config.all_schema.values()

            for data_type in all_data_type:
                if str(data_type) not in all_schema:
                    data_type_status=False
                    with open(self.config.STATUS_FILE_PATH,"a")as file:
                        file.append(f"\ndata type status: {data_type_status}")
                
                else:
                    data_type_status=True
                    with open(self.config.STATUS_FILE_PATH,"a")as file:
                        file.write(f"\ndata type status: {data_type_status}")
                
                return data_type_status
            
        except Exception as e: 
            raise e