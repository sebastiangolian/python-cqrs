from commands.handlers.create_user.create_user_handler import CreateUserCommand, CreateUserHandler
from commands.handlers.send_mail.send_mail_handler import SendMailCommand


command = CreateUserCommand(
    firstname="Jan",
    lastname="Nowak", 
    mail_notification=SendMailCommand(
        receiver="jannowak@gmail.com", 
        subject="Create user"
    )
)

if __name__ == "__main__":
    CreateUserHandler(command).execute()