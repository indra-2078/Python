import time

inp = input("Do you want the password to be strong,little weak or weak(S/lw/W): ")

spass = ["9MBmns4/H[*8^`c3", "!HYY@6%-5V7%jvby","ytm8-#zF&CGhxze3","tUn=!paXRWS6x@tz"]

if inp == "S" or inp =="s":
    for num in spass:
        print(num)
    time.sleep(1)
    a = input("Do you want to Save the passwords to a text file(Y/n)(make sure that the .txt file is in the desktop path)Y/n: ")
    if a == "Y" or a == "y":
        time.sleep(1)
        print("The file will be stored as ")
        b = open( "writed.txt" + "\n" )
        b.write(num)
    b.close()

