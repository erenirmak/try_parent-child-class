class Mat_Islemleri():
    def __init__(self, num1, num2, op = "+"):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        self.result = 0

        if self.op == "+":
            self.topla()
        if self.op == "-":
            self.cikar()
        if self.op == "*":
            self.carp()
        if self.op == "/":
            self.bol()

    def topla(self):
        self.result = self.num1 + self.num2
        return self.result

    def cikar(self):
        self.result = self.num1 - self.num2
        return self.result 

    def carp(self):
        self.result = self.num1 * self.num2
        return self.result

    def bol(self):
        self.result = self.num1 / self.num2
        return self.result

class Aritmetik(Mat_Islemleri):
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2
        self.sum = 0
        #self.count = 1
        self.ave = 0
        self.aritmetik_ort()

    def topla(self):
        if self.num1 != self.num2 + 1:
            self.sum = self.sum + self.num1
            self.num1 = self.num1 + 1
            return self.topla()
        else:
            return self.sum

    def countr(self):
        count = self.num2 - self.num1 + 1
        return count

    def aritmetik_ort(self):
        obj = Mat_Islemleri(self.countr(), self.topla(), "/")
        self.ave = obj.result**(-1)
        return self.ave