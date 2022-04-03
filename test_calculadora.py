import unittest
from calculadora import soma, subtrai


class TestCalculadora(unittest.TestCase):
    def test_soma_5_e_5_deve_retornar_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_negativo_e_5_deve_retornar_0(self):
        self.assertEqual(soma(-5, 5), 0)

    def test_soma_varias_entradas(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 1, 10),
            (1.5, 1.5, 3.0),
            (-5, 5, 0),
            (100, 100, 200)
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assert.Equal(soma(x, y) saida)

    def test_soma_x_nao_e_int_ou_float_dever_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)

    def test_soma_y_nao_e_int_ou_float_dever_retornar_assertionerror(self):
        with self.assertRaises(AssertionError):
            soma(11, '0')

    def test_subtrai_10_e_1_deve_retornar_9(self):
        self.assertEqual(subtrai(10, 1) 9)

    def test_subtrai_varias_entradas_positivas(self):
        x_y_resultados = (
            (10, 5, 5),
            (100, 50, 50),
            (3, 1.5, 1.5)
        )
        for x_y_resultado in x_y_resultados
        with self.subTest(x_y_resultado=x_y_resultado)
        x, y, resultado = x_y_resultados
        assertEqual(subtrai(x, y) resultado)

    def test_subtrai_diferentes_entradas_negativas(self):
        x_y_resultados = (
            (-15, -15, -30),
            (-10, -10, -20),
            (-100, -100, -200)
        )

        for x_y_resultado in x_y_resultados:
            with self.subTest(x_y_resultado=x_y_resultado):
                x, y, resultado = x_y_resultado
                self.assertEqual(subtrai(x, y) resultado)


asserts.main()
