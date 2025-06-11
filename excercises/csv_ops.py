import csv , os
import importlib.resources
from os.path import exists

from pathlib import  Path
def do_csv_ops(file):
    '''
     code snippet that does read from a csv file that is comma separated
    :param file:
    :return:
    '''
    try:
        with importlib.resources.files('excercises').joinpath('records.csv').open('r') as f:
            content = csv.reader(f)
            for line in content:
                print(line)

    except Exception as e:
        print(f'encountered exception:{e}')

def do_csv_ops_dict(file):
    '''
     code snippet that does read from a csv file and interprets the data as dict of key-value instead of list of values
    :param file:
    :return:
    '''
    try:
        with importlib.resources.files('excercises').joinpath('records.csv').open('r') as f:
            for line in csv.DictReader(f):
                print(line)
    except Exception as e:
        print(f'encountered an exception:{e}')
def do_csv_ops_write(file):
    '''
     code snippet that does write to the file passed as arg. file is opened in w mode , so we always overwrite
    :param file:
    :return:
    '''
    dirs = Path('C:\\Users\\esmjaga\\dir_for_python_stubs')
    dirs.mkdir(parents=False,exist_ok=True)
    content = [['Region','Country','Capital'],
               ['Asia','Myanmar','Rangoon'],
               ['Europe','Germany','Berlin'],
               ['North America','Mexico','Mexico City']
               ]
    try:
        print(dirs)
        file_name = dirs.joinpath(file)
        with open(file_name,mode='a+') as f:
            for c in content:
                csv.writer(f).writerow(c)
            csv.writer(f).writerows([['Africa','SA','Pretoria'],
                                 ['South America','Brazil','Brasilia']])
    except Exception as e:
        print(f'encountered an exception:{e}')


if __name__ == '__main__':
    file_name = 'records.csv'
    out_file_name = 'records_out.csv'
    do_csv_ops(file_name)
    do_csv_ops_dict(file_name)
    do_csv_ops_write(out_file_name)