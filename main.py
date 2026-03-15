from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.issues import router as issues_router
from app.middleware.timer import timer_middleware

app = FastAPI(
    title="Issue Tracker API",
    description="Fast API Tutorial",
)
app.middleware("http")(timer_middleware)
app.add_middleware(CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
app.include_router(issues_router)