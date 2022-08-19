# Openhab icloud script
Script for getting data from icloud. This script is using pyicloud. This is layer for integration to openhab only.

## Installation and setup steps
1) Install library - [pyicloud](https://github.com/picklepete/pyicloud) pip install pyicloud - on the openhab server
2) Setup pyicloud on your server based on [documentation](https://github.com/picklepete/pyicloud). Pay attention - you have to run command under openhab user - for example "sudo - u openhab icloud --username=jappleseed@apple.com"
3) Install exec binding at openhab
4) Install jsontransformation binding at openhab
5) Copy icloud.py to your folder openhab/scripts
6) Update username at icloud.py
7) Create Things from exebinding as command and setup command - python /etc/openhab/scripts/icloud.py -l "your phone key"
8) You can create rule for run of this things or setup timer
9) Create Item for gps location
10) Create rule for update item gps location:
```java
rule "Location"
when 
    Item Location_Output received update 
then
    val mygps = transform("JSONPATH","$.localization.latitude",Location_Output.state.toString)+","+transform("JSONPATH","$.localization.longitude",Location_Output.state.toString)
    Location_Item.postUpdate(mygps)    
end
```

