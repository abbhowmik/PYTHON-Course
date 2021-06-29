class Train:
    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print(f'The name of the train is {self.name}')
        print(f'The seats availavle in the train are {self.seats}')

    def fareInfo(self):
        print(f'The price of each ticket is : Rs. {self.fare}')

    def bookTicket(self):
        if(self.seats > 0):
            print(
                f'Your ticket is booked! and your seat number in this train is {self.seats}')
            self.seats = self.seats - 1
        else:
            print('Sorry,,, this train is reserved and no seats available right now, Please contact to another train')


shatabdi = Train('Shatabdi Express: 90230', 500, 30)
shatabdi.getStatus()
shatabdi.bookTicket()
shatabdi.getStatus()


# class Train:
#     def __init__(self, name, ticketprice, avalseats):
#         self.name = name
#         self.ticketprice = ticketprice
#         self.avalseats = avalseats

#     def getStatus(self):
#         print(
#             f'The name of the train is {self.name}\nSeats available in this train is {self.avalseats}')
#         print(f'Per ticket price is Rs.{self.ticketprice}')

#     def bookTicket(self):
#         if self.avalseats > 0:
#             print(
#                 f'Your seat is booked** and your Seat No. is {self.avalseats}')
#         self.avalseats -= 1


# a = Train('Shatabdi Express', 500, 60)
# a.getStatus()
# a.bookTicket()
a.getStatus()
