from typing import Dict
import requests
import logging
from decouple import config


def get_company_info(cnpj: str, datasets: list) -> Dict[str, str]:
    """ Get info of the Company's """

    url_base = "https://bigboost.bigdatacorp.com.br"

    base_payload = {
        "Datasets": "basic_data",
        "q": f"doc{{{cnpj}}}",
        "AccessToken": config("TOKEN"),
    }

    payload = {}

    for dataset in datasets:
        print(f"{cnpj} - Getting data of the Company - " f"{dataset}")
        base_payload["Datasets"] = dataset
        try:
            response = requests.post(f"{url_base}/companies", json=base_payload)
            payload[dataset] = response.json()["Result"][0]
            payload[dataset]["QueryId"] = response.json()["QueryId"]
        except Exception as error:
            logging.info(f"Error in response of API BigData Corp - {error}")
    
    return payload