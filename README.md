# โปรแกรมดึงราคาทองรายวันและแจ้งเตือนไปยังไลน์ (The program retrieves daily gold prices and sends notifications to LINE Notify.)

ระบบนี้จะแจ้งเตือนราคาทองคำ วันละ 1 ครั้ง ตามกำหนด โดยเวลาที่ผมกำหนดไว้คือ 24 ชั่วโมง หมายความว่า เมื่อเปิดระบบครบ 24 ชั่วโมงแล้ว ระบบจะแจ้งเตือนไปยังไลน์ 1 ครั้ง และทำซ้ำไปเรื่อยๆ


This system will send a gold price notification once a day, according to the schedule I've set, which is every 24 hours. This means that when the system has been running for a full 24 hours, it will send a notification to LINE once, and it will repeat this process continuously.


#  How to Install

    pip install python-dotenv
    pip install requests

# Include Credits
API GOLD : https://api.chnwt.dev/thai-gold-api/latest
LINE Notify API Document https://notify-bot.line.me/doc/en/


# Preview
![Screenshot 2023-09-20 233428](https://github.com/bigy2012/gold-price-now/assets/121282845/a1ea9d5a-2234-42e9-9199-ad2b2a8a688a)


# License
