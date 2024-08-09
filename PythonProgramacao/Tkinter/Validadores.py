# Para criar validação de entradas numéricas na parte de CÓDIGO e TELEFONE

class Validadores:
    # Validando entrada docódigo de até dois dígitos:
    def validate_entrada_codigo(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 100
    # Validando entreda do telefone de até 1.000.000.000 dígitos:       
    def validate_entrada_telefone(self, text):
        if text == "": return True
        try:
            value = int(text)
        except ValueError:
            return False
        return 0 <= value <= 99999999999            # Quantidade de algarismos em um número de telefone
    