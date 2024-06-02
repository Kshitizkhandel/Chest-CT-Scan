import os
import zipfile
import gdown
from cnnClassifier import logger
from cnnClassifier.utils.common import get_size
from cnnClassifier.entity.config_entity import DataIngestionConfig

class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

     
    def download_file(self)-> str:
        '''
        Fetch data from the url
        '''

        try: 
            dataset_url = "https://drive.google.com/file/d/1Te_0zPDsfiNgepXYhYDWtIpn4wrUb6bY/view?usp=sharing"
            zip_download_dir = self.config.local_data_file
            os.makedirs(zip_download_dir,exist_ok=True)
            #os.makedirs("artifacts/data_ingestion", exist_ok=True)
            logger.info(f"Downloading data from {dataset_url} into file {zip_download_dir}")

            file_id = dataset_url.split("/")[-2]
            prefix="https://drive.google.com/uc?/export-download&id-"
            gdown.download(prefix+file_id,zip_download_dir)

            logger.info(f"Downloaded data from {dataset_url} into file {zip_download_dir}")

        except Exception as e:
            raise e
        
    
    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
       
         """
        zip_file_path = self.config.local_data_file
        unzip_path = self.config.unzip_dir

        # Debugging prints to check paths
        print(f'Zip file path: {zip_file_path}')
        print(f'Unzip directory: {unzip_path}')

        # Check if the zip file path is actually a file
        #if not os.path.isfile(zip_file_path):
            #raise IsADirectoryError(f"The specified path {zip_file_path} is not a valid file.")

        # Create the directory if it doesn't exist
        os.makedirs(unzip_path, exist_ok=True)
        print('Unzip directory created')

        # Extract the zip file
        #with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            #zip_ref.extractall(unzip_path)
        #print('Extraction completed')

