import code as x

x.create("vamsi",25)

x.create("src",70,3600) 

x.read("vamsi")

x.read("src")

x.create("vamsi",50)

x.modify("vamsi",55)

x.delete("vamsi")

t1=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t1.start()
t1.sleep()
t2=Thread(target=(create or read or delete),args=(key_name,value,timeout)) #as per the operation
t2.start()
t2.sleep()
