import threading
import time

def countdown_timer(seconds):
    while seconds > 0:
        print("Sisa waktu:", seconds, "detik")
        time.sleep(1)
        seconds -= 1
    print("Waktu habis!")

def main():
    seconds = int(input("Masukkan jumlah detik: "))
    thread = threading.Thread(target=countdown_timer, args=(seconds,))
    thread.start()

if __name__ == '__main__':
    main()