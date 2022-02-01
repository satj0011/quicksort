
from ListAsTwoCell import List

my_list=List()


f=open("unsorted.txt","r")


line = f.readline()
position=my_list.first()
while line:
        line=float(line.rstrip())
        #check if the value thats added is float
        #check_float = isinstance(line, float)
        #print(check_float)

        my_list.insert(position=position, obj=line)
        line = f.readline()
        while position != my_list.end():
                position=my_list.next(position)

        
f.close()

""" Print List
position= my_list.first()
while position != my_list.end():
                value=my_list.inspect(position)
                print(value)        
                position=my_list.next(position) 
"""
                

def quickSort(unsortedlist, cmpfunction):
        pivpos=unsortedlist.first()
        pivot=unsortedlist.inspect(pivpos)
        unsortedlist.remove(pivpos)
        position = unsortedlist.first()
        low=List()
        high=List()
        pos_low=low.first()
        pos_high=high.first()
        
      
        
        while position != unsortedlist.end():
                        value=unsortedlist.inspect(position)
                        if cmpfunction(value,pivot):
                                low.insert(position=pos_low,obj=value)
                                #pos_low=low.next(pos_low)

                        else:
                                high.insert(position=pos_high,obj=value)
                                #pos_high=high.next(pos_high)
                                
                        position=unsortedlist.next(position)
                        
        low.insert(position=pos_low,obj=pivot)
        
        #quickSort(low,sortLowFirst)
        #quickSort(high,sortLowFirst)
        
        position= low.first()
        while position != low.end():
                        value=low.inspect(position)
                        print(value)        
                        position=low.next(position)
        
        position= high.first()
        while position != high.end():
                        value=high.inspect(position)
                        print(value)        
                        position=high.next(position) 
        

def sortLowFirst(val1,val2):
        if val1<val2:
                return True
        else:
                return False

quickSort(my_list,sortLowFirst)        




