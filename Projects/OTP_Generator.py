import random

length = 6
otp = ""
while length>0:
    otp_Num = random.randint(0,9)
    otp = otp + str(otp_Num)
    length -= 1
print(otp)
