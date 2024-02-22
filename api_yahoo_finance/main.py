from fastapi import FastAPI
from app.features.Usuario.V1.Controllers.user_controller import router as user_router
from app.features.Yahoo.V1.Controllers.yahoo_controller import router as yahoo_service

app = FastAPI()

# Adicionando os roteadores das controllers ao aplicativo
app.include_router(user_router, prefix="/api/v1")
app.include_router(yahoo_service, prefix="/api/v1/yahoo")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)