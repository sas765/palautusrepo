import unittest
from unittest.mock import Mock, call, ANY

from kauppa import Kauppa
from tuote import Tuote


class TestKauppa(unittest.TestCase):
    def setUp(self):
        self.pankki_mock = Mock()
        self.viitegeneraattori_mock = Mock()
        self.viitegeneraattori_mock.uusi.return_value = 42

        self.varasto_mock = Mock()
        self.varasto_saldot = {1: 10, 2: 10}
        self.varasto_tuotteet = {
            1: Tuote(1, "maito", 5),
            2: Tuote(2, "leipä", 2),
        }
        self.varasto_mock.saldo.side_effect = self.varasto_saldot.get
        self.varasto_mock.hae_tuote.side_effect = self.varasto_tuotteet.get

        self.kauppa = Kauppa(
            self.varasto_mock,
            self.pankki_mock,
            self.viitegeneraattori_mock,
        )

    def test_maksettaessa_ostos_pankin_metodia_tilisiirto_kutsutaan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called()

    def test_maksettaessa_ostos_tilisiirtoa_kutsutaan_oikein_parametrein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_maksettaessa_usean_tuotteen_ostos_tilisiirtoa_kutsutaan_oikein_parametrein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 7
        )

    def test_maksettaessa_usean_saman_tuotteen_ostos_tilisiirtoa_kutsutaan_oikein_parametrein(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 10
        )

    def test_maksettaessa_loppuneen_tuotteen_ostos_tilisiirtoa_kutsutaan_oikein_parametrein(self):
        self.varasto_saldot[2] = 0

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.pankki_mock.tilisiirto.assert_called_with(
            "pekka", 42, "12345", "33333-44455", 5
        )

    def test_asioinnin_aloittaessa_edellisen_ostoksen_tiedot_nollataan(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("venni", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "venni", 42, "54321", "33333-44455", 5
        )

    def test_kauppa_pyytaa_uuden_viitenumeron_jokaiselle_maksutapahtumalle(self):
        self.viitegeneraattori_mock.uusi.side_effect = [1, 2, 3]

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("pekka", "12345")

        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(2)
        self.kauppa.tilimaksu("venni", "54321")

        self.assertEqual(
            self.pankki_mock.tilisiirto.call_args_list,
            [
                call(ANY, 1, ANY, ANY, ANY),
                call(ANY, 2, ANY, ANY, ANY),
                call(ANY, 3, ANY, ANY, ANY)
            ]
        )
    
    def test_tuote_poistuu_korista(self):
        self.kauppa.aloita_asiointi()
        self.kauppa.lisaa_koriin(1)
        self.kauppa.lisaa_koriin(2)
        self.kauppa.poista_korista(2)
        self.kauppa.tilimaksu("venni", "54321")

        self.pankki_mock.tilisiirto.assert_called_with(
            "venni", 42, "54321", "33333-44455", 5   
        )