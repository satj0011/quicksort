
####Funkar inte på listastwocell
#from ListAsTwoCell import List

from ListAsArray import List

def quickSort(unsortedlist, cmpfunction):

        position = unsortedlist.first()

        #if len(unsortedlist)<=1
        if position == unsortedlist.end():
                return unsortedlist
        else:
                # "Pop" pivot
                pivpos=unsortedlist.first()
                pivotLIST=List()
                pivot=unsortedlist.inspect(pivpos)
                pivotLIST=pivotLIST.insert(pivpos,pivot)
                unsortedlist.remove(pivpos)                
        low=List()
        high=List()
        pos_low=low.first()
        pos_high=high.first()
        
        while position != unsortedlist.end():        
                value=unsortedlist.inspect(position)
                if cmpfunction(value,pivot):
                        low.insert(position=pos_low,obj=value)
                        #pos_low=low.next(pos_low)
                        position=unsortedlist.next(position)

                else:
                        high.insert(position=pos_high,obj=value)
                        #pos_high=high.next(pos_high)
                                
                        position=unsortedlist.next(position)
        
        low1=quickSort(low,cmpfunction) 
        high1=quickSort(high,cmpfunction)
        
        low1_pos= low1.first()
        high1_pos=high1.first()
        sortedlist=List()
        sortedpos=sortedlist.first()
        
        # Create sortedlist, first input low1 (lower than pivot)
        while low1_pos != low1.end(): 
                val=low1.inspect(low1_pos)
                sortedlist.insert(sortedpos,val)
                low1_pos=low1.next(low1_pos)
                sortedpos=sortedlist.next(sortedpos)
        
        # Insert Pivot in sortedlist
        sortedlist.insert(sortedpos,pivot)
        sortedpos=sortedlist.next(sortedpos)
        
        
        # insert all values from high, after pivot
        while high1_pos != high1.end():
                val=high1.inspect(high1_pos)
                sortedlist.insert(sortedpos,val)
                high1_pos=high1.next(high1_pos)
                sortedpos=sortedlist.next(sortedpos) 
        
        position=unsortedlist.first()
        unsortedlist.insert(position,pivot)
        return sortedlist
               
        
def printList(Listname):
        position= Listname.first()
        while position != Listname.end():
                        value=Listname.inspect(position)
                        print(value)        
                        position=Listname.next(position) 
                        

def sortLowFirst(val1,val2):
        if val1<val2:
                return True
        else:
                return False
                        
        
def sortHighFirst(val1,val2):
        if val1>val2:
                return True
        else:
                return False
        



#Skapa en lista
my_list=List()
        
#Fråga användaren efter namnet på datafilen
#Öppna datafilen
#f=open(input("Ange namnet på din fil: ",))
f=open("unsorted.txt","r")

#Läs igenom den rad för rad och lägg till raden till listan
# Read line-by-line using readline() in a while-loop
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




#Starta en loop som
#Frågar användaren om vad denne vill göra – det är ok att ha tre val, ett för varje sorteringsordning samt ett val för att avsluta.
# 1st= lista som ska sorteras

Userchoice=0
while Userchoice != 3:
        print("\n What do you want to do?")
        print("1: Sort list in decreesing order")
        print("2: Sort list in increesing order")
        print("3: EXIT")
        user_input=(input("Enter a number: ",))
        try:
                Userchoice=int(user_input)
                if Userchoice not in [1 , 2, 3]:
                        print("\n\n ERROR: you need to choose a number. 1,2 or 3.")                 
        except ValueError:
                print("\n\n ERROR: you need to choose a number. 1,2 or 3.")  
        if Userchoice ==1:       
                a=quickSort(my_list,sortLowFirst)
                print("Falling array is: ")
                printList(a) 
                Userchoice=0
        elif Userchoice==2:
                a=quickSort(my_list,sortHighFirst)
                print("Falling array is: ")
                printList(a)                 
                Userchoice=0
        elif Userchoice == 3:
                print("Thank you, we are done")

        