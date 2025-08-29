from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any, Dict
import os
import re

app = FastAPI(title="BFHL API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

FULL_NAME = os.getenv("FULL_NAME", "nidhish balasubramanya")  
DOB_DDMMYYYY = os.getenv("DOB_DDMMYYYY", "30062004")
EMAIL = os.getenv("EMAIL", "nidhishbala3006@gmail.com")
ROLL_NUMBER = os.getenv("ROLL_NUMBER", "22BRS1061")

class BFHLRequest(BaseModel):
    data: List[Any]

def is_int_str(s: str) -> bool:
    return bool(re.fullmatch(r"-?\d+", s))

def is_alpha_str(s: str) -> bool:
    return bool(re.fullmatch(r"[A-Za-z]+", s))

def alt_caps_reverse_concat(alpha_tokens: List[str]) -> str:
    letters: List[str] = []
    for token in alpha_tokens:
        for ch in token:
            if ch.isalpha():
                letters.append(ch)

    letters.reverse()

    out_chars = []
    for i, ch in enumerate(letters):
        if i % 2 == 0:
            out_chars.append(ch.upper())
        else:
            out_chars.append(ch.lower())
    return "".join(out_chars)

@app.post("/bfhl")
def bfhl_endpoint(body: BFHLRequest) -> Dict[str, Any]:
    try:
        tokens: List[str] = []
        for item in body.data:
            if item is None:
                continue
            s = str(item).strip()
            if s == "":
                continue
            tokens.append(s)

        even_numbers: List[str] = []
        odd_numbers: List[str] = []
        alphabets: List[str] = []
        special_characters: List[str] = []

        total = 0

        for tok in tokens:
            if is_int_str(tok):
                n = int(tok)
                total += n
                if abs(n) % 2 == 0:
                    even_numbers.append(tok)
                else:
                    odd_numbers.append(tok)
            elif is_alpha_str(tok):
                alphabets.append(tok.upper())
            else:
                special_characters.append(tok)

        concat_string = alt_caps_reverse_concat([t for t in tokens if is_alpha_str(t)])

        response = {
            "is_success": True,
            "user_id": f"{FULL_NAME.lower()}_{DOB_DDMMYYYY}",
            "email": EMAIL,
            "roll_number": ROLL_NUMBER,
            "odd_numbers": odd_numbers,
            "even_numbers": even_numbers,
            "alphabets": alphabets,
            "special_characters": special_characters,
            "sum": str(total),
            "concat_string": concat_string,
        }
        return response
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
