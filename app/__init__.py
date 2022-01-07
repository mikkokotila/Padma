import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_headers=["*"],
)

from app.utils.initialize import initialize_meta
from app.utils.initialize import initialize_dictionary
from app.utils.initialize import initialize_tokens
from app.utils.initialize import initialize_texts
from app.utils.initialize import initialize_index
from app.utils.initialize import initialize_locations

from app.utils.text_search import text_search
from app.utils.tokenization import init_tokenizer

meta = initialize_meta()
dictionary = initialize_dictionary()
tokens = initialize_tokens()
texts = initialize_texts()
index = initialize_index()
locations = initialize_locations()

tokenizer = init_tokenizer()

from botok import Text

from app import routes
