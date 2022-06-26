class NotWorking:
    def __init__(self, why, what_did_you_try, new_to_coding, willing_to_pay):
        self.why = why
        self.whatDidYouTry = what_did_you_try
        self.newToCoding = new_to_coding
        self.willingToPay = willing_to_pay

    def say_why_not_working(self):
        print(str(self.why))

    def say_what_user_did(self):
        print(self.whatDidYouTry)

    def help(self):
        if str(self.why):
            print("There is nothing we can do to help you my guy!!")

    def help_when_theyPay(self):
        solution = ""
        if self.willingToPay:
            # print("Okay, since you are willing to pay, we might actually have a solution hehehehe!!")
            solution = "You just have to delete matlab and re download it!"
            print(solution)
        else:
            solution = "Sorry, we do not have a solution; so we cannot help you"
            print(solution)


Emeka = NotWorking("UI Control shit in matlab", "I tried googling lol. I also changed my matlab credentials", False,
                   True)
Emeka.say_why_not_working()
Emeka.say_what_user_did()
Emeka.help_when_theyPay()
