class Carteira:
    def __init__(self, moeda, saldo):
        self.moeda = moeda
        self.saldo = saldo

    def converteryuan (self, valoryuan):
        if self.moeda == "USD":
            return valoryuan * 0.14
        elif self.moeda == "BRL":
            return valoryuan * 0.85
        elif self.moeda == "CNY":
            return valoryuan

    def __add__(self, valoryuan):
        valorconvertido = self.converteryuan(valoryuan)
        return self.saldo + valorconvertido

    def __sub__(self, valoryuan):
        valorconvertido = self.converteryuan(valoryuan)
        return self.saldo - valorconvertido


carteirausd = Carteira ("USD", 10.0)
print("Soma da carteira USD + 50 yuan =" carteirausd + 50.0)

carteirabrl = Carteira ("BRL", 100.0)
print("Soma da carteira BRL + 50 yuan =" carteirabrl + 50.0)

carteiracny = Carteira ("CNY", 200.0)
print("Subtração da carteira CNY - 20 Yuan =" carteiracny - 20.0)
