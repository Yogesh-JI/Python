# try:
#     this block of code will run and throw errors if there are any


# except:
#     this will raise the errors


# else:
#     this will execute if there are no errors


# finally:
#     this will execute regardless the result of try and except




# try:
#     f=open('fiboonachi.py','w')
#     try:
#         f.write('abc')
#     except:
#         print('error in the file')
#     finally:
#         f.close()
# except:
#     print('cant find the file')


a=5
if a<10:
    # raise Exception('value is less than 5')
     print('kjgu')

a=[546,46,54,64,645,654,5]
try:
    print(a[8])
except:
    print('index is out of range')