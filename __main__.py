import time
from src.data_collector import get_data
from src.file_generator import generate_file
from src.emails import Email
from src.prepare_mail import format_mail


def main():

    while True:
        cm = get_data()
        chip_multi_url = generate_file(data=cm)

        gmail = Email()
        gmail.login()
        _body, _subject, _recipients, _attachs = format_mail(attachs=[chip_multi_url])
        gmail.send_mail(to=_recipients, subject=_subject, body=_body, attachments=_attachs)
        gmail.logout()

        time.sleep(86400)


if __name__ == '__main__':
    main()