from typing import Union
from commands.command import Command
from commands.handler import HandlerRollback


class CreateUserDatastoreCommand(Command):
    firstname: str
    lastname: str

class CreateDatastoreUserHandler(HandlerRollback):
    def __init__(self, command: CreateUserDatastoreCommand) -> None:
        self._command = command
        self.__user_id = None

    @property
    def user_id(self) -> Union[int, None]:
        return self.__user_id
        
    def _execute(self) -> None:
        self._validation()
        self.__user_id = 123

    def _rollback(self) -> None:
        pass

    def _validation(self) -> None:
        if self._command.get("lastname") is None:
            raise Exception("Lastname is required")