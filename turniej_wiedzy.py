import sys


def open_file(file_name, mode):
    """Otwórz plik"""
    try:
        the_file = open(file_name, mode)
    except IOError as e:
        print("Nie można otworzyć pliku", file_name, "\nProgram zostanie zakończony.\n", e)
        input("\n\nAby zakończyć program, naciśnij klawisz Enter")
        sys.exit()
    else:
        return the_file


def next_line(the_file):
    """Zwróć kolejny wiersz pliku kwiz po sformatowaniu go"""
    line = the_file.readline()
    line = line.replace("/", "\n")
    return line


def next_block(the_file):
    """Zwróć kolejny blok danych z pliku kwiz."""
    category = next_line(the_file)
    question = next_line(the_file)
    answers = []
    for i in range(4):
        answers.append(next_line(the_file))
    correct = next_line(the_file)
    if correct:
        correct = correct[0]
    explanation = next_line(the_file)

    return category, question, answers, correct, explanation


def welcome(title):
    """Przywitaj gracza"""
    print("\t\tWitaj w turnieju wiedzy!\n")
    print("\t\t", title, "\n")


def main():
    trivia_file = open_file("kwiz.txt", "r")
    title = next_line(trivia_file)
    welcome(title)
    score = 0
    category, question, answers, correct, explanation = next_block(trivia_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print("\t", i + 1, "-", answers[i])
        answer = input("Jaka jest Twoja odpowiedź?: ")
        if answer == correct:
            print("\nOdpowiedź prawidłowa!", end=" ")
            score += 1
        else:
            print("\nOdpowiedź niepoprawna.", end=" ")
        print(explanation)
        print("Wynik:", score, "\n\n")
        category, question, answers, correct, explanation = next_block(trivia_file)

    trivia_file.close()

    print("To było końcowe pytanie!")
    print("Twój końcowy wynik wynosi", score)


main()
input("\n\nAby zakończyć program, naciśnij klawisz Enter")