import sys
from main import ParkingLot

sys.stdin = open('input.txt','r')
sys.stdout = open('output.txt','w')

while True:
    try:
        s = [str(i) for i in input().split()]
        if s[0] == 'create_parking_lot':
            p = ParkingLot(int(s[1]))
            p.createSlots(int(s[1]))
        elif s[0] == 'park':
            try:
                p.addCar(s[1] ,s[2])
            except:
                print('First create a Parking Lot')
        elif s[0] == 'leave':
            try:
                p.leaveCar(int(s[1]))
            except:
                print('First create a Parking Lot')
        elif s[0] == 'status':
            try:
                p.status()
            except:
                print('First create a Parking Lot')
        elif s[0] == 'registration_numbers_for_cars_with_colour':
            try:
                p.getColorRegestration(s[1])
            except:
                print('First create a Parking Lot')
        elif s[0] == 'slot_numbers_for_cars_with_colour':
            try:
                p.getColorSlots(s[1])
            except:
                print('First create a Parking Lot')
        elif s[0] == 'slot_number_for_registration_number':
            try:
                p.slotNumber(s[1])
            except:
                print('First create a Parking Lot')
    except:
        break
