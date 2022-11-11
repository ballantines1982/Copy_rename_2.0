from pilmeny import clear_scr
import random

class Bastu:
    celcius = 0
    
    def run(self):
        self.celcius = self.fahr_to_cel(self.input_fahr())
        if self.celcius < 82:
            return str(self.celcius) + "℃  grader är för kallt."
        elif self.celcius > 87:
            return str(self.celcius) + "℃  grader är för varmt."
        return str(self.celcius) + "℃  grader är lagom, Välkommen in i Bastun."
    
    
    def start_text(self):
        print("Välkommen till Bastun!")
        print("Ställ in en lagom temperatur")
        print("------------------------------\n")


    def input_fahr(self):
        while True:
            try:
                self.user_input = int(input("Ange Grader:     ℉\b\b\b\b\b"))
            except ValueError:
                print("Ingen siffra...")
            else:
                return self.user_input
            

    def fahr_to_cel(self, fahrenheit):
        if fahrenheit == 0:
            self.fahr_to_cel(self.overloaded())
            return self.celcius
        else:
            self.celcius = ((fahrenheit - 32)*5)/9
            self.cel_two_deci = round(self.celcius, 2)
            self.celcius = self.cel_two_deci
            return self.celcius

    def overloaded(self):
        random_cel = random.randint(50,220)
        return random_cel


if __name__ == '__main__':
    clear_scr()
    main_program = Bastu()
    main_program.start_text()
    
    while main_program.celcius < 82 or main_program.celcius > 87:
        print(main_program.run())



        

    