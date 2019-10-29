import os
import argparse

def create_all():
    for dir_name in ['data', 'log', 'models', 'result']:
        os.makedirs(dir_name, exist_ok=True)
    with open('.env', 'w', encoding='utf8') as f:
        f.writelines('email=\n')
        f.writelines('email_passwd=\n')

def delete(key: str):
    if key == 'all':
        for dir_name in ['data', 'log', 'models', 'result']:
            os.removedirs(dir_name)
    else:
        os.removedirs(key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-c', action='store_true')
    group.add_argument('-d', choices=['log', 'data', 'models', 'all', 'result'],
                       default='log')

    args = parser.parse_args()
    if args.c:
        create_all()
    else:
        delete(args.d)