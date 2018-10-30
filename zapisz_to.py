print("Utworzenie pliku tekstowego za pomocą metody write()")
text_file = open("zapisz_to.txt", "w")
text_file.write("Wiersz 1\n")
text_file.write("To jest wiersz 2\n")
text_file.write("Ten tekst tworzy wiersz 3\n")

text_file.close()

print("\nOdczytanie zawartości nowo utworzonego pliku.")
text_file = open("zapisz_to.txt", "r")
print(text_file.read())
text_file.close()
