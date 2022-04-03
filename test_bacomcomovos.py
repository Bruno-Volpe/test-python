"""
TDD - Test driven development

Parte 1 - Criar teste e ver falahar - RED

Parte 2 - Criar o programa e ver o teste passar - GREEN

Parte 3 - Melhorar meu codigo - REFACTOR
"""

import unittest
from bacon_com_ovos import bacon_com_ovos


class TestBaconComOvos(unittest.TastCase):
    def tets_bacon_ovo_com_ovos_deve_levantar_assertion_error_se_nao_for_int(self):
        with self.assertRaises(AssertionError):
             bacon_com_ovos('m')

    def test_bacon_com_ovos_deve_retornar_bacon_com_ovos_se_entrada_for_multiplo_de_3_e_5(self):
        entradas = (15, 30, 45, 60)
        saida = 'Bacon com Ovos'

        for entrada in entrada
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'{entrada} nao retornou {saida}')

    def test_bacon_com_ovos_deve_retornar_passar_fome_se_entrada_nao_for_multiplo_de_3_e_5(self):
        entradas = (1, 2, 4, 7, 8)
        saida = 'Passar fome'

        for entrada in entrada
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'{entrada} nao retornou {saida}')

    def test_bacon_com_ovos_deve_retornar_bacon_se_a_entrada_for_mutipla_de_3(self)
        entradas = (3, 6, 9, 12, 18, 21)
        saida = 'Bacon'

        for entrada in entrada
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida,
                                 msg=f'{entrada} nao retornou {saida}')

      def test_bacon_com_ovos_deve_retornar_ovos_se_a_entrada_for_mutipla_de_5(self)
        entradas = (5, 10, 20, 25, 35, 40)
        saida = 'ovos'

        for entrada in entrada
            with self.subTest(entrada=entrada, saida=saida):
                self.assertEqual(bacon_com_ovos(entrada), saida, msg=f'{entrada} nao retornou {saida}')
    

unittest.main(verbosity=2)
