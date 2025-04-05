# 🌟 Data-Driven AI for Sustainable Farming

## 💡 Overview
This project is designed to assist farmers in making **data-driven decisions** about crop selection, market trends, and sustainability. Using **rule-based decision logic**, it recommends **optimal crops** based on **soil conditions, climate factors, and market demand**.

## 🔍 Problem Statement
Farmers often struggle with **choosing the right crops** due to unpredictable weather, soil conditions, and fluctuating market demand. Traditional methods lack **data-driven insights**, leading to **low productivity and financial losses**. This project provides **intelligent recommendations** to optimize **crop yield and profitability**.

## 🔋 Key Features

✅ **Crop Recommendation** – Suggests the best crop based on **soil pH, moisture, rainfall, and temperature**.  

✅ **Market Analysis** – Evaluates **market trends** to ensure crops are in demand.  

✅ **Sustainability Check** – Assesses **crop yield** and **sustainability score** to promote **eco-friendly farming**.  

✅ **User-Friendly Web App** – Built with **Flask**, allowing farmers to input farm details and receive **instant recommendations**.  

## 🛠️ Technologies Used

- **Python** (Decision rule-based system)

- **Flask** (Web framework for UI)

- **Pandas** (Data handling)

- **SQLite** (For dataset storage)

- **HTML + CSS** (User Interface)

## 📂 Project Structure
```
/data-driven-ai-farming
│── /data                   # Dataset & database storage
│   ├── farmer_advisor_dataset.csv  # Farmer advisory dataset
│   ├── market_research_dataset.csv # Market trends dataset
│   ├── farming.db                # SQLite Database (if used)
│
│── /rules                   # Decision Rule-Based Logic
│   ├── crop_recommendation.py  # Crop recommendation logic
│   ├── market_analysis.py      # Market research & trend analysis
│   ├── sustainability_check.py # Sustainability & yield evaluation
│
│── /templates              # HTML Templates for Flask Web App
│   ├── index.html          # Main UI Page (contains internal CSS)
│   ├── dashboard.html      # Dashboard for displaying recommendations
│
│── app.py                  # Main Flask Application (handles UI & logic)
│── config.py               # Configuration settings (DB, dataset paths)
│── requirements.txt        # List of dependencies (Flask, Pandas, etc.)
│── README.md               # Project Documentation
```

## 🚀 How to Run the Project

### 1️⃣ Clone the repository

git clone https://github.com/Mazid2003/Farm-Recommendation-System-using-Machine-Learning.git

cd directory name

### 2️⃣ Install dependencies

pip install -r requirements.txt

### 3️⃣ Run the Flask app

python app.py

### 4️⃣ Open the app in your browser

http://127.0.0.1:5000/


### 🌟 Impact & Benefits

💡 Helps **farmers** make **informed decisions** using **data-driven insights**.  

💡 Ensures **better crop yield, profitability, and sustainability**.  

💡 Eliminates the need for **complex AI models**, making it **lightweight & efficient**.  

---
This project is a step toward **intelligent agriculture**, empowering farmers with **data-driven decision-making tools**. 🌱🚜  

Made with ❤️ by **Mohammad Mazid**
🤝 Contributing

Feel free to fork the repo and improve the game with new features or optimizations. Pull requests are welcome!

and also submit PRs, and give your feedback! 🔥💡

📜 License

This project is open-source and available under the MIT License.

http://mazid85.pythonanywhere.com
