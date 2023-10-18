import unittest
from carrigan_tire_service import CarriganTireService

class TestCarriganTireService(unittest.TestCase):
    def test_needs_service(self):
        tire_service = CarriganTireService()

        self.assertTrue(tire_service.needs_service([0.1, 0.8, 0.9, 0.95]))

        self.assertFalse(tire_service.needs_service([0.1, 0.8, 0.7, 0.6]))

if __name__ == '__main__':
    unittest.main()
