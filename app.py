# app.py
from fastapi import FastAPI, Form, Depends, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from starlette.middleware.wsgi import WSGIMiddleware
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
from models import Base, DimUsuario  # Usamos DimUsuario para autenticación
from dash_app import dash_app  # Importamos la instancia de Dash

DATABASE_URL = "postgresql://usuario:contraseña@db:5432/mi_base"

# Configuración de la conexión a la base de datos
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base.metadata.create_all(bind=engine)

# Clase para encapsular la lógica de la aplicación (principio de responsabilidad única)
class AppService:
    def __init__(self) -> None:
        self.app = FastAPI()
        self._mount_dash()
        self._configure_routes()

    def _mount_dash(self) -> None:
        # Monta la aplicación de Dash en FastAPI
        self.app.mount("/dashboard", WSGIMiddleware(dash_app.server))

    def _configure_routes(self) -> None:
        @self.app.get("/login", response_class=HTMLResponse)
        def login_form() -> str:
            return """
            <html>
              <body>
                <form action="/login" method="post">
                  Usuario: <input type="text" name="username"><br>
                  Contraseña: <input type="password" name="password"><br>
                  <input type="submit" value="Login">
                </form>
              </body>
            </html>
            """

        @self.app.post("/login")
        def login(username: str = Form(...), password: str = Form(...), db: Session = Depends(get_db)) -> RedirectResponse:
            usuario = db.query(DimUsuario).filter(DimUsuario.username == username).first()
            if not usuario or password != "dummy":  # Validación simplificada
                raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales incorrectas")
            return RedirectResponse(url="/dashboard/", status_code=status.HTTP_302_FOUND)

# Dependencia para obtener la sesión de base de datos
def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Instanciamos el servicio de la aplicación
service = AppService()
app = service.app

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

