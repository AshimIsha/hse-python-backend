
from fastapi import FastAPI
from routers import shop_router
from prometheus_fastapi_instrumentator import Instrumentator
app = FastAPI()
Instrumentator().instrument(app).expose(app)

app.include_router(shop_router)
