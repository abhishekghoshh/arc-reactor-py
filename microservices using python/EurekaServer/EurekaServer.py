from flask import Flask, request, jsonify
import json

def addDataToJson(values):
    with open('clients.json') as f:
        f.seek(0)
        first_char = f.read(1)
        if not first_char:
            with open('clients.json', 'w') as f:
                json.dump(values, f)
        else:
            f.seek(0)
            with open('clients.json') as f:
                data = json.load(f)
                data.update(values)
                with open('clients.json', 'w') as f:
                    json.dump(data, f)

def readJson():
    try:
        f=open("clients.json","r")
        clients=dict(json.load(f))
        return list(clients.values())
    except Exception:
        return []

app = Flask(__name__)

@app.route("/", methods=["POST"])
def addClient():
    ip = request.json['ip']
    port = request.json['port']
    application_name=request.json['application_name']
    values={}
    values[ip]={
        "ip":ip,
        "port":port,
        "application_name":application_name
    }
    addDataToJson(values)
    return jsonify({"message":"Client is added"})

@app.route("/<app_name>", methods=["GET"])
def getClientByName(app_name):
    clients=readJson()
    fliteredClients=list(filter(lambda client: client['application_name']==app_name, clients))
    return jsonify(fliteredClients)

@app.route("/", methods=["GET"])
def getAllClients():
    clients=readJson()
    return jsonify(clients)

if __name__ == '__main__':
    app.run(debug=True,host="0.0.0.0",port=5000)