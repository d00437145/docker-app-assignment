import os
import requests

app_env = os.getenv("APP_ENV", "unknown")

print("=" * 50)
print(f"🚀 Dockerized App Starting up in environment: [{app_env.upper()}]")
print("=" * 50)

try:
    response = requests.get("https://api.github.com/zen", timeout=5)
    if response.status_code == 200:
        print(f"💡 GitHub Zen Quote: \"{response.text.strip()}\"")
    else:
        print("💡 Successfully connected using the 'requests' pip package!")
except Exception as err:
    print(f"⚠️ Network check warning: {err}")

print("=" * 50)
print("✅ Application finished running inside Docker successfully!")
print("=" * 50)
