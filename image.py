# f=open('IMG_.jpg','rb')
# # print(f.read())
# g=open('IMG.jpg','wb')

# for i in f:
#     g.write(i)

import os
if os.path.exists('IMG.jpg'):
    os.remove('IMG.jpg')
else:
    print('file does not exist')