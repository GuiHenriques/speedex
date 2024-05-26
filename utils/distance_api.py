import os
import requests

from dotenv import load_dotenv

load_dotenv()


def requisicao_api_distance(cep_destino, mode):
    base_url = "https://maps.googleapis.com/maps/api/distancematrix/json"
    cep_ufsc = "88040-370"

    params = {
        "destinations": cep_destino,
        "mode": mode,
    }

    params["origins"] = cep_ufsc
    params["key"] = os.getenv("API_KEY")

    response = requests.get(base_url, params=params).json()

    if response["status"] == "OK":
        return response["rows"][0]["elements"][0]
    else:
        raise Exception(response["error_message"])
