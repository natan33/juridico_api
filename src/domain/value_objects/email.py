class Email:
    def __init__(self,value:str):
        if not value or "@" not in value:
            raise ValueError("Email inválido")
        self.value = value

    def __eq__(self, other):
        return isinstance(other,Email) and self.value == other.value
    