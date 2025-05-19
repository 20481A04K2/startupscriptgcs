from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return """Hello, World! from github  {
  "db_user": "vamsi",
  "db_pass": "securepassword-rollback",
  "api_key": "your-api-key-value"
} """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
