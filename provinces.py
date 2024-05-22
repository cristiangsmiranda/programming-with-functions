# Abra o arquivo provinces.txt para leitura.
# Leia o conteúdo do arquivo em uma lista em
# que cada linha de texto no arquivo é armazenada
# em um elemento separado na lista.

def main():
    provinces_list = read_list("provinces.txt")
    # Imprima a lista inteira.
    print(provinces_list)

# Remova o primeiro elemento da lista.
    provinces_list.pop(0)

# Remova o último elemento da lista.
    provinces_list.pop()

# Substitua todas as ocorrências de "AB" na lista por "Alberta".
    for i in range(len(provinces_list)):
        if provinces_list[i] =="AB":
            provinces_list[i] = "Alberta"

# Contar o número de elementos que são "Alberta" e imprimir esse número.
    count = provinces_list.count("Alberta")
    print(f"Alberta occurs {count} times in the modified list.")

def read_list(filename):
# Crie uma lista vazia que armazenará
# as linhas de texto do arquivo de texto.
        text_list = []

# Abra o arquivo de texto para leitura e armazene uma referência
# ao arquivo aberto em uma variável chamada text_file.        
        with open(filename, "rt") as text_file:

# Leia o conteúdo do arquivo de texto
# do arquivo, uma linha de cada vez.
            for line in text_file:

# Remove white space, if there is any,
# from the beginning and end of the line.
                clean_line = line.strip()

# Acrescente a linha limpa de texto
# no final da lista.
                text_list.append(clean_line)

# Retorna a lista que contém as linhas de texto.
        return text_list

if __name__ == "__main__":
    main()