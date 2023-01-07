from commands.handler import HandlerRollback
from commands.handlers.create_user.create_user_datastore_handler import CreateUserDatastoreCommand


class CreateUserAlgoliaCommand(CreateUserDatastoreCommand):
    id: int

class CreateUserAlgoliaHandler(HandlerRollback):
    def __init__(self, command: CreateUserAlgoliaCommand) -> None:
        self._command = command
        
    def _execute(self) -> None:
        self._validation()

    def _rollback(self) -> None:
        pass

    def _validation(self) -> None:
        if self._command.get("lastname") is None:
            raise Exception("Lastname is required")