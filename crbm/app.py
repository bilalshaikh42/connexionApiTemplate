import connexion
from connexion.resolver import RestyResolver

app = connexion.App(__name__, specification_dir="./api")
app.add_api("api.yml", resolver=RestyResolver('crbm.api'))
