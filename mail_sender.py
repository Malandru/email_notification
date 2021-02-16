import smtplib


class MailSender:
    def __init__(self, from_address, password):
        self.from_address = from_address
        self.message = f'From: {from_address}\n'
        self.message += 'To: {}\nSubject: {}\n\n{}'
        self.server = smtplib.SMTP('smtp.gmail.com', 587)
        self.server.starttls()
        self.server.login(from_address, password)
        print('Mail sender login success')

    def send_text(self, to_addresses, subject, body_text):
        to = to_addresses
        if isinstance(to_addresses, list):
            to = ','.join(to_addresses)
        msg = self.message.format(to, subject, body_text)
        print(msg)
        self.server.sendmail(self.from_address, to_addresses, msg)
        print(f'Email has been sent to {to}')
