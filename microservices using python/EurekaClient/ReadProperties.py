f=open("application.properties","r")
lines=list(f.read().split("\n"))
properties={}
for line in lines:
    try:
        line=line.split("=")
        properties[line[0]]=line[1]
    except Exception:
        pass
def readProperties(key):
    try:
        return properties[key]
    except Exception:
        return None