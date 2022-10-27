def send_mail(from_message,to_message,message,username,password,SMTP_server):
    try:
        import smtplib
        server = smtplib.SMTP(SMTP_server)
        server.starttls()
        server.login(username, password)
        server.sendmail(from_message, to_message, message)
        server.quit()
        print("Mail sent successfully")
    except:
        print("Mail sent failed")

def send_message(nexmo_key,nexmo_Secret,from_message,to_message,text):
    try:
        import nexmo
        client = nexmo.Client(key=nexmo_key, secret=nexmo_Secret)
        response = client.send_message(
            {
                "from": from_message,
                "to": to_message,
                "text": text,
            }
        )
        if response["messages"][0]["status"] == "0":
            print("Message sent successfully")
        else:
            print("Message sent failed")
    except:
        print("Message sent failed")

def get_pylirt():
    import pylirt

def get_pywirt():
    import pywirt

def alienvault_control(OTX_key,find_word):
    from OTXv2 import OTXv2
    otx = OTXv2(OTX_key)
    for i in (otx.getall()):
        try:
            id = str(i['id'])
        except:
            id = ""
        try:
            name = str(i['name'])
        except:
            name = ""
        try:
            description = str(i['description'])
        except:
            description = ""
        try:
            created = str(i['created'])
        except:
            created = ""
        try:
            tlp = str(i['tlp'])
        except:
            tlp = ""
        try:
            adversary = str(i['adversary'])
        except:
            adversary = ""
        try:
            author = str(i['author_name'])
        except:
            author = ""
        try:
            indicators = str(i['indicators'])
        except:
            indicators = ""
        try:
            full = ""
        except:
            full = ""
        try:
            content = str(id) + "\n" + str(name) + "\n" + str(description) + "\n" + str(created) + "\n" + str(
                tlp) + "\n" + str(adversary) + "\n" + str(author) + "\n" + str(indicators) + "\n" + str(
                full) + "\n\n\n=========\n\n\n"
            if find_word in content:
                print(find_word)
        except:
            pass

def send_log(SIEMhost,SIEMport,log):
    import socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((SIEMhost, SIEMport))
    s.sendall(log)
    s.close()

def staxx_ip_control(username,password,staxx_URL):
    import requests
    import json
    header = {'Content-Type': 'application/json'}
    veri = {"username": username, "password": password}
    url = staxx_URL + '/api/v1/login'
    response = requests.post(url=url, headers=header, data=json.dumps(veri), verify=False)
    token = response.json()['token_id']
    data = {"token": str(token), "query": "confidence>70", "type": "json", "size": 10}
    url = staxx_URL + "/api/v1/intelligence"
    result = requests.post(url=url, headers=header, data=json.dumps(data), verify=False)
    return result

def sendSplunk(host,port,username,password,file):
    import splunklib.client as client
    import splunklib.results as results
    from splunklib.binding import AuthenticationError
    try:
        service = client.connect(host=host, port=port, username=username, password=password)
    except exception as e:
        print(str(e))
        myindex = service.indexes['main']
    try:
        myindex.upload(file)
    except Exception as e:
        print(str(e))

