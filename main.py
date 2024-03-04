from flask import Flask, request, jsonify
from pymongo import MongoClient
from bson import ObjectId, errors

app = Flask(__name__)

# MongoDB setup
CONNECTION_STRING = "mongodb+srv://dibyamongo:rLtI8oJmCCo6I34m@dibya.d7hfomy.mongodb.net/"
client = MongoClient(CONNECTION_STRING)
db = client.dibya
collection = db.resum_data

print("+++++++++++++++")
print(collection)

@app.route('/')
def index():
    # ... your code for the root route
    return "Hello, World!"

@app.route('/upload/', methods=['POST'])
def upload_file():
    # ... your code for file upload
    return "File Uploaded"

@app.route('/user', methods=['GET'])
def get_user():
    user_id = request.args.get('user_id')
    print("Received user_id:", user_id)

    try:
        object_id = ObjectId(user_id)
    except errors.InvalidId:
        print("Invalid ObjectId format")
        return jsonify({"message": "Invalid user ID format"}), 400

    print("Converted ObjectId:", object_id)
    user_document = collection.find_one({"_id": object_id})
    print("Query result:", user_document)

    if user_document:
        user_document["_id"] = str(user_document["_id"])
        return jsonify(user_document)
    else:
        return jsonify({"message": "User not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
