import unittest
from octoprime_tire_service import OctoprimeTireService

class TestOctoprimeTireService(unittest.TestCase):
    def test_needs_service(self):
        tire_service = OctoprimeTireService()

        self.assertTrue(tire_service.needs_service([1, 1, 0.5, 0.5]))

        self.assertFalse(tire_service.needs_service([0.8, 0.7, 0.5, 0.5]))

if __name__ == '__main__':
    unittest.main()
