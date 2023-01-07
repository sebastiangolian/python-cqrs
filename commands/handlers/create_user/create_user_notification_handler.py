from commands.handler import Handler
from commands.handlers.create_user.create_user_datastore_handler import CreateUserDatastoreCommand


class CreateUserNotificationCommand(CreateUserDatastoreCommand):
    pass

class CreateUserNotificationHandler(Handler):
    def __init__(self, command: CreateUserNotificationCommand) -> None:
        self._command = command
        
    def _execute(self) -> None:
        self._validation()

    def _validation(self) -> None:
        if self._command.get("lastname") is None:
            raise Exception("Lastname is required")