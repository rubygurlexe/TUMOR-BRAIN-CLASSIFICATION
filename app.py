import numpy as np
from flask import Flask, request, render_template, jsonify
from PIL import Image
import tensorflow as tf
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Rute untuk halaman utama
@app.route("/", methods=["GET"])
def home():
    # Render file HTML di folder templates
    return render_template("index.html")

# Rute untuk klasifikasi tumor
@app.route("/tumor-brain", methods=['POST'])
def tumor_brain_classifier():
    try:
        # Ambil gambar yang dikirim melalui request
        image_request = request.files['image']

        # Konversi gambar menjadi array
        image_pil = Image.open(image_request).convert('RGB')

        # Resize gambar
        expected_size = (150, 150)
        resized_image_pil = image_pil.resize(expected_size)

        image_array = np.array(resized_image_pil)
        rescale_image_array = image_array / 255.0
        batched_rescaled_image_array = np.array([rescale_image_array])

        # Load model
        load_model = tf.keras.models.load_model('tumor-brain.h5')

        # Prediksi hasil klasifikasi
        result = load_model.predict(batched_rescaled_image_array)
        formatted_result = get_formatted_predict_result(result)
        
        # Mengembalikan hasil prediksi dalam format JSON
        return jsonify(formatted_result)
    
    except Exception as e:
        return jsonify(str(e)), 400


def get_formatted_predict_result(predict_result):
    # Mapping index hasil prediksi ke kelas tumor
    class_indexes = {
        0: "Meningioma",
        1: "Glioma",
        2: "Pituitari"
    }

    process_predict_result = predict_result[0]
    max_index = np.argmax(process_predict_result)  # Mengambil indeks nilai tertinggi
    return class_indexes[max_index]


if __name__ == "__main__":
    app.run(debug=True)
