class Account:
    def __init__(self,acc_no,acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass

acc1 = Account(123,"abc")
print(acc1.acc_no)
print(acc1.__acc_pass )# should be private

# private banauna ko lagi __ (undscore) use garne ani rpivate hunxa
# class ko bhitra chai access hunxa baira chai hudena
