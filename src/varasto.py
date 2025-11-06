"""
Tämä moduuli määrittelee Varasto-luokan,
joka mallintaa yksinkertaista varastoa.
"""

class Varasto:
    """
    Luokka mallintaa varastoa, jolla on tilavuus ja saldo.
    """
    def __init__(self, tilavuus, alku_saldo = 0):
        """
        Luo uuden varasto-olion.
        (Refaktoroitu Pylintiä varten)

        Args:
            tilavuus (float): Varaston maksimitilavuus.
            alku_saldo (float, optional): Varaston alkusaldo.
                Oletus 0.
        """
        if tilavuus > 0.0:
            self.tilavuus = tilavuus
        else:
            # virheellinen, nollataan
            self.tilavuus = 0.0

        # Alustetaan saldo __init__:ssä W0201-virheen korjaamiseksi
        self.saldo = 0.0

        # Ulkoistetaan saldon asetus omaan metodiin (max-statements-säännön takia)
        self._aseta_alkusaldo(alku_saldo)

    def _aseta_alkusaldo(self, alku_saldo):
        """Apumetodi alkusaldon turvalliseen asettamiseen."""
        if alku_saldo < 0.0:
            # virheellinen, nollataan
            self.saldo = 0.0
        elif alku_saldo <= self.tilavuus:
            # mahtuu
            self.saldo = alku_saldo
        else:
            # täyteen ja ylimäärä hukkaan!
            self.saldo = self.tilavuus

    def paljonko_mahtuu(self):
        """Palauttaa, paljonko varastoon mahtuu vielä tavaraa."""
        return self.tilavuus - self.saldo

    def lisaa_varastoon(self, maara):
        """
        Lisää tavaraa varastoon.
        Negatiiviset lisäykset jätetään huomiotta.
        Ylimenevä osa hukataan.
        """
        if maara < 0:
            return
        if maara <= self.paljonko_mahtuu():
            self.saldo = self.saldo + maara
        else:
            self.saldo = self.tilavuus

    def ota_varastosta(self, maara):
        """
        Ottaa tavaraa varastosta.
        Negatiiviset otot palauttavat 0.
        Jos yritetään ottaa enemmän kuin on, palautetaan kaikki mitä on.
        """
        if maara < 0:
            return 0.0
        if maara > self.saldo:
            kaikki_mita_voidaan = self.saldo
            self.saldo = 0.0

            return kaikki_mita_voidaan

        self.saldo = self.saldo - maara

        return maara

    def __str__(self):
        """Palauttaa varaston tilan merkkijonona."""
        # Rivitetty C0301 (line-too-long) -virheen korjaamiseksi
        return f"saldo = {self.saldo}, " \
               f"vielä tilaa {self.paljonko_mahtuu()}"