from varasto import Varasto

def alusta_varastot():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def tulosta_varastot(otsikko, mehua, olutta):
    print(otsikko)
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def testaa_getterit(olutta):
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def testaa_setterit(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def testaa_virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def testaa_ylivuodot_ja_negatiiviset(mehua, olutta):
    tulosta_varastot(f"Olutvarasto: {olutta}", mehua, olutta)
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

def main():
    mehua, olutta = alusta_varastot()
    tulosta_varastot("Luonnin jälkeen:", mehua, olutta)
    testaa_getterit(olutta)
    testaa_setterit(mehua)
    testaa_virhetilanteet()
    testaa_ylivuodot_ja_negatiiviset(mehua, olutta)

if __name__ == "__main__":
    main()