import requests
from pymongo import MongoClient

def get_last_document(collection):
    cursor = collection.find().sort("_id", -1).limit(1)
    last_document = next(cursor, None)
    return last_document

if __name__ == "__main__":
    client = MongoClient('mongodb+srv://nisamanee:passw0rd!@ct-pj-iot.mongocluster.cosmos.azure.com/?tls=true&authMechanism=SCRAM-SHA-256&retrywrites=false&maxIdleTimeMS=120000')
db = client['Project']
collection = db['Temp Status']

last_document = get_last_document(collection)

if last_document:
    print(last_document)
else:
    print("ไม่พบข้อมูลในคอลเล็กชัน")

def send_line_notify(message, token):
    url = 'https://notify-api.line.me/api/notify'
    headers = {'Authorization': f'Bearer {token}'}
    data = {'message': message}
    response = requests.post(url, headers=headers, data=data)
    print(response.text)

def check_and_alert(document):
    if 'value' in document and document['value'] > 27:
        send_line_notify("27: {}".format(document))
    else:
        print("ไม่ต้องแจ้งเตือน: {}".format(document))


if __name__ == "__main__":
    # ใส่ Token ที่ได้จาก Line Notify ที่นี่
    line_notify_token = '2wJIirlADdpseIU1SOi9BSRLxofFZ97GCZ6m5X3ZEax'
    message = 'Hi pam!'

    send_line_notify(message, line_notify_token)

