from fastapi import FastAPI

from routes.imei_routes import imei_router
from routes.user_routes import user_router

app = FastAPI()

app.include_router(user_router)
app.include_router(imei_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=False)
