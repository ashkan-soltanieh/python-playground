class MailService:
    def __init__(self, message):
        self.__message = message

    def send_email(self):
        self.__connect()
        self.__authenticate()
        # Do send email...
        print("Sending email...")
        print("Email sent!")
        self.__disconnect()
    
    def __connect(self):
        print("Connect")
    
    def __disconnect(self):
        print("Disconnect")
    
    def __authenticate(self):
        print("authenticate")