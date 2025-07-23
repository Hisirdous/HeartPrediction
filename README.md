# Heart Prediction
Dự án AI sử dụng các thuật toán học máy để dự đoán khả năng mắc bệnh tim dựa trên dữ liệu y tế cá nhân.
## 🧰 Cài đặt & Khởi chạy
1. Clone repo & di chuyển vào thư mục
```
git clone https://github.com/Hisirdous/HeartPrediction.git
cd HeartPrediction
```
2. Tạo môi trường ảo
```
Với Conda:
conda env create -f environment.yml
conda activate heartpred

Hoặc dùng pip:
python -m venv venv
.\venv\Scripts\activate       # Windows
source venv/bin/activate     # Mac/Linux
pip install -r requirements.txt
```
3. Train model
```
python src/modeling/train.py
```
4. Chạy app Flask
```
python app.py
Truy cập http://localhost:5000/predict để gửi input và nhận kết quả.
```
🧩 Cấu trúc thư mục
```
HeartPrediction/
├── app.py                  # Flask API để dự đoán
├── environment.yml         # File môi trường Conda
├── requirements.txt        # Pip requirements
├── data/
│   └── raw/                # Chứa data gốc (csv)
├── notebooks/              # Notebook EDA và thử nghiệm model
└── src/
    ├── config.py           # Đường dẫn dữ liệu/model
    ├── dataset.py          # Load & xử lý dữ liệu
    ├── features.py         # Feature engineering
    └── modeling/
        ├── train.py        # Train model
        └── predict.py      # Gọi model để dự đoán
```
🔄 API Endpoint
POST /predict
```
📥 Input (JSON):
{
  "age": 58,
  "sex": 1,
  "resting_bp": 140,
  "cholesterol": 211,
  "fasting_bs": 0,
  "max_hr": 165,
  "oldpeak": 1.0,
  ...
}
```
📤 Output:
```
{"prediction": 1}  # 0 = Không bệnh tim, 1 = Có bệnh tim
```
📌 Ghi chú
```
Dữ liệu được xử lý tự động từ data/raw/, model sẽ được lưu tại models/.

Đảm bảo cấu trúc thư mục đúng như trên trước khi train hoặc chạy API.
```

