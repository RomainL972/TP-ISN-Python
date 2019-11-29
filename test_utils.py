import unittest
import utils

class UtilsTest(unittest.TestCase):

    """Test case utilisé pour tester les fonctions du module utils"""

    def test_divisible(self):
        """Teste le fonctionnement de la fonction 'utils.divisible'."""
        self.assertTrue(utils.divisible(10,2))
        self.assertFalse(utils.divisible(8,3))

        with self.assertRaises(TypeError):
            utils.divisible(5)
        with self.assertRaises(TypeError):
            utils.divisible(5, 4, 3)
        with self.assertRaises(TypeError):
            utils.divisible("b", 5)

    def test_divisors(self):
        """Teste le fonctionnement de la fonction 'utils.divisors'."""
        self.assertEqual([1, 2, 5, 10, 25, 50], utils.divisors(50))
        self.assertEqual([], utils.divisors(-5))
        self.assertEqual([1], utils.divisors(2, 1))

        with self.assertRaises(TypeError):
            utils.divisors(5, 4, 4)
        with self.assertRaises(TypeError):
            utils.divisors()
        with self.assertRaises(TypeError):
            utils.divisors("b", 5)

    def test_evenNumbers(self):
        """Teste le fonctionnement de la fonction 'utils.evenNumbers'."""
        self.assertEqual(utils.evenNumbers(), list(range(0,100,2)))
        self.assertEqual([2,4,6,8], utils.evenNumbers(2,9))

        with self.assertRaises(TypeError):
            utils.divisors(5, 4, 4)
        with self.assertRaises(TypeError):
            utils.divisors("b")

    def test_geometricSuite(self):
        """Teste le fonctionnement de la fonction 'utils.geometricSuite'."""
        self.assertEqual(utils.geometricSuite(2,2), [2,4,8,16,32,64,128,256,512,1024])
        self.assertEqual(utils.geometricSuite(5,5,3), [5,25,125])

        with self.assertRaises(TypeError):
            utils.divisors()
        with self.assertRaises(TypeError):
            utils.divisors(5, 4, 4)
        with self.assertRaises(TypeError):
            utils.divisors("b", 4)

    def test_toBinary(self):
        """Teste le fonctionnement de la fonction 'utils.toBinary'."""
        self.assertEqual(utils.toBinary(42), "101010")
        self.assertEqual(utils.toBinary(-5), "-101")

        with self.assertRaises(TypeError):
            utils.toBinary()
        with self.assertRaises(TypeError):
            utils.toBinary(5, 2)
        with self.assertRaises(TypeError):
            utils.toBinary("5")

    def test_arrayToStr(self):
        """Teste le fonctionnement de la fonction 'utils.arrayToStr'."""
        self.assertEqual(utils.arrayToStr([50, 25]), "50 et 25")
        self.assertEqual(utils.arrayToStr([42]), "42")
        self.assertEqual(utils.arrayToStr([5, 789, 32]), "5, 789 et 32")
        self.assertEqual(utils.arrayToStr("test"), "t, e, s et t")

        with self.assertRaises(TypeError):
            utils.arrayToStr([5], [8])
        with self.assertRaises(TypeError):
            utils.arrayToStr()
