from mail_sender import MailSender
import argparse
import json
import os


def main():
    args = parse_arguments()
    config = load_configuration(args.config)

    from_address = config['from']
    password = config["password"]
    receivers = config["to"]
    subject = config["subject"]
    message = config["message"]

    mail_sender = MailSender(from_address, password)
    mail_sender.send_text(receivers, subject, message)


def parse_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument('--config', required=True, help='JSON configuration file with mail settings')
    args = parser.parse_args()

    args.config = os.path.abspath(args.config)
    print('Using config file: ', args.config)
    return args


def load_configuration(filename):
    with open(filename) as json_file:
        data = json.load(json_file)
        json_file.close()
        return data


if __name__ == '__main__':
    main()
