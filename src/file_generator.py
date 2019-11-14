import sys
import pandas as pd
from datetime import datetime, date
from src.logger import Logger


date_format = '%Y-%m-%d'
today_str = datetime.now().strftime(date_format)

def generate_file(data: pd.DataFrame):
    chip_multi = data
    chip_multi['StoneCode'] = chip_multi['Opportunity__r'].map(lambda row: row['StoneCode__c'])
    chip_multi['Account'] = chip_multi['Opportunity__r'].map(lambda row: row['Account']['Id'])
    chip_multi['Polo'] = chip_multi['Opportunity__r'].map(lambda row: row['Account']['Grupo_3_SF__c'])
    chip_multi['Comercial'] = chip_multi['Opportunity__r'].map(lambda row: row['Account']['Grupo_4_SF__c'])
    chip_multi['CreatedDate'] = chip_multi['Opportunity__r'].map(lambda row: row['CreatedDate'])
    chip_multi['CreatedDate'] = pd.to_datetime(chip_multi['CreatedDate']).map(lambda x: x.replace(tzinfo=None))
    chip_multi.drop(columns='Opportunity__r', inplace=True)
    chip_multi.sort_values('CreatedDate', ascending=False, inplace=True)
    today_work = chip_multi[chip_multi['CreatedDate'] > f'{date.today().strftime(date_format)}']
    cred = chip_multi.dropna(subset=['StoneCode'])
    ncred = chip_multi.loc[chip_multi['StoneCode'].isna()]

    file_name = f'files/{today_str}_Credenciamento_Chip_Multi.xlsx'

    try:
        with pd.ExcelWriter(file_name) as writer:
            today_work.to_excel(writer, sheet_name='Hoje', index=False)
            cred.to_excel(writer, sheet_name='Credenciados', index=False)
            ncred.to_excel(writer, sheet_name='Não Credenciados', index=False)

    except Exception as error:
        logger = Logger()
        logger.send(f'An Error occurred generating attach file! ERROR: {error}')
        sys.exit(6)


    return file_name