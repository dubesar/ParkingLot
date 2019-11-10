import unittest 
from main import ParkingLot


class TestMain(unittest.TestCase):
    
    def test_createSlots(self):
        p = ParkingLot(6)
        result = p.occupied_no
        self.assertEqual(result,0)
    
    def test_addCar(self):
        p = ParkingLot(6)
        p.createSlots(6)
        p.addCar('5484-ADFE-DW45','White')
        result = p.occupied_no
        self.assertEqual(result,1)
    
    def test_leaveCar(self):
        p = ParkingLot(6)
        p.createSlots(6)
        p.addCar('5484-ADFE-DW45','White')
        p.leaveCar(1)
        result = p.occupied_no
        self.assertEqual(result,0)

if __name__ == '__main__':
    unittest.main()
