import os    

def rename_file_names():    
    file_list=os.listdir(r"C:\Users\Dawn\Documents\UdacityPtyhon\prank")    
    print (file_list)    
    saved_path=os.getcwd()    
    print("current working direcorty is"+saved_path)    
    os.chdir(r"C:\Users\Dawn\Documents\UdacityPtyhon\prank")    
    remove="0123456789"    
    table=str.maketrans("","",remove)    
    for file_name in file_list:    
        os.rename(file_name,file_name.translate(table))    


rename_file_names()  
