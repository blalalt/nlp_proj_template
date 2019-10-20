import os
import argparse

def create_all():
    for dir_name in ['data', 'log', 'models']:
        os.makedirs(dir_name)

def delete(key: str):
    os.removedirs(key)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    group = parser.add_mutually_exclusive_group()

    group.add_argument('-c', action='store_true')
    group.add_argument('-d', choices=['log', 'data', 'models', 'all'],
                       default='log')

    args = parser.parse_args()
    if args.c:
        create_all()
    else:
        delete(args.d)