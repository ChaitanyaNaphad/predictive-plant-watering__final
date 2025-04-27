# firebase_config.py

import firebase_admin
from firebase_admin import credentials, db

# Replace with the correct path to your Firebase service account JSON file.
SERVICE_ACCOUNT_PATH = r"E:\all_csv\predictive-plant-watering-firebase-adminsdk-fbsvc-c2ba0ff7d9.json"


# Your Firebase Realtime Database URL
DATABASE_URL = "https://predictive-plant-watering-default-rtdb.asia-southeast1.firebasedatabase.app/"

# Initialize the Firebase Admin SDK inside a try/except block to catch errors.
try:
    cred = credentials.Certificate(SERVICE_ACCOUNT_PATH)
    firebase_admin.initialize_app(cred, {
        'databaseURL': DATABASE_URL
    })
    print("✅ Firebase Admin SDK initialized successfully.")
except Exception as e:
    print("❌ Error initializing Firebase Admin SDK:", e)
    # Optionally, you might want to exit or handle the error appropriately.
    raise

def get_sensor_data():
    """
    Fetch sensor data from the root of your Firebase Realtime Database.
    Adjust the reference path if your data is stored under a different node.
    
    Returns:
        A dictionary containing your sensor data.
    """
    try:
        ref = db.reference("/")  # Use "/" if your data is stored at the root.
        data = ref.get()
        return data
    except Exception as e:
        print("❌ Error fetching sensor data:", e)
        return None

if __name__ == "__main__":
    # For testing, print the sensor data in the console.
    sensor_data = get_sensor_data()
    print("Fetched Sensor Data:", sensor_data)
