from enum import Enum

class ProcessStatus(str, Enum):
    ABERTO = 'ABERTO'
    EM_ANDAMENTO = 'EM_ANDAMENTO'
    ENCERRAMENTO = 'ENCERRAMENTO'