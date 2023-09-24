from random import randint
from sys import argv


if __name__ == '__main__':
    #components_count = int(argv[1])
    #max_vectors_count = int(argv[2])
    #high_bound = int(argv[3])
    #file_name = argv[4]

    components_count = 2
    max_vectors_count = 2000
    high_bound = 5000
    file_name = "test123.txt"

    result = set()
    for i in range(max_vectors_count):
        result.add(tuple(randint(0, high_bound) for i in range(components_count)))
    with open(file_name, 'w') as out:
        out.write('{}\n'.format(components_count))
        for item in result:
            out.write('\t'.join((str(x) for x in item)) + '\n')
