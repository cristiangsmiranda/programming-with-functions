import csv

def main():
    I_NUMBER_INDEX = 0
    NAME_INDEX = 1

    students = read_dictionary("students.csv", I_NUMBER_INDEX)
    
    inumber = (input("Please enter an I-Number (xxxxxxxxx): "))
    inumber = inumber.replace("-", "")

    #The isdigit() method returns True if all the characters are digits, otherwise False
    if not inumber.isdigit():
        print("Invalid character in I-Number")
    else:
    # len() returns the length of an object. 
        if len(inumber) < 9:
            print("Invalid I-Number: too few digits")
        elif len(inumber) > 9:
            print("Invalid I-Number: too many digits")
        else:
            if inumber not in students:
                print("No such student")
            else:
                value = students[inumber]
                name = value[NAME_INDEX]
                print (name)
    
def read_dictionary(filename, key_column_index):
    dictionary = {}
    with open(filename,"rt") as csv_file:
        reader = csv.reader(csv_file)
# The next() function returns the next item in an iterator.
        next(reader)

        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
        return dictionary

if __name__ == "__main__":
    main()

# ignorar a primeira linha de texto do arquivo, pois ela contém apenas cabeçalhos,
# e ler as outras linhas do arquivo em um dicionário. O programa deve armazenar
# cada I-Number do aluno como uma chave e cada par de nome do I-Number ou cada
# nome como um valor no dicionário.

# Obter um I-Number do usuário, usar o I-Number para localizar o nome do aluno
# correspondente no dicionário e imprimir o nome.

# Se um usuário digitar um I-Number que não exista no dicionário, seu programa
# deverá imprimir a mensagem "No such student" (sem as aspas).
