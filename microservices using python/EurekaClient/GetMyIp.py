import os

def getMyIp():
    try:
        output=os.popen('ipconfig /all')
        output=output.read().split("\n")
        ipv4=list(filter(lambda x:"IPv4 Address" in x,output))[0].strip()
        return (ipv4[36:49])
    except Exception:
        return None