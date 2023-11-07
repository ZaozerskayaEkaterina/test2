#5.	Ввести строку, вывести на экран, но слова в обратном порядке, отсортированные по убыванию (asci code)

str = input("Enter string: ")

while True:
    try:      #операция, которая может вызвать исключение
        only_spaces = True
        for word in str:
            if word != ' ' and word != '\t':
                only_spaces = False
                break

        if only_spaces:
            print("Incorrect string. The string consists only of spaces or tab characters")
            str = input("Enter correct string: ")

        else:
            break

    except:
        break
words = str.split()       #список
words.sort(reverse=True)
print(' '.join(words))