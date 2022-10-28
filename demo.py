from src.insurance.pipeline.pipeline import Pipeline
from src.exception import PremiumException
from src.logger import logging
from src.insurance.config.configuration import Configuration
import os

def main():
    try:
        config_path = os.path.join("config","config.yaml")
        pipeline = Pipeline(Configuration(config_file_path=config_path))
        #pipeline.run_pipeline()
        pipeline.start()
        logging.info("main function execution completed.")

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()