

def format(low, file_name):
    min_evaluation = 100000000000
    min_x, min_y, min_z = 0, 0, 0

    with open(file_name, 'r') as previous_f:
        with open(file_name[0:-4] + '_formatted.txt', 'w') as after_f:
            while True:
                try:
                    s = previous_f.readline()

                    if s == '':
                        break

                    x, y, z, evaluation = s.split()

                    print(x, y, z, evaluation)

                    if min_evaluation > float(evaluation):
                        min_evaluation = float(evaluation)
                        min_x, min_y, min_z = x, y, z

                    if float(evaluation) > low:
                        continue

                    after_f.write('{} {} {} {}\n'.format(x, y, z, evaluation))
                except ValueError:
                    continue

    print('\nmin: {} {} {} {}'.format(min_x, min_y, min_z, min_evaluation))


def upper_format(high, file_name):
    max_evaluation = 1000
    max_x, max_y, max_z = 0, 0, 0

    with open(file_name, 'r') as previous_f:
        with open(file_name[0:-4] + '_hformatted.txt', 'w') as after_f:
            while True:
                try:
                    s = previous_f.readline()

                    if s == '':
                        break

                    x, y, z, evaluation = s.split()

                    print(x, y, z, evaluation)

                    if max_evaluation < float(evaluation):
                        max_evaluation = float(evaluation)
                        max_x, max_y, max_z = x, y, z

                    if float(evaluation) < high:
                        continue

                    after_f.write('{} {} {} {}\n'.format(x, y, z, evaluation))
                except ValueError:
                    continue

    print('\nmax: {} {} {} {}\n'.format(max_x, max_y, max_z, max_evaluation))


if __name__ == '__main__':

    file_name = 'precision_table_3km_1deg.txt'
    low = 200
    format(low, file_name)

    '''
    file_name = 'precision_table_1km.txt'
    high = 100
    upper_format(high, file_name)
    '''
