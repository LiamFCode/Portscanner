#-----------------------------------------------------------------------------#
import nmap
import yaml
import json
import csv
import os
scanner = nmap.PortScanner()
#-----------------------------------------------------------------------------#       #---terminal-interface-&-config-grab--#
configNames = ['config1', 'config2', 'config3']
with open('config.yaml', 'r') as file:
    global allConfigs
    allConfigs = yaml.safe_load(file)
def terminalInput():
    selectedConfig = 0
    print("options:\n  config \n  run")
    mode = input('select mode: ')
    ###---[[[try catch]]]---###
    for i in range(1, len(configNames)+1):                                                 #---select-config---#
        print("  " + (str(allConfigs.get("config"+str(i), {}).get("name"))))
    configName = input('select config: ')
    selectionValid = False
    for i in range(1, len(configNames)):
        if configName == allConfigs.get("config"+str(i), {}).get("name"):
            selectedConfig = configNames[i-1]
            selectionValid = True
    if selectionValid != True:
        print('ERROR: name does not correspond to any configuration')
        terminalInput()
    match mode:
        case 'run':
            fileID = allConfigs['universalKeys']['id']
            dumpFile = allConfigs[selectedConfig].get('outputFileName', 'Scan-Results')
            fileType = allConfigs[selectedConfig].get('outputFileType', 'json')
            target = allConfigs[selectedConfig].get('targetIP')
            argListRaw = allConfigs[selectedConfig].get('script')
            argListUnfiltered = argListRaw.split()
            fileID+=1
            allConfigs['universalKeys'].update({'id':fileID})
            with open("config.yaml", "w") as file:
                yaml.safe_dump(allConfigs, file, sort_keys=False, allow_unicode=True)
            run(argListRaw, target, dumpFile, fileType, fileID)
        case 'config':                                                                      #---edit-config---#
            edit(selectedConfig)
#-----------------------------------------------------------------------------#       #---config-function-[improve-description-later]---#
def edit(selectedConfig):
    print(allConfigs[selectedConfig])
    changedValue = input('select value to edit: ')  #replace with if tree for each var in config
    newValue = input('enter new value: ')
    allConfigs[selectedConfig].update({changedValue: newValue})
    with open("config.yaml", "w") as file:
        yaml.safe_dump(allConfigs, file, sort_keys=False, allow_unicode=True) #---need-to-format-write-first---#
    exit = input('continue editting? Y or n\t')
    if exit == 'n':
        terminalInput()
    elif exit == 'Y':
        edit(selectedConfig)
#-----------------------------------------------------------------------------#       #---run-scan---#
def run(argListRaw, target, dumpFile, fileType, fileID):
    scanner.scan(target, arguments=(eval("'"+argListRaw+"'")))
    data = {"host":[],"hostname":[],"hostState":[],"protocol":[],"port":[],"portState":[]}
    for host in scanner.all_hosts():
        hostname = scanner[host].hostname()
        print("Host: %s (%s)" % (host, hostname))
        hostState = scanner[host].state()
        print("State: %s" % hostState)
        data["host"].append(host)
        data["hostname"].append(hostname)
        data["hostState"].append(hostState)
        for protocol in scanner[host].all_protocols():
            print("Protocol: %s" % protocol)
            port_info = scanner[host][protocol]
            data["protocol"].append(protocol)
            for port, state in port_info.items():
                print("Port: %s\tState: %s" % (port, state))
                portState = state
                data["port"].append(port)
                data["portState"].append(portState)
    print(data)
#-----------------------------------------------------------------------------#       #---output-dict-to-file---#
    if fileType == "json":
        with open(dumpFile + str(fileID) + "." + fileType, "x", encoding="utf-8") as file:
            json.dump(data, file, indent=4)
    elif fileType == "csv":
        with open(dumpFile + str(fileID) + "." + fileType, "x", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=['host', 'hostname', 'hostState', 'protocol', 'port', 'portState'], extrasaction='ignore')
            writer.writeheader()
            writer.writerow(data)
    elif fileType == "txt":
        with open(dumpFile + str(fileID) + "." + fileType, "x", encoding="utf-8") as file:
            json.dump(data, file, indent =4)
#-----------------------------------------------------------------------------#       #---init---#
terminalInput()
