########################################################
#Author Ritshdize Nemudzivhaidi
#Date: 2022-09-24
#Description: Luhn Algorithm for South African ID numbers
#Version: 1.0
#Usage: python3 Luhn_Algorithm.py
#########################################################
import datetime

class luhn:
    #construction that accepts only id throws error if not 13 digits
    def __init__(self,id_):
        self.id_ = str(id_)
        
        if len(self.id_) < 13 or len(self.id_) > 13:
            raise Exception("ID number must be 13 digits long")
        
        else:
            # C denotes that the citizen is a south african or a permanent resident 0 = south african 1 = permanent resident
            self.c = self.id_[10:11]
            pass
    #creating female numbers from 0000 to 4999 #array []
    def female(self):
        self.female_num = []
        self.female_num.append('0000')
        self.ones = '000'
        self.tens = '00'
        self.hundreds = '0'
        
        for i in range(1,5000):
            self.i_s = str(i)

            if i < 10:
                self.female_num.append(self.ones+self.i_s)
            
            elif i < 100:
                self.female_num.append(self.tens+self.i_s)
            
            elif i < 1000:
                self.female_num.append(self.hundreds+self.i_s)
            
            else:
                self.female_num.append(self.i_s)

    #creating male numbers from 5000 to 9999
    def male(self):
        self.male_num = [male for male in range(5000,10000)]
    
    #extract odd number from the id
    def odd_(self):
        self.odd = [odd for odd in range(0,12,2)]
        self.odd_answer  = 0
    
    #extract even  number from the id
    def even_(self):
        self.even = [even for even in range(1,13,2)]
        self.even_answer = ''
    #LUHN algo calculations 
    def calc(self):
        #for odd numbers
        for i in self.odd:
            self.odd_answer = self.odd_answer + int(self.id_[i])

        #for even numbers 
        for i in self.even:
            self.even_answer += self.id_[i]
        
        #multiply even numbers by 2
        self.even_answer = str(int(self.even_answer)*2)
        
        #add odd and even numbers
        self.even_answer_final = 0
        for i in self.even_answer:
            self.even_answer_final += int(i)
        self.final_digit  = self.odd_answer + self.even_answer_final
        
        #id validation number
        self.id_validation = 0
        if len(str(self.final_digit)) == 2:
            self.id_validation = int(self.final_digit[-1])
        
        elif len(str(self.final_digit)) == 1:
            self.id_validation = int(self.final_digit)
        
        #check this error out for mistakes that you have done !!!
        else:
            raise Exception("ID number is invalid")
    #date of birth
    def dob(self):
        self.sex = self.id_[6:10]
        self.year = self.id_[0:2]
        self.month = self.id_[2:4]
        self.day = self.id_[4:6]

        #changing the 2 digit year to full year amnont
        self.year = datetime.datetime.strptime(self.year, '%y').strftime('%Y')
        
        dob = f'{self.year}-{self.month}-{self.day}'
        return dob
    #check if the citizen is south african or permanent resident
    def citizen(self):
        if self.c == '0':
            return 'Citizen'
        
        elif self.c == '1':
            return 'Permanent Resident'
        
        else:
            return 'Invalid citizenship status'
    
    #validatioin for south african ID
    def validation(self):
        
        if self.id_validation == int(self.id_[-1]):
            return 'Valid ID number'
        else:
            return 'Invalid ID number'
    
    
    #Gender determination
    def gender_determination(self):
        
        for i in self.female_num:
            if str(i) == self.sex:
                return "Female"
        
        for i in  self.male_num:
            if str(i) == self.sex:
                return "Male"
        

#example = luhn('8001015009087')