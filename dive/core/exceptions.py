from abc import ABC, abstractmethod


class ClientError(ABC, Exception):
    
    @property
    def status_code(self) -> int:
        return 400

    @property
    @abstractmethod
    def message(self) -> str:
        pass


class NotFound(ClientError):

    def __init__(self) -> None:
        super().__init__(self.message)

    @property
    def status_code(self) -> int:
        return 404

    @property
    def message(self) -> str:
        return 'Resource not found.'
