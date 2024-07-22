import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

# Memuat data
file_path = 'onlinefoods.csv'
data = pd.read_csv(file_path)

# Praproses data
# Mengonversi kolom 'Gender' menjadi numerik
data['Gender'] = data['Gender'].map({'Male': 0, 'Female': 1})

# Mengonversi kolom 'Monthly Income' menjadi numerik
income_map = {
    'No Income': 0,
    'Below Rs.10000': 1,
    '10001 to 25000': 2,
    '25001 to 50000': 3,
    'More than 50000': 4
}
data['Monthly_Income'] = data['Monthly_Income'].map(income_map)

# Memilih kolom yang relevan
features = ['Age', 'Gender', 'Monthly_Income', 'Family_Size']
X = data[features]
y = data['Output'].map({'Yes': 1, 'No': 0})  # Mengonversi target menjadi numerik

# Split data menjadi training dan testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Melatih model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Menyimpan model yang telah dilatih
joblib_file = "best_model.pkl"
joblib.dump(model, joblib_file)

print(f"Model berhasil disimpan sebagai {joblib_file}")
