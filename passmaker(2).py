import os,sys,platform
words=str(input("ethods (a,b,c... if file , say : FiL321): "))
if words == "FiL321":
    while 1:
        try:
            pat=str(input("file path : "))
            words=open(pat,"r").readlines()
            break
        except:
            print("wrong file path.")
            sys.exit(0)
else:
    words=words.strip(" ").split(",")
output=str(input("output file : "))
if os.path.isfile(output):
    print("file already exist.")
    while 1:
        output=str(input("output file : "))
        if os.path.isfile(output):
            print("file already exist")
        else:
            break
o=open(output,"a")
lis = []
print("getting ready.")
def two():
    for i1 in words:
        for i2 in words:
            lis.append(i1+i2)
    print("done . generated "+str(len(lis))+" passwords.")
    print("making output file...")
    print("configuring output file...")
    for i in lis:
        o.write(i+"\n")
    print("output file cinfigured .")
def three():
    for i1 in words:
        for i2 in words:
            for i3 in words:
                lis.append(i1+i2+i3)
    print("done . generated "+str(len(lis))+" passwords.")
    print("making output file...")
    print("configuring output file...")
    for i in lis:
        o.write(i+"\n")
    print("output file cinfigured .")
def four():
    for i1 in words:
        for i2 in words:
            for i3 in words:
                for i4 in words:
                    lis.append(i1+i2+i3+i4)
    print("done . generated "+str(len(lis))+" passwords.")
    print("making output file...")
    print("configuring output file...")
    for i in lis:
        o.write(i+"\n")
    print("output file cinfigured .")
while True:
    plat = platform.platform().lower()
    if "linux" in plat:
        osd=os.popen("clear").read()
        print(osd)
    else :
        osd=os.popen("cls").read()
        print(osd)
    print("""
by : VIRUS TEAM
contact me: @virus00_0v3rw4tch3r_virus00
 ____________________________________________________________
/___________________________________________________________/|
|OPTION  |   LENGTH   |   OKAY FOR                         | |
|________|____________|____________________________________| |
|1       |     2      |accounts and servers with normal sec| |
|________|____________|____________________________________| |
|2       |     3      |servers and accounts with high sec  | |
|________|____________|____________________________________| |
|3       |     4      |     I don't know either !!!        | |
|________|____________|____________________________________|/
""")
    opt=str(input("option : "))
    opts=["1","2","3"]
    if opt in opts:
        if opt == "1" :
            two()
            break
        elif opt == "2":
            three()
            break
        elif opt == "3":
            four()
            break
input()
