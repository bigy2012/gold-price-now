from dotenv import load_dotenv
import os 
load_dotenv()
import requests

def main(message):
    url = os.getenv('URL_LINE_NOTIFY');
    token = os.getenv('TOKEN_LINE_NOTIFY');
    header = {
        'Content-Type':	'application/x-www-form-urlencoded',
        'Authorization': 'Bearer ' + token,
    }
    Package_id = 446
    stickerId = 2003
    sticker = {'message': ' ', 'stickerPackageId': Package_id, 'stickerId': stickerId}

    if message['status'] == 'error':
        requests.post(url, headers=header, data=message)
        return
    else:
        requests.post(url, headers=header, data=message)
        response = requests.post(url, headers=header, data=sticker)

    status = 'error'
    if response.status_code == 200:
        status = 'Success'
    return status

def getGold():
    url = os.getenv('URL_GOLD')
    response = requests.get(url)
    
    data = { 'response': 'error' }
    if response.status_code == 200:
        data = response.json()

    return data['response']


if __name__ == '__main__':
        dataGold = getGold()
        if dataGold != 'error':
            GoldData =  f"{dataGold['date']} \n"\
                        f"{dataGold['update_time']} \n"\
                        f"---------------------- \n"\
                        f"ทองคำแท่ง : รับซื้อ {dataGold['price']['gold_bar']['buy']} \n"\
                        f"ทองคำแท่ง : ขายออก {dataGold['price']['gold_bar']['sell']} \n"\
                        f"---------------------- \n"\
                        f"ทองรูปพรรณ : รับซื้อ {dataGold['price']['gold']['buy']} \n"\
                        f"ทองรูปพรรณ : ขายออก {dataGold['price']['gold']['sell']} \n"\
                        f"---------------------- \n"\
                        f"วันนี้ ขึ้น/ลง : {dataGold['price']['change']['compare_previous']} \n"
                        
            msg = {'message': GoldData, "status": "success"}
            line = main(msg)
        else:
            msg = {'message': "ไม่สามารถแสดงข้อมูลได้", "status": "error"}
            line = main(msg)
             