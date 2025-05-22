# Google Drive Uploader MCP Tool

โปรเจกต์นี้เป็นเครื่องมือช่วยอัปโหลดไฟล์ (เช่น ไฟล์รายงาน .png หรือ .csv) ไปยัง Google Drive โดยใช้ **PyDrive2** ผ่านการยืนยันตัวตนแบบ OAuth 2.0  
รองรับแนวคิด **Model Context Protocol (MCP)** สำหรับการวิเคราะห์และส่งออกรายงานอัตโนมัติในระบบ Legacy หรือ Workflow แบบ Automations

---

## Project Workspace Structure
```
google-drive-uploader/
│
├── README.md # ไฟล์นี้ - อธิบายโปรเจกต์และการใช้งาน
├── client_secrets.json # OAuth 2.0 credentials จาก Google Cloud Console
├── credentials.json # บันทึก token หลัง auth ครั้งแรก
│
├── upload_to_drive.py # โค้ดหลักที่ใช้อัปโหลดไฟล์ขึ้น Google Drive
├── myfile.png # ไฟล์ตัวอย่างที่ใช้ในการอัปโหลด
│
├── legacy/ # โฟลเดอร์สำหรับระบบดั้งเดิมหรือรายงานอัตโนมัติ
│ ├── reports/ # เก็บรายงานที่ generate แล้ว เช่น .png หรือ .csv
│ └── utils/ # ฟังก์ชันช่วยเหลือต่างๆ เช่น email, drive upload ฯลฯ
```

---

## Environment Variables (ENV)

โปรเจกต์นี้ใช้ตัวแปรแวดล้อม (Environment Variables) ดังนี้:

| ชื่อ ENV Variable     | คำอธิบาย                                           |
|----------------------|----------------------------------------------------|
| `GOOGLE_DRIVE_FOLDER_ID` | (ไม่จำเป็น) หากต้องการอัปโหลดไฟล์เข้าโฟลเดอร์เฉพาะใน Drive |
| `PYDRIVE2_SETTINGS`      | (ขั้นสูง) path ไปยังไฟล์ตั้งค่าของ PyDrive2 หากแยก config ไว้ |

สามารถตั้งค่า ENV เหล่านี้ได้ผ่านไฟล์ `.env` (ถ้าใช้ `python-dotenv`) หรือเซ็ตในระบบปฏิบัติการ

---

## Workflow Diagram (MCP Style)
```
+-------------------+
|   User Request    |
+---------+---------+
          |
          v
+-------------------+      +--------------------+
| Fetch News from   | ---> | Summarize News with |
| TheNewsAPI       |      | facebook/bart-large-cnn |
+---------+---------+      +----------+---------+
          |                           |
          v                           v
+-------------------+        +------------------+
|  Save Context &   |        |  Format Digest   |
|  News History     |        +---------+--------+
| (e.g. Pinecone)   |                  |
+---------+---------+                  v
          |                  +-------------------+
          +----------------> |  Send Digest to   |
                             |    Discord Bot    |
                             +-------------------+
```