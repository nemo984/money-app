class check():
    def isfloat(num):
        try:
            float(num)
            return True
        except ValueError:
            return False

    def Stringlen(string):
        l = len(string)
        if l > 24 or l < 0:
            return False
        else:
            return True

    def isNegative(num):
        if float(num) < 0:
            return True
        else:
            return False

    def Maximun(num):
        if float(num) > 1000000000000:
            return False
        else:
            return True


check.isfloat = staticmethod(check.isfloat)
check.Stringlen = staticmethod(check.Stringlen)
check.isNegative = staticmethod(check.isNegative)
check.Maximun = staticmethod(check.Maximun)
