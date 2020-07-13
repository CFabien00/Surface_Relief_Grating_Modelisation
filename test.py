import unittest

from grating import *


class GratingTest(unittest.TestCase):

    def setUp(self):
        self.srg_3 = SurfaceReliefGrating("data/3g.txt")
        self.grating_list = self.srg_3.get_list_of_grating(0)
        self.srg_surface = self.srg_3.get_stretched_surface(
            stretching=0, dimension=10, step=1)
        self.grating = SinusoidalGrating(1.5, 1, 0.5)
        self.grating_surface = self.grating.get_surface(dimension=10, step=0.1)

    def test_init(self):
        self.assertEqual(self.srg_3.nb_grating, 3)
        self.assertEqual(self.srg_3.nb_strech, 7)
        self.assertEqual(len(self.srg_3.pitches[0]), 3)
        self.assertEqual(len(self.srg_3.pitches), 7)
        self.assertEqual(len(self.srg_3.amplitudes[0]), 3)
        self.assertEqual(len(self.srg_3.amplitudes), 7)
        self.assertEqual(len(self.srg_3.angles[0]), 3)
        self.assertEqual(len(self.srg_3.angles), 7)

    def test_list_of_gratings(self):
        self.assertEqual(len(self.grating_list), 3)
        self.assertEqual(self.grating_list[0].pitch, 0.695692302)
        self.assertEqual(self.grating_list[0].amplitude, 1)
        self.assertEqual(self.grating_list[0].angle, 1.46323095)

    def test_get_stretched_surface(self):
        self.assertEqual(int(self.srg_surface[0][0]), 0)
        self.assertEqual(int(self.srg_surface[-1][0]), 8)

    def test_get_surface(self):
        self.assertEqual(int(self.grating_surface[0][0]), 0)
        self.assertEqual(int(self.grating_surface[-1][-1]), 8)


if __name__ == "__main__":
    unittest.main()
