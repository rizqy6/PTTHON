def wordCount(mystring):  
        tempcount = 0  
        count = 1  

        try:  
            for character in mystring:  
                if character == " ":  
                    tempcount +=1  
                    if tempcount ==1:  
                        count +=1  

                    else:  
                        tempcount +=1
                else:
                     tempcount=0

            return count  

        except Exception:  
             error = "Not a string"  
             return error  

mystring = "iki"

print(wordCount(mystring))