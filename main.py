class ParkingLot:
    def __init__(self,n): 
        self.n = n
        self.occupied_no = 0
        self.__slots = {}             #For maintaining the slots along with color and regestration number (private dictionary)
        self.__colors = {}            #For maintaing the colors for every regestration number (private dictionary)
    def createSlots(self,n):
        for i in range(1,self.n+1):
            self.__slots[i] = [0,0]                   #Initialising each slot with 0,0 where first index is for regestration number and second for color
    def addCar(self,regestration_no,color):         #Function for adding a car in the parking slot
        try:
            self.__colors[color].append(regestration_no)
        except:
            self.__colors[color] = [regestration_no]
        for i in range(1,self.n+1):
            if self.__slots[i] == [0,0]:
                self.__slots[i] = [regestration_no,color]
                self.occupied_no += 1                      #number of occupied places in the parking slot (have kept it public so that anytime can be accessible)
                print('Allocated slot number: ' + str(i))
                break
            else:
                continue
        if self.occupied_no == 0:
            print('Sorry, parking lot is full')
    def leaveCarByRegestration(self, regestration):           #Function for car leave from a slot and can be used to show its regestration number
        for key in self.__slots: 
            if self.__slots[key] == regestration_no:
                print('Slot number '+str(key)+' '+'is free')
                self.__slots[key] = [0,0]
                break
    def leaveCar(self,slotNumber):                    #Function for slotNumber from which the car is leaving
        self.__slots[slotNumber] = [0,0] 
        print('Slot number '+str(slotNumber)+' '+'is free')
    def status(self):                                 #Status of the parking lot
        print('Slot No.'+'   '+'Regestration No'+'   '+'Color')
        for i in range(1,self.n+1):
            try:
                print(str(i)+'          '+(self.__slots[i])[0]+'     '+(self.__slots[i])[1])
            except:
                print('parking lot is empty')
    def slotsColor(self,color):          #Function showing the regestration numbers of a particular number
        print(','.join(self.__colors[color])) 
    def slotNumber(self,regestration_no):        #Function showing the slot number of a particular car
        p = 0 
        for key in self.__slots:
            if (self.__slots[key])[0] == regestration_no:
                print(key)
                p+=1
                break
        if p==0:
            print('Not Found')
    def getColorSlots(self,color):            #Function showing slot numbers of a particular color
        for key in self.__slots:
            if (self.__slots[key])[1] == color:
                print(str(key),end=', ')
        print('')
    def getColorRegestration(self,color):     #Function showing regestration numbers of a particular color
        for key in self.__slots:
            if (self.__slots[key])[1] == color:
                print(str((self.__slots[key])[0]),end= ', ')
        print('')
