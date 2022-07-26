import os
plugins = {"diff": True, "camera": True, "lidar": False, "360_lidar": True}
with open(os.path.dirname(__file__) +'/../gazebo_plugins/config.yaml', mode='r', encoding='utf-8') as set:
    for (i, line) in enumerate(set):
        datas = line.strip().split(':')
        plugins[datas[0]] = datas[1]
        plugins = plugins
print(plugins)
for i in plugins:
    print(plugins[i])
    if(plugins[i] == "True"):
        print(i)
        