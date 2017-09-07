"""This is main package module"""

from knoema.api_config import ApiConfig
from knoema.api_client import ApiClient
from knoema.data_reader import DataReader

def get(dataset, IncludeMetadata = False, **dim_values):
    """Use this function to get data from Knoema dataset."""

    if not dataset:
        raise ValueError('Dataset id is not specified')

    if not dim_values:
        raise ValueError('Dimensions members are not specified')

    config = ApiConfig()
    client = ApiClient(config.host, config.app_id, config.app_secret)

    dataset = client.get_dataset(dataset)
    dimensions = []
    for dim in dataset.dimensions:
       dimensions.append(client.get_dimension(dataset.id, dim.id))
    data_reader = DataReader(client, dataset, dimensions, dim_values, IncludeMetadata)

    return data_reader.get_pandasframe()

def upload(file_path, dataset=None, public=False):
    """Use this function to upload data to Knoema dataset."""

    config = ApiConfig()
    client = ApiClient(config.host, config.app_id, config.app_secret)
    return client.upload(file_path, dataset, public)

def delete(dataset):
    """Use this function to delete dataset by it's id."""
    
    config = ApiConfig()
    client = ApiClient(config.host, config.app_id, config.app_secret)
    client.delete(dataset)

def verify(dataset, publication_date, source, refernce_url):
    """Use this function to verify a dataset."""

    config = ApiConfig()
    client = ApiClient(config.host, config.app_id, config.app_secret)
    client.verify(dataset, publication_date, source, refernce_url)
