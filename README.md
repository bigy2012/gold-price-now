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
![enter image description here](https://photos.app.goo.gl/gCXX5P4DovfzPcv49)
