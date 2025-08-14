from src.ai_or_human_text.logging import logger
from src.ai_or_human_text.pipeline.stage_01_data_ingestion import DataIngestionPipeline



stage_one="Data Ingestion"

if __name__ == "__main__":
    try:
        logger.info(f"<<<< stage: {stage_one} started")
        obj=DataIngestionPipeline()
        obj.main()
        logger.info(f"stage: {stage_one} completed >>>>")
    except Exception as e: 
        logger.info(e)
        raise e
    
