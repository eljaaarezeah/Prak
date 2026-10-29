for hari in range(1,4):
    print("\n=== Latihan Hari ke -", hari, "===")

    total_pushup = 0

    while total_pushup < 50:
        tambahan = int(input("Berapa kali push-up yang baru saja Anda lakukan?"))
        total_pushup += tambahan
        print("Progres hari ini:", total_pushup, "/ 50")

    print("Selamat! Target push-up hari ke -", hari, "selesai.")