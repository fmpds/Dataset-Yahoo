from fastapi import FastAPI
import uvicorn
from fastapi.middleware.cors import CORSMiddleware
from .routes.predict import router as predict_router

app = FastAPI()

app.include_router(predict_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
