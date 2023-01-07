from commands.command import Command
from commands.handler import Handler
from commands.handlers.create_user.create_user_algolia_handler import CreateUserAlgoliaCommand, CreateUserAlgoliaHandler
from commands.handlers.create_user.create_user_bigquery_handler import CreateUserBigqueryHandler
from commands.handlers.create_user.create_user_datastore_handler import CreateDatastoreUserHandler
from commands.handlers.create_user.create_user_notification_handler import CreateUserNotificationHandler
from commands.handlers.send_mail.send_mail_handler import SendMailCommand, SendMailHandler


class CreateUserCommand(Command):
    firstname: str
    lastname: str
    mail_notification: SendMailCommand

class CreateUserHandler(Handler):
    def __init__(self, command: CreateUserCommand) -> None:
        self._command = command
        
    def _execute(self) -> None:
        try:
            create_user_datastore_handler=CreateDatastoreUserHandler(self._command)
            create_user_datastore_handler.execute()
            create_user_command = CreateUserAlgoliaCommand(
                firstname=self._command.get("firstname"),
                lastname=self._command.get("lastname"),
                id=create_user_datastore_handler.user_id
            )
            create_user_algolia_handler=CreateUserAlgoliaHandler(create_user_command)
            create_user_algolia_handler.execute()
            CreateUserBigqueryHandler(create_user_command).execute()
            CreateUserNotificationHandler(create_user_command).execute()
            send_mail_command = SendMailCommand(**self._command.get("mail_notification"), body="Success create user")
            SendMailHandler(send_mail_command).execute()
        except Exception as e:
            create_user_datastore_handler.rollback()
            create_user_algolia_handler.rollback()
            send_mail_command = SendMailCommand(**self._command.get("mail_notification"), body=f"Error in create user: '{str(e)}'")
            SendMailHandler(send_mail_command).execute()