import argparse


def transform_address_details(details):
    if type(details) is not list:
        raise TypeError('Details need to be a valid list')
    details[0] = details[0].lower()
    details[1] = int(details[1])
    return tuple(details)


def get_address_queries_from_file(file_path):
    addresses = []
    queries = []
    try:
        with open(file_path) as file:
            content = file.readlines()
            address_count = int(content[0])

            for i, line in enumerate(content[1:]):
                if i <= address_count-1:
                    details = line.split()
                    parsed_details = transform_address_details(details)
                    addresses.append(parsed_details)
                else:
                    queries.append(line.strip().lower())

        unique_addresses = set(addresses)
        return unique_addresses, queries
    except IOError as error:
        raise error
    except Exception as error:
        raise error


def execute_queries(addresses, query):
    addresses_length = len(addresses)

    for name in query:
        search_result = None
        for i, address in enumerate(addresses):

            if address[0] == name:
                search_result = '{}={}'.format(address[0], address[1])
                yield (search_result)

            if search_result is None and i >= addresses_length-1:
                yield 'Not Found'


def run(file):
    addreesses, queries = get_address_queries_from_file(file)
    result = execute_queries(addreesses, queries)

    while result:
        try:
            print(next(result))
        except StopIteration:
            break

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--file',
        type=str,
        default=None,
        help="The path to the file containing addresses and queries.")
    args = parser.parse_args()
    file = args.file
    if not file:
        raise IOError('Provide path to the address/query file')
    else:
        run(args.file)
