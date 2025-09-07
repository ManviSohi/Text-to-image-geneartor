from flask import Flask, request, jsonify, send_from_directory
import random

app = Flask(__name__, static_url_path="", static_folder=".")

@app.route("/api/generate", methods=["POST"])
def generate():
    data = request.get_json()
    count = int(data.get("count", 1))
    
    # Fake images for testing
    fake_images = [f"https://picsum.photos/seed/{random.randint(1,9999)}/512/512" for _ in range(count)]
    
    return jsonify({"images": fake_images})

@app.route("/")
def index():
    return send_from_directory(".", "text-to-image-frontend.html")

if __name__ == "__main__":
    app.run(port=5000, debug=True)
