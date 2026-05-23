from flask import Flask
import redis
import os

app = Flask(__name__)

r = redis.Redis(
    host=os.getenv("REDIS_HOST", "redis"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route("/")
def home():
    return "Welcome to Flask + Redis 🚀"

@app.route("/count")
def count():
    return f"Visits: {r.incr('visits')}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)