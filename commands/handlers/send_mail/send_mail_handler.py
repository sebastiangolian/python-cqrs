from commands.command import Command
from commands.handler import Handler


class SendMailCommand(Command):
    receiver: str
    subject: str
    body: str

class SendMailHandler(Handler):
    def __init__(self, command: SendMailCommand) -> None:
        self._command = command
        
    def _execute(self) -> None:
        self._validation()

    def _validation(self) -> None:
        if self._command.get("receiver") is None:
            raise Exception("Receiver is required")
