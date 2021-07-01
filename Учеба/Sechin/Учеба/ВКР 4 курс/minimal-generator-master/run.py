from MinGen import *


input_file_name = 'input.txt'


def main():
    with open(input_file_name, 'r') as f:
        data = [list(map(int, line.split())) for line in f.read().split('\n')]

    objects_count = len(data)
    signs_count = len(data[0])
    mg = MinGen(signs_count, objects_count, data)
    mg.print_data()

    mg.print_prom_tab()

    mg.gen_all()

    mg.check()

    mg.save_all_to_excel()




if __name__ == '__main__':
    main()
