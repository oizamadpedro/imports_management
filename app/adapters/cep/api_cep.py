from uplink import Consumer, get, Path, Query, returns, json

class CepApi(Consumer):
    
    @returns.json
    @get("https://viacep.com.br/ws/{cep}/json/")
    def getCep(self, cep: Path): pass

#cep = CepApi().getCep("29163242")
