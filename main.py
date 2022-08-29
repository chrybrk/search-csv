import csv

def read_csv(fp):
    list_of_content = []

    with open(fp, "r") as file:
        read = csv.reader(file)
        for i in read: list_of_content.append(i)

    return list_of_content

def show_table(list_of_content):
    total_length = [[0, 0] for i in range(len(list_of_content[0]))]

    for content in range(0, len(list_of_content)):
        m = list_of_content[content]
        for ext in range(0, len(m)):
            if len(m[ext]) > total_length[ext][0]:
                total_length[ext][0] = len(m[ext])
                total_length[ext][1] = m[ext]

    for content in range(0, len(list_of_content)):
        m = list_of_content[content]
        for ext in range(len(m)):
            if m[ext] != total_length[ext][1]:
                for i in range(int((total_length[ext][0] - len(m[ext])) / 2)): print(" ", end="")
            print(m[ext], end=" ")
            if m[ext] != total_length[ext][1]:
                size = (total_length[ext][0] - len(m[ext])) - int((total_length[ext][0] - len(m[ext])) / 2)
                for i in range(size): print(" ", end="")
        print()

def search_by_first_letter(list_of_content, c, which):
    print()
    list_of_searched_item = []

    for content in range(0, len(list_of_content)):
        m = list_of_content[content]
        if c == m[which - 1][0]: list_of_searched_item.append(m[which - 1])

    if (len(list_of_searched_item) == 0): print("** NO ITEM FOUND **")
    else:
        print(f"** FOUND {len(list_of_searched_item)} ITEM **")
        for item in list_of_searched_item:
            print(item)

        print()

file = read_csv(input("path of file: (ex. ./emp.csv OR C:/Desktop/emp.csv) "))
while True:
    print("""
    1) Show Table
    2) Search By First Letter
    e) Exit
    """)

    opt = input("$> ")
    if opt.lower() == "1": show_table(file)
    if opt.lower() == "2": search_by_first_letter(file, input("Letter: "), int(input("In which Coloumn: ")))
    if opt.lower() == "e": exit(0)
