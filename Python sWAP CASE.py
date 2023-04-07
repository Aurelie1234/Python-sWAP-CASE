def swap_case(s):
     
    string = ''
    
    for i in s:
        
     if i.isupper() == True:
      string += i.lower()
        
     elif i.islower() == True:
      string += i.upper()
    
     elif i.isspace() == True:
      string += i
      
     elif i.isdigit() == True:
      string += i
       
     elif i.isalnum() == False:
      string += i
            
    return string
