from typing import Dict
import requests
import logging
from decouple import config



def get_partner_info(cpf: str, datasets: list) -> Dict[str, str]:
    """ Get info of the Partner """

    url_base = "https://bigboost.bigdatacorp.com.br"

    base_payload = {
        "Datasets": "basic_data",
        "q": f"doc{{{cpf}}}",
        "AccessToken": config("TOKEN"),
    }

    payload = {}

    for dataset in datasets:
        print(f"{cpf} - Getting data of the people - " f"{dataset}")
        base_payload["Datasets"] = dataset
        try:
            response = requests.post(f"{url_base}/peoplev2", json=base_payload)
            payload[dataset] = response.json()["Result"][0]
            payload[dataset]["QueryId"] = response.json()["QueryId"]
        except Exception as error:
            logging.info(f"Error in response of API BigData Corp - {error}")
    
    return payload