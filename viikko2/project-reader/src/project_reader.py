from urllib import request
from project import Project
import toml


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        toml_tiedosto = toml.loads(content)
        
        toml_tiedosto_nimi = toml_tiedosto['tool']['poetry']['name']
        toml_tiedosto_kuvaus = toml_tiedosto['tool']['poetry']['description']
        toml_tiedosto_riippuvuudet = toml_tiedosto['tool']['poetry']['dependencies']
        toml_tiedosto_dev_riippuvuudet = toml_tiedosto['tool']['poetry']['dev-dependencies']


        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(toml_tiedosto_nimi,toml_tiedosto_kuvaus,toml_tiedosto_riippuvuudet,toml_tiedosto_dev_riippuvuudet)
