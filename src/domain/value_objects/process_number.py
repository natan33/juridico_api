class ProcessNumber:
    def __init__(self, value:str):
        if not value or len(value) < 5:
            raise ValueError("Número de processo Invalido")
        self.value = value

    def __eq__(self, other):
        return isinstance(other, ProcessNumber) and self.value == other.value
    
    
        