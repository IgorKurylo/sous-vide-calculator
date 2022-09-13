from datetime import datetime, timedelta
import argparse
DATE_FORMAT = '%d-%m-%Y'
DATETIME_FORMAT = '%d-%m-%Y %H:%M'


def main():
    parser = init_parser()
    args = parser.parse_args()
    calculate_destination(args)


def calculate_destination(args):
    hours = args.hours
    date = args.date
    start_date = date-timedelta(hours=int(hours))
    print(f'Sous vide cooking for {hours}h')
    print(f'Cooking request end at {date.strftime(DATETIME_FORMAT)}')
    print(f'Start cooking at {start_date.strftime(DATETIME_FORMAT)}')


def valid_date_type(date_args):
    try:
        return datetime.strptime(date_args, DATETIME_FORMAT)
    except ValueError:
        msg = f'Give date {date_args} not valid! Expected format {DATETIME_FORMAT}'
        raise argparse.ArgumentTypeError(msg)


def init_parser():
    parser = argparse.ArgumentParser(description='Sous vide calculator')
    parser.add_argument(
        '--hours', help='A hour to setup a sous vide machine for cooking')
    parser.add_argument(
        '-d', '--date', type=valid_date_type, help=f'A day you want the cooking is ready, format {DATETIME_FORMAT}')

    return parser


if __name__ == '__main__':
    main()
