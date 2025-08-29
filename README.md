# BFHL API (FastAPI + Streamlit)

This implements the **/bfhl** POST endpoint that accepts a JSON body like:
```json
{"data": ["a","1","334","4","R","$"]}
```
and returns the required response (is_success, user_id, email, roll_number, even/odd numbers as strings, alphabets in uppercase, special characters, sum as string, and alternating-caps reverse concatenation of all alphabetic characters).

## Run locally

```bash
# 1) create & activate venv (Windows PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1

# macOS/Linux
python3 -m venv .venv
source .venv/bin/activate

# 2) install
pip install -r requirements.txt

# 3) run API
uvicorn app.main:app --reload

# 4) in another terminal, run Streamlit tester
streamlit run streamlit_app.py
```

The API will be at http://localhost:8000/bfhl  
The Streamlit app will open in your browser, defaulting to http://localhost:8501

## Configure identity fields
Set these as environment variables on your host (or edit in `app/main.py`):
- `FULL_NAME` (lowercase, e.g. `john doe` -> will become `john doe`)
- `DOB_DDMMYYYY` (e.g. `17091999`)
- `EMAIL`
- `ROLL_NUMBER`

## Deploy (Render example)
1. Push this repo to GitHub.
2. On Render, create a **Web Service** from your repo.
3. **Build Command**: `pip install -r requirements.txt`
4. **Start Command**: `uvicorn app.main:app --host 0.0.0.0 --port 10000`
5. Add environment variables for identity fields.
6. Once deployed, your endpoint will be `https://<your-app>.onrender.com/bfhl`

## Deploy (Railway example)
1. Create a new service from your GitHub repo.
2. Set **Start Command** to `uvicorn app.main:app --host 0.0.0.0 --port $PORT`
3. Add environment variables for identity fields.
4. Deploy and grab the public URL.

## VS Code test (REST Client)
Install the REST Client extension and use `test.http` in this project.
