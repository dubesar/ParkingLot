class ParkingLot:
    def __init__(self,n): 
        self.n = n
        self.occupied_no = 0
        self.__slots = {}
        self.__colors = {}
    def createSlots(self,n):
        for i in range(1,self.n+1):
            self.__slots[i] = [0,0]
    def addCar(self,regestration_no,color):
        try:
            self.__colors[color].append(regestration_no)
        except:
            self.__colors[color] = [regestration_no]
        for i in range(1,self.n+1):
            if self.__slots[i] == [0,0]:
                self.__slots[i] = [regestration_no,color]
                self.occupied_no += 1
                print('Allocated slot number: ' + str(i))
                break
            else:
                continue
        if self.occupied_no == 0:
            print('Sorry, parking lot is full')
    def leaveCarByRegestration(self, regestration):
        for key in self.__slots:
            if self.__slots[key] == regestration_no:
                print('Slot number '+str(key)+' '+'is free')
                self.__slots[key] = [0,0]
                break
    def leaveCar(self,slotNumber):
        self.__slots[slotNumber] = [0,0] 
        print('Slot number '+str(slotNumber)+' '+'is free')
    def status(self):
        print('Slot No.'+'   '+'Regestration No'+'   '+'Color')
        for i in range(1,self.n+1):
            try:
                print(str(i)+'          '+(self.__slots[i])[0]+'     '+(self.__slots[i])[1])
            except:
                pass
    def slotsColor(self,color):
        print(','.join(self.__colors[color]))
    def slotNumber(self,regestration_no):
        p = 0
        for key in self.__slots:
            if (self.__slots[key])[0] == regestration_no:
                print(key)
                p+=1
                break
        if p==0:
            print('Not Found')
    def getColorSlots(self,color):
        for key in self.__slots:
            if (self.__slots[key])[1] == color:
                print(str(key),end=', ')
        print('')
    
    def getColorRegestration(self,color):
        for key in self.__slots:
            if (self.__slots[key])[1] == color:
                print(str((self.__slots[key])[0]),end= ', ')
        print('')
