from luo_peli import LuoPeli


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        tyyppi = input()
        
        peli = LuoPeli.luo_peli(tyyppi)
         
        if not peli:
            break
        peli.pelaa()


if __name__ == "__main__":
    main()
