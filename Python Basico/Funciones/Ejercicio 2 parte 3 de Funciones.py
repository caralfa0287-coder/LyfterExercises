variable = 8

def modify_global_variable():
    global variable
    variable *= 2   
    print (variable)

modify_global_variable()