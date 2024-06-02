from cnnClassifier.config.configuration import ConfigurationManager
from cnnClassifier.components.data_ingestion import DataIngestion
from cnnClassifier import logger
STAGE_NAME="Data Ingestion Pipeleine"

class DataTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        try:
            config = ConfigurationManager()
            data_ingestion_config = config.get_data_ingestion_config()
            data_ingestion = DataIngestion(config=data_ingestion_config)
            logger.info('Data ingestion done')
            data_ingestion.download_file()
            logger.info('Downloading files done')
            data_ingestion.extract_zip_file()
            logger.info('Extracting all')
        except Exception as e:
             raise e
        
if __name__=='__main__':
    obj=DataTrainingPipeline()
    logger.info(f'Initiating pipeline {STAGE_NAME}')
    obj.main()
    logger.info(f'{STAGE_NAME} completed')

  