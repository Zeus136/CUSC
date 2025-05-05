import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score
from flask import Flask, request, render_template
import joblib  # Thư viện để lưu và tải mô hình

# Đọc dữ liệu từ file Excel
data_file = "data.xlsx"  # Đường dẫn tới file Excel
df = pd.read_excel(data_file)

# Kiểm tra số lượng dòng trong DataFrame
print(f"Số lượng dòng trong DataFrame: {len(df)}")
print(df.head())  # Hiển thị 5 dòng đầu tiên để kiểm tra

# Chuyển đổi dữ liệu triệu chứng thành dạng vector
vectorizer = TfidfVectorizer(stop_words='english')
X = vectorizer.fit_transform(df['symptoms'])

# Dữ liệu đầu ra: Phác đồ điều trị (treatment_regimen)
y = df['treatment_regimen']

# Chia dữ liệu thành bộ dữ liệu huấn luyện và kiểm tra
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Tên file lưu mô hình và vectorizer
model_file = "random_forest_model.pkl"
vectorizer_file = "tfidf_vectorizer.pkl"

try:
    # Tải mô hình và vectorizer nếu đã tồn tại
    model = joblib.load(model_file)
    vectorizer = joblib.load(vectorizer_file)
    print("Mô hình và vectorizer đã được tải thành công.")
except FileNotFoundError:
    # Huấn luyện mô hình nếu chưa tồn tại
    print("Không tìm thấy mô hình. Đang huấn luyện mô hình mới...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # Lưu mô hình và vectorizer
    joblib.dump(model, model_file)
    joblib.dump(vectorizer, vectorizer_file)
    print("Mô hình và vectorizer đã được lưu.")

# Dự đoán và đánh giá mô hình
y_pred = model.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred)}")

# Tạo ứng dụng Flask
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    user_input = request.form['input']  # Lấy dữ liệu đầu vào từ form
    
    # Kiểm tra loại đầu vào
    if user_input in df['icd_code'].values:
        # Nếu là mã ICD
        result = df[df['icd_code'] == user_input]['treatment_regimen'].values[0]
    elif user_input in df['disease_name'].values:
        # Nếu là tên bệnh
        result = df[df['disease_name'] == user_input]['treatment_regimen'].values[0]
    else:
        # Nếu là triệu chứng
        symptom_vector = vectorizer.transform([user_input])
        result = model.predict(symptom_vector)[0]
    
    return render_template('result.html', prediction=result)

if __name__ == '__main__':
    app.run(debug=True)
