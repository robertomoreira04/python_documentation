# percorrendo n linhas de um arquivo txt

def file_read_from_line(fname, nlines):
    from itertools import islice
    with open(fname, encoding="utf-8") as file:
        for line in islice(file, nlines):
            print(line.strip())

file_read_from_line("name.txt", 2)