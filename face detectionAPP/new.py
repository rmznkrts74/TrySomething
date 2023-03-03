import threading

def print_numbers():
    for i in range(1, 11):
        print(i)

def print_letters():
    for letter in 'abcdefghij':
        print(letter)

# iki thread oluşturma
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

# her iki thread'ın başlatılması
t1.start()
t2.start()

# her iki thread'in işlerinin tamamlanmasının beklendiği kısım
t1.join()
t2.join()

print("Both threads have finished.")
