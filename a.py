from utils.apis import get_distancia
from datetime import timedelta

d = get_distancia("09530210", 1)

distancia = d["distance"]["value"]
segundos = d["duration"]["value"]
time = d["duration"]["text"]


# print(tempo)
print(time)
