import requests,json,GetMyIp as Ip,ReadProperties as properties

my_ip=Ip.getMyIp()
port=properties.readProperties("server.port")
application_name=properties.readProperties("application.name")
eureka_url=properties.readProperties("eureka.server.url")


payload ={
        'ip':my_ip,
	    'port':port,
	    'application_name':application_name
    }
headers = {'content-type': 'application/json'}
try: 
    r = requests.post(url=eureka_url,data=json.dumps(payload), headers=headers)
    pastebin_url = r.json()
    print("The pastebin URL is:%s"%pastebin_url) 
except Exception as e:
    print(e)