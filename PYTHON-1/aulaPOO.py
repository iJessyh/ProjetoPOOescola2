class Carro:
    def __init__(self, marca, modelo, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor
        self.velocidade = 0

    def acelerar(self, valor):
        self.velocidade   += valor
        print(f"{self.modelo} acelerou para {self.velocidade} km/h.")
        
    def frear(self, valor):
        self.velocidade -= valor
        if self.veocidade < 0 :
           self.velocidade = 0
        print(f"{self.modelo} reduzi para {self.velocidade} km/h")

        def detalhes(self):
            return(f"{self.marca} {self.modelo} ({self.ano}) - "
                   f" cor: {self.cor}, velocidade: {self.velocidade} km/h")
        carro1 = carro


 