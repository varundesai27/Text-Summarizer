from src.textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from src.textSummarizer.logging import logger

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f"---- stage {STAGE_NAME} ----")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f"---- stage {STAGE_NAME} completed ---- \n\n x =========================== x")
except Exception as e:
    logger.error(e)
    raise e