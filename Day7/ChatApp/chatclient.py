import requests
def send_message(user, text):
    msg = {"user": user, "text": text}
    requests.post("http://localhost:8000", json=msg)
def show_messages():
    r = requests.get("http://localhost:8000")
    print(r.json())
send_message("Aditri", "Hello!")
send_message("Divya", "Hi Aditri!")
show_messages()
