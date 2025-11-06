from varasto import Varasto

def funktio_jolla_liikaa_argumentteja(arg1, arg2, arg3, arg4, arg5, arg6):
    """Tämä funktio rikkoo max-args -sääntöä."""
    print(f"Rikottiin max-args: {arg1}{arg2}{arg3}{arg4}{arg5}{arg6}")


def main():
    
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:")
    print(f"Mehuvarasto: {mehua}")

    
     print(f"Olutvarasto: {olutta}")

    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

   
    print("Rikotaan max-nested-blocks:")
    for i in range(1): 
        if i >= 0: 
            if i >= 0: 
                print("Tämä on kolmas sisennystaso ja rikkoo säännön.")

    
    funktio_jolla_liikaa_argumentteja(1, 2, 3, 4, 5, 6)

    print("Tämä on tahallaan erittäin, erittäin, ERITTÄIN pitkä rivi, joka on suunniteltu vain ja ainoastaan rikkomaan Pylintin 80 merkin pituinen max-line-length -sääntö, jotta näemme 'line-too-long' -virheilmoituksen.")


if __name__ == "__main__":
    main()