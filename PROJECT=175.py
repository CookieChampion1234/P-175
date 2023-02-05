import matplotlib .pyplot as plt
import psutil as p
app_name_dict={"spider":10}
key=[]
max_min_list=[]
count=0
for process in p.process_iter():
    count = count + 1
    if count <= 10:
        name = process.name()
        cpu_usage = p.cpu_percent()
        print('name : ', name , '-- cpu_usage : ',cpu_usage)
        app_name_dict.update({name:cpu_usage})
        keymax=max(app_name_dict, key=app_name_dict.get)
        print(keymax)
        keymin=min(app_name_dict, key=app_name_dict.get)
        print(keymin)
        name_list=[keymax,keymin]
        print(name_list)
        app=app_name_dict.values()
        max_app=max(app)
        print(max_app)
        min_app=min(app)
        print(min_app)
        max_min_list=[max_app, min_app]
        key=[keymax,keymin]
        
plt.figure(figsize=(15,7))
plt.xlabel("min and max")
plt.ylabel("Usage")
plt.bar(key,max_min_list, width=0.6,color=("red","blue"))
plt.show()

