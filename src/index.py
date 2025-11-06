"""
Pääohjelma Varasto-luokan testaamiseen ja esittelyyn.
Refaktoroitu Pylintiä varten.
"""

from varasto import Varasto

def alusta_varastot():
    """Luo ja palauttaa mehu- ja olutvarastot."""
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)
    return mehua, olutta

def tulosta_varastot(otsikko, mehua, olutta):
    """Tulostaa varastojen tilan annetulla otsikolla."""
    print(otsikko)
    print(f"Mehuvarasto: {mehua}")
    print(f"Olutvarasto: {olutta}")

def testaa_getterit(olutta):
    """Testaa ja tulostaa olutvaraston getterit."""
    print("Olut getterit:")
    print(f"saldo = {olutta.saldo}")
    print(f"tilavuus = {olutta.tilavuus}")
    print(f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

def testaa_setterit(mehua):
    """Testaa ja tulostaa mehuvaraston setterit."""
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def testaa_virhetilanteet():
    """Testaa virheelliset alustusarvot."""
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def testaa_lisaykset(mehua, olutta):
    """Testaa ylisuuret ja negatiiviset lisäykset."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def testaa_oluen_otot(olutta):
    """Testaa oluen ylisuuret otot."""
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def testaa_mehun_otot(mehua):
    """Testaa mehun negatiiviset otot."""
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")

def main():
    """
    Käyttää Varasto-luokkaa ja tulostaa esimerkkitoimintoja.
    Tämä funktio on nyt alle 10 lausetta pitkä.
    """
    mehua, olutta = alusta_varastot()
    tulosta_varastot("Luonnin jälkeen:", mehua, olutta)
    testaa_getterit(olutta)
    testaa_setterit(mehua)
    testaa_virhetilanteet()
    testaa_lisaykset(mehua, olutta)
    # Jaettiin liian pitkä funktio (testaa_otot) kahdeksi
    testaa_oluen_otot(olutta)
    testaa_mehun_otot(mehua)

if __name__ == "__main__":
    main()