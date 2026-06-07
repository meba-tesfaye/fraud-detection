import pandas as pd
import logging

# Set up logging to track production pipeline execution
logging.basicConfig(
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - %(message)s'
)

def load_data(file_path: str) -> pd.DataFrame:
    """
    Safely loads raw transaction CSV files with explicit error handling.
    """
    try:
        logging.info(f"Attempting to load data from: {file_path}")
        df = pd.read_csv(file_path)
        logging.info(f"Successfully loaded data. Shape: {df.shape}")
        return df
    except FileNotFoundError:
        logging.error(f"Critical Error: The file at '{file_path}' does not exist.")
        raise
    except Exception as e:
        logging.error(f"An unexpected error occurred while loading data: {str(e)}")
        raise

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Handles pipeline deduplication safely.
    """
    try:
        initial_rows = len(df)
        df_cleaned = df.drop_duplicates()
        logging.info(f"Data cleaning complete. Removed {initial_rows - len(df_cleaned)} duplicate rows.")
        return df_cleaned
    except Exception as e:
        logging.error(f"Error encountered during data cleaning phase: {str(e)}")
        raise