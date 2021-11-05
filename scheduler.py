import argparse

from utils.athena_utils import generate_athena_tables
from workflows.snowflake import drop_star_schema, generate_snowflake_star_schema, load_data_from_s3


def get_args():
    parser = argparse.ArgumentParser(description='Arguments to manage s3 and snowflake infrustructure')

    parser.add_argument('-g', '--generate',
                        action="store", dest="query",
                        help="Generate infrustructure", default=False)

    parser.add_argument('-d', '--delete',
                        action="store", dest="delete",
                        help="Delete tables", default=False)

    parser.add_argument('-r', '--refresh',
                        action="store", dest="refresh",
                        help="Refresh tables ", default=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()

    if args.generate:
        generate_snowflake_star_schema()
        generate_athena_tables()
        load_data_from_s3()
        return

    if args.delete:
        drop_star_schema()
        return

    if args.refresh:
        drop_star_schema()
        generate_snowflake_star_schema()
        generate_athena_tables()
        load_data_from_s3()


if __name__ == '__main__':
    main()