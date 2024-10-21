from datetime import datetime

# Lấy timestamp hiện tại
timestamp = str(datetime.now().timestamp())

print(timestamp)

Payload = {
            "name": "favorite" + timestamp
        }

print(Payload)