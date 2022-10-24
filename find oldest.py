#enter 'youngest' or 'oldest'  according to your question)
t=str(input('youngest or oldest:'))
goodu=int(input('enter goodu age:'))
lazy=int(input('enter lazy age:'))
murga=int(input('enter murga age:'))

if t=='oldest':
    def oldest(goodu,lazy,murga):
        if goodu>lazy and goodu> murga:
            print(' goodu is oldest')
        elif lazy> goodu and lazy>murga:
            print('lazy is oldest')    
        elif murga>goodu and murga>goodu:
            print('murga is oldest')
    oldest(goodu,lazy,murga)

elif t=='youngest':
    def youngest(goodu,lazy,murga):
        if lazy< goodu and lazy<murga: 
           print(' lazy is youngest')  
        elif goodu<lazy and goodu< murga: 
           print(' goodu is youngest') 
        elif murga<goodu and murga<goodu:
           print(' murga is youngest')  
    youngest(goodu ,lazy,murga)       
     