from main import ParkingLot

while True:
    try:
        s = [str(i) for i in input().split()]
        if s[0] == 'create_parking_lot':
            p = ParkingLot(int(s[1]))
            p.createSlots(int(s[1]))
        elif s[0] == 'park':
            p.addCar(s[1] ,s[2])
        elif s[0] == 'leave':
            p.leaveCar(int(s[1]))
        elif s[0] == 'status':
            p.status()
        elif s[0] == 'registration_numbers_for_cars_with_colour':
            p.getColorRegestration(s[1])
        elif s[0] == 'slot_numbers_for_cars_with_colour':
            p.getColorSlots(s[1])
        elif s[0] == 'slot_number_for_registration_number':
            p.slotNumber(s[1])
    except:
        break
