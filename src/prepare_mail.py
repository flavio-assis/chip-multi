from datetime import datetime


date_format = '%d/%m/%Y'
today_str = datetime.now().strftime(date_format)

def format_mail(attachs: list):
    with open('templates/email_body.txt', 'r', encoding='utf-8') as body_file:
        _body = f'{body_file.read()}'.format(today_str)

    with open('templates/email_subject.txt', 'r', encoding='utf-8') as subject_file:
        _subject = f'{subject_file.read()}'.format(today_str)

    with open('templates/recipient.txt', 'r', encoding='utf-8') as recipients_file:
        _recipients = recipients_file.read().split(',')


    _attachs = [(f'{attach[6:]}', open(attach, 'rb')) for attach in attachs]

    return _body, _subject, _recipients, _attachs