from math import *

import numpy as np


def get_dividers(nb: int):
    list_dividers = []
    for d in range(1, nb + 1):
        if nb % d == 0:
            list_dividers.append(d)
    return list_dividers


def is_prime(nb: int):
    if nb < 2:
        return False
    for d in range(2, nb):
        if nb % d == 0:
            return False
    return True


def get_prime_list(inf: int, sup: int):
    prime_list = []
    for nb in range(inf, sup + 1):
        if is_prime(nb):
            prime_list.append(nb)
    return prime_list


def get_prime_dividers(nb: int):
    divider_list = []
    for divider in get_dividers(nb):
        if is_prime(divider):
            divider_list.append(divider)
    return divider_list


def is_sg_prime(nb: int):
    if is_prime(nb) and is_prime(nb * 2 + 1):
        return True
    else:
        return False


def get_list_sg_prime(inf: int, sup: int):
    sg_list = []
    for i in range(inf, sup + 1):
        if is_sg_prime(i):
            sg_list.append(i)
    return sg_list


def is_power(n: int, p: int):
    for i in range(1, n):
        if i ** p > n:
            return False
        elif i ** p == n:
            return True


liste = [1, 8, 12, 75, 6, 88, 2, 99, -100, 78, 87]


def mini(array: liste):
    mini_list = liste[0]
    for i in liste:
        if i < mini_list:
            mini_list = i
    return mini_list


def max(array: liste):
    max_list = liste[0]
    for i in liste:
        if i > max_list:
            max_list = i
    return max_list


value = {1: 1, 2: 1}


def fibonacci(n):
    global value
    if not n in value.keys():
        value[n] = fibonacci(n - 1) + fibonacci(n - 2)
    return value[n]


def fibona(n):
    liste_fibo = []
    a = 0
    b = 1
    while a < n:
        liste_fibo.append(a)
        a, b = b, a + b
    print(liste_fibo)


def bubble_sort(list):
    permutation = True
    while permutation:
        permutation = False
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                permutation = True
    return list


liste_alpha = [45, 87, 96, 41, 10, 54, 99]


def somme(liste):
    total = 0
    for number in liste:
        total += number
    return total


def moyenne(liste):
    total = 0
    note_number = len(liste)
    for number in liste:
        total += number
        moyenne = total / note_number
    print(moyenne)


def lenght(liste):
    total = 0
    for i in liste:
        total += 1
    return total


def puissance(n, p):
    if p == 0:
        return 1
    elif p == 1:
        return n
    else:
        n = n ** p
    return n


def puissance_total(a, p):
    if p == 0:
        return 1
    else:
        total = 1
        if p > 0:
            for i in range(p):
                total *= a
        else:
            for i in range(abs(p)):
                total *= (1 / a)
        return total


def somme_total_puissance(n, k):
    total = 0
    for i in range(k + 1):
        total += n ** i
    return total


list_a = [5, 8, 9, 10, 41, 8]
list_b = [44, 87, 97, 107, 417]


def concat_list(a, b):
    new_list = []
    for i in (a, b):
        new_list += i
    return new_list


def find_index(list, to_find):
    for i, element in enumerate(list):
        if element == to_find:
            return i
    return -1


def occurence(liste, search):
    total = 0
    for i in liste:
        if i == search:
            total += 1
    return total


list_string = ["a", "b", "c", "d"]


def pyjoin(char, list):
    final_string = str()
    length = len(char)
    for element in list:
        final_string = final_string + element + char
    if length == 0:
        return final_string
    else:
        return final_string[:-length]


def convert(seconde):
    heure = seconde // 3600
    seconde = seconde - 3600 * heure
    minute = seconde // 60
    seconde = seconde - minute * 60

    return f"{heure} heures {minute} minutes et {seconde} secondes"


jour_de_la_semaine = ["Lundi",
                      "Mardi",
                      "Mercredi",
                      "Jeudi",
                      "Vendredi",
                      "Samedi",
                      "Dimanche"]

joueurs = ["Sarah", "Lucie", "Antoine", "Olivier"]

"""cesar = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
         "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]"""


def cryptage(key, letter):
    if 65 <= ord(letter) <= 90:
        return chr(65 + (ord(letter) - 65 + key) % 26)
    elif 97 <= ord(letter) <= 122:
        return chr(97 + (ord(letter) - 97 + key) % 26)
    return letter


def decryptage(key, letter):
    if 65 <= ord(letter) <= 90:
        return chr(65 + (ord(letter) - 65 - key) % 26)
    elif 97 <= ord(letter) <= 122:
        return chr(97 + (ord(letter) - 97 - key) % 26)
    else:
        return letter


def cesar(key, mot):
    a = ""
    for lettre in mot:
        a += cryptage(key, lettre)
    return a


def cesar_decrypte(key, mot):
    a = ""
    for lettre in mot:
        a += decryptage(key, lettre)
    return a


def decrypte_force(letter):
    pass_force = ""
    for i in range(1, 26):
        pass_force += cesar_decrypte(i, letter) + "\n"
    print(pass_force)


def construct_matrix():
    row = int(input("ENtrer le nombre de lignes : "))
    col = int(input("ENtrer le nombre de colonnes : "))
    A = []

    for i in range(row):
        A.append([0] * col)
        print(A)
        for j in range(col):
            A[i][j] = int(input("Entrez les elements de la matrice :"))
            print(A)
    print(A)


alphabet1 = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
             "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

alphabet2 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def rot13_chiffrement(text):
    text = text.upper()
    result = ""
    for char in text:
        if char.isalpha():
            result += alphabet2[(alphabet2.index(char) + 13) % 26]
        else:
            result += char
    return result


def suivant(n: int):
    if n == 1:
        return n
    else:
        if n % 2 == 0:
            return n / 2
        else:
            return n * 3 + 1


def collatz(n):
    c = 0
    while n != 1:
        c += 1
        n = suivant(n)
    return c


def max(n):
    L = []
    L.append(n)
    max = n
    while n != 1:
        n = suivant(n)
        L.append(round(n))
        if n > max:
            max = n
    return round(max), L


def start_algo_collatz():
    print("***Algorithme Lancé***")
    print("Entrer un nombre positif")
    print("Entrer n :")
    n = int(input())
    print(f"Le nombre d'étapes est : {collatz(n)}")
    result = max(n)
    print(f"La plus grande valeur est : {result[0]}")
    print(f"La liste de nombres encontrés est : {result[1]}")


def collatz_final(NbrEtape):
    n = 2
    while collatz(n) != NbrEtape:
        n += 1
    print(f"Nombre d'étape : {NbrEtape}")
    print(f"N = {n}")
    print(f"Le plus grand nombre rencontrer : ")
    result = max(n)
    print(f"La plus grand nombre est : {result[0]}")


def pgcd():
    while True:
        A = int(input("Entrer le nombre A"))
        B = int(input("Entrez le nombre B"))
        if A > 0 and B > 0:
            break
    if A > B:
        x = A
        y = B
    else:
        x = B
        y = A
    while x % y != 0:
        r = x % y
        x = y
        y = r
    print(f"Le pgcd de {A} et de {B} est {y}")


a = np.array([1,2,3,4])
b = np.array([1,2,3,4])
print(a+b)