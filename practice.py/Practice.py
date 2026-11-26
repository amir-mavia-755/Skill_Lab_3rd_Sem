# print(bool(0.0))
# print(int(True))
# a=2+7j
# print(a)
# a=2+7J
# print(a)

# a={40,10,12,30,1}
# print(a,type(a))
# print(a[0])

# a={(10,20)}
# print(a)

# a={'a':[10,20,30],'b':40}
# print(a['a'][1])
# print(a['a'][-2])
# print(list(a.values())[0][1])

# a= { "a":[10,20,30], "b":20}
# print(list(a.values())[0][1])

# a = "Good Morning"

# b = a[2:4]
# c = a[-2:-4:-1]
# print(b)
# print(c)

# a="Hello"
# print(a[-2:-5:-1])
# print(a[-1:-6:-1])
# print(a[::-1])

# a = "Good Morning"
# print(a[1:6:2])
# print(a[5::3])
# print(a[-7::3])
# print(a[-2:-9:-3])

# a = eval(input("Enter a number: "))
# print(a, type(a))

# check if the length of list is 5 or not
# a = eval(input("Enter a list: "))
# if not isinstance(a, list):
#     print("The input is not a list.")
# else:
#     if len(a) == 5:
#         print("The length of the list is 5.")
#     else:
#         print("The length of the list is not 5.")

# print(   (ord('a') - 32))
# print(chr(ord('a') - 32))

# chr = eval(input("Enter a character: "))
# print("The ASCII value of charachter is: ", ord(chr))
# if "A" <= chr <= "Z":
#     print("The character is uppercase.")    
# elif "a" <= chr <= "z":
#     print("The character is lowercase.")
# else:
#     print("The character is not a letter.")

# user_name = "1GD25CS003"
# password = "BaBeS@123"
# un = input("Enter your username: ")
# if (un == user_name):
#     pw = input("Enter your password: ")
#     if (pw == password):
#         print("Login Successful")
#     else:
#         print("Incorrect password")
#         exit()
# else: print("Incorrect username")
# exit()

# i = 0
# while i<= 50:
#     if i % 2 == 0:
#         print(i, "even")
#     i +=1/

# a = input("Enter a number: ")
# print(type(a))
# b = a[::-1]
# print(b)

# to print the reverse of a number
# n = int(input("Enter a number: "))
# rev = 0
# while n > 0:
#     ld = n % 10
#     n = n // 10
#     rev = rev * 10 + ld
# print("Reverse number is: ", rev) 


# for i in range(1,101):
#     print(i, end=" ")


# for i in range(1, 50):
#     if i % 2 == 0:
#         print(i, "even")

# l = [10, 20, 30]
# for i in l:
#     print(i)

# convert uppercase to lowercase and vice versa
# s = input("Enter anything: ")
# out = ' '

# for i in s:
#     if 'A' <= i <= 'Z':
#         out += chr(ord(i) + 32)
#     elif 'a' <= i <= 'z':
#         out += chr(ord(i) - 32)
#     else:
#         out += i
# print("Output:", out)


# reverse a string without using slicing
# s = input("Enter a string: ")
# rev = ''
# for i in  s:
#     rev = i + rev
# print("Output:", rev)


# nested for loop to print a pattern
    # for i in range(1, 6):
    #     for j in range(1, 6):
    #         print(' * ', end=' ')
    #     print()

    # for i in range(1, 6):
    #     for j in range(1,6):
    #         if i == j:
    #             print('*', end=' ')
    #         else:
    #             print(' ', end=' ')
    #     print()
    # print()
    # for i in range(1,6):
    #     for j in range(1,6):
    #         if i > j:
    #             print('*', end=' ')
    #         else:
    #             print(' ', end=' ')
    #     print()

    # for i in range(1,6):
    #     for j in range(1,6):
    #         if i < j:
    #             print('*', end=' ')
    #         else:
    #             print(' ', end=' ')
    #     print()


# a = "Happy birthday"
# print(a[-4:-7:-1])


# def convert(s,out):
#     for i in s:
#         if 'a' <= i <= 'z':
#             out += chr(ord(i)-32)
#         else:
#             out += i
#     return out
# print(convert(input("Enter a string: "), ' '))


# def convert(s,out):
#     for i in s:
#         if 'a' <= i <= 'z':
#             out += chr(ord(i)-32)
#         else:
#             out += i
#     print(out)
# convert(input("Enter a string: "), ' ')

# class COLLEGE:
#     clg_name= 'GCEM'
#     clg_loc= 'Hoodi'
# s1 = COLLEGE()
# print(s1.clg_name, s1.clg_loc)

# print(COLLEGE.clg_name)

# COLLEGE.clg_loc = 'KR puram'
# print(COLLEGE.clg_loc)
# print(s1.clg_loc)

# s1.clg_name = 'Hoodi'
# print(s1.clg_name)
# class COLLEGE:
#     clg_name= 'GCEM'
#     clg_loc= 'Hoodi'
    

# s1 = COLLEGE()
# s1.sname = 'Harish'
# s1. phno = 1234567890

# s2 = COLLEGE()
# s2.sname = 'Girish'
# s2.phno = 987654321

# print(s1.clg_loc)
# s1.clg_loc = 'KR Puram'
# print("After changing")
# print(s1.clg_loc)
# print(s2.clg_loc)
# print(COLLEGE.clg_loc)


class COLLEGE:
    def __init__(self, name, phone, usn):
        self.name = name
        self.phone = phone
        self.usn = usn
    def dis(self):
        print(self.name,self.phone,self.usn)
    def edit_name(self, new_name):
        self.name = new_name
    def edit_ph(self, new_ph):
        self.phone = new_ph
    @classmethod
    def display():
        pass
    
s1 = COLLEGE('Harish', 1234, '1GD001')
s2 = COLLEGE('Nirish', 5678, '1GD002')
s1.dis()
s2.dis()
s1.edit_name('Hareesh')
s1.edit_ph(2345)
s1.dis()
