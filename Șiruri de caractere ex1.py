# Realizați un program care citește de la tastatură un șir de caractere și afișează de câte ori apare litera "a" în text.

#Exemplu. Pentru "Mihai este la mare." se va afișa 3.
#Rezolvare. Simplu – folosind metoda count():

#s = input()
#print(s.count("a"))
#Exercițiu propus. Realizați un program similar care afișează de câte ori apare
#fiecare vocală din alfabetul englezesc în textul citit și apoi la final, totalul
#aparițiilor lor. Atenție la detalii – mai jos e stilizat puțin rezultatul:
print("Textul dumneavoastra este:")
a = str(input())
# a este variabiala pentru text
print("Vocale:")
print(("a - "), a.count("a") )
print(("e - "), a.count("e") )
print(("i - "), a.count("i") )
print(("o - "), a.count("o") )
print(("u - "), a.count("u") )
