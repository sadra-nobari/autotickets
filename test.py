import time
import requests

# آدرس تست وب‌هوک n8n خودت رو اینجا بزار
WEBHOOK_URL = "http://localhost:5678/webhook-test/incoming-tickets"

# سناریوهای مختلف تیکت برای تست هوش مصنوعی
test_tickets = [
    
    {
        "title": "سوال در مورد فرآیند استخدام نیروی جدید",
        "description": "سلام وقت بخیر، می‌خواستم بدونم مراحل مصاحبه فرستاده شده برای پوزیشن جدید چقدر زمان می‌بره؟",
    },
]

print("🚀 شروع فرستادن تیکت‌های تست به n8n...\n")

for i, ticket in enumerate(test_tickets, 1):
    print(f"🔄 در حال ارسال تیکت شماره {i}: {ticket['title']}")
    try:
        response = requests.post(WEBHOOK_URL, json=ticket)
        print(f"✅ وضعیت پاسخ: {response.status_code}")
    except Exception as e:
        print(f"❌ خطا در اتصال به وب‌هوک: {e}")

    time.sleep(2)  # فاصله انداختن بین ارسال تیکت‌ها

print("\n✨ تمام تیکت‌ها ارسال شدند. حالا محیط n8n رو چک کن!")