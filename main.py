class ParkingLot:
    def __init__(self,n): 
        self.n = n
        self.occupied_no = 0
        self.slots = {}
        self.colors = {}
    def createSlots(self,n):
        for i in range(1,self.n+1):
            self.slots[i] = [0,0]
    def addCar(self,regestration_no,color):
        try:
            self.colors[color].append(regestration_no)
        except:
            self.colors[color] = [regestration_no]
        for i in range(1,self.n+1):
            if self.slots[i] == [0,0]:
                self.slots[i] = [regestration_no,color]
                self.occupied_no += 1
                print('Allocated slot number: ' + str(i))
                break
            else:
                continue
        if self.occupied_no == 0:
            print('Sorry, parking lot is full')
    def leaveCarByRegestration(self, regestration):
        for key in self.slots:
            if self.slots[key] == regestration_no:
                print('Slot number '+str(key)+' '+'is free')
                self.slots[key] = [0,0]
                break
    def leaveCar(self,slotNumber):
        self.slots[slotNumber] = [0,0] 
        print('Slot number '+str(slotNumber)+' '+'is free')
    def status(self):
        print('Slot No.'+'   '+'Regestration No'+'   '+'Color')
        for i in range(1,self.n+1):
            try:
                print(str(i)+'          '+(self.slots[i])[0]+'     '+(self.slots[i])[1])
            except:
                pass
    def slotsColor(self,color):
        print(','.join(self.colors[color]))
    def slotNumber(self,regestration_no):
        p = 0
        for key in self.slots:
            if (self.slots[key])[0] == regestration_no:
                print(key)
                p+=1
                break
        if p==0:
            print('Not Found')
    def getColorSlots(self,color):
        for key in self.slots:
            if (self.slots[key])[1] == color:
                print(str(key),end=', ')
        print('')
    
    def getColorRegestration(self,color):
        for key in self.slots:
            if (self.slots[key])[1] == color:
                print(str((self.slots[key])[0]),end= ', ')
        print('')

p = ParkingLot(6)
p.createSlots(6) #Creating a slot for the cars

#adding the car using the regestration number and the color
p.addCar('KA-01-HH-1234' ,'White')
p.addCar('KA-01-HH-9999', 'White')
p.addCar('KA-01-BB-0001', 'Black')
p.addCar('KA-01-HH-7777', 'Red')
p.addCar('KA-01-HH-2701', 'Blue')
p.addCar('KA-01-HH-3141', 'Black')

#leave the car
p.leaveCar(4)

#Checking the status of the parking lot 
p.status()

#Adding more cars
p.addCar('KA-01-P-333', 'White')
p.addCar('DL-12-AA-9999','White')

#registration_numbers_for_cars_with_colour White
p.getColorRegestration('White')

#slot_numbers_for_cars_with_colour White
p.getColorSlots('White')

#slot_number_for_registration_number KA-01-HH-3141
#slot_number_for_registration_number MH-04-AY-1111
p.slotNumber('KA-01-HH-3141')
p.slotNumber('MH-04-AY-1111')
