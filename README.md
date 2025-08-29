# Bajaj BFHL API (FastAPI + Streamlit)

This repository contains the implementation of the **Bajaj Full Stack Hiring Challenge (BFHL)** API using **FastAPI** for the backend and a small **Streamlit app** for testing the API.

---

## 📌 Problem Statement

The task was to build and host a REST API with the following specifications:

- **Method:** `POST`  
- **Route:** `/bfhl`  
- **Input:** JSON body containing an array (strings/numbers/special characters).  
- **Output:** JSON response with:  
  1. `is_success` (status flag)  
  2. `user_id` (format: `<full_name_ddmmyyyy>`)  
  3. `email`  
  4. `roll_number`  
  5. Array of **even numbers**  
  6. Array of **odd numbers**  
  7. Array of **alphabets (uppercase)**  
  8. Array of **special characters**  
  9. **Sum** of numbers (as string)  
  10. **Concatenation** of all alphabetic characters in reverse order with alternating caps  

---

## 🚀 Hosted API

**Endpoint:**  
👉 [[https://your-app-name.onrender.com/bfhl](https://bajaj-fullstack-bfhl-api.onrender.com)]([https://your-app-name.onrender.com/bfhl](https://bajaj-fullstack-bfhl-api.onrender.com))  

**Method:** `POST`  

### ✅ Example Request

```json
{
  "data": ["a","1","334","4","R","$"]
}
```

### ✅ Example Response

```json
{
  "is_success": true,
  "user_id": "nidhish balasubramanya_30062004",
  "email": "nidhishbala3006@gmail.com",
  "roll_number": "22BRS1061",
  "odd_numbers": ["1"],
  "even_numbers": ["334", "4"],
  "alphabets": ["A", "R"],
  "special_characters": ["$"],
  "sum": "339",
  "concat_string": "Ra"
}
```

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **FastAPI** (REST API framework)  
- **Uvicorn** (ASGI server)  
- **Streamlit** (simple UI to test API)  
- **Pydantic** (request validation)  
- **Gunicorn** (production server, if needed)  

---

## ⚙️ Local Development

Clone the repository:

```bash
git clone https://github.com/<your-username>/bajaj-bfhl-api.git
cd bajaj-bfhl-api
```

Create and activate a virtual environment:

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# macOS / Linux
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the API locally:

```bash
uvicorn main:app --reload
```

The API will be live at:  
👉 [http://localhost:8000/bfhl](http://localhost:8000/bfhl)

---

## 🌐 Deployment (Render)

This project is configured for **Render** hosting.

1. Push this repo to GitHub (public).  
2. Go to [https://render.com](https://render.com) → Create **New Web Service**.  
3. Connect your GitHub repo.  
4. Set:
   - **Build Command:**  
     ```bash
     pip install -r requirements.txt
     ```
   - **Start Command:**  
     ```bash
     uvicorn main:app --host 0.0.0.0 --port 10000
     ```
5. Add environment variables in Render dashboard:  
   - `FULL_NAME` = `nidhish balasubramanya`  
   - `DOB_DDMMYYYY` = `30062004`  
   - `EMAIL` = `nidhishbala3006@gmail.com`  
   - `ROLL_NUMBER` = `22BRS1061`  
6. Deploy and note the public URL (e.g. `https://your-app.onrender.com/bfhl`).  

---

## 🎛️ Testing with Streamlit

This repo also includes a simple **Streamlit app** (`streamlit_app.py`) to test the API.

Run locally:

```bash
streamlit run streamlit_app.py
```

- Enter comma-separated values in the input box.  
- Provide your API base URL (`http://localhost:8000` or your Render URL).  
- Click **Send** to see request/response in real time.  

---

## 📋 Identity Information

- **User ID:** `nidhish balasubramanya_30062004`  
- **Email:** `nidhishbala3006@gmail.com`  
- **Roll Number:** `22BRS1061`  

---

## ✅ Submission Notes

- Endpoint `/bfhl` is fully functional and hosted.  
- Handles input validation, classification, and response formatting.  
- Numbers are always returned as **strings** (per requirements).  
- Error handling included for invalid inputs.  

---

## 📂 Project Structure

```
bajaj-bfhl-api/
 ├── main.py              # FastAPI backend (core API logic)
 ├── streamlit_app.py     # Streamlit UI tester
 ├── requirements.txt     # Python dependencies
 ├── Procfile             # For deployment (Heroku/Render)
 ├── README.md            # Documentation (this file)
 └── .gitignore
```

---
