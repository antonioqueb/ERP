# gestpro-erp-core/core/middleware/auth.py

from fastapi import HTTPException, Request
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError
from core.config import settings
from shared.http_client import AuthServiceClient
from functools import wraps

# Cliente para interactuar con el servicio de autenticación
auth_client = AuthServiceClient(base_url=settings.AUTH_SERVICE_URL)

def verify_token(token: str):
    """
    Función que decodifica y verifica un token JWT.
    """
    try:
        # Decodificamos el token usando la clave secreta
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload  # Retorna el payload con los datos del usuario
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def get_token_from_request(request: Request):
    """
    Obtiene el token JWT de la cabecera Authorization de la solicitud.
    """
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    if not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    return token.split(" ")[1]  # Extrae el token del formato "Bearer <token>"

async def check_token(request: Request):
    """
    Middleware que valida el token JWT en las solicitudes entrantes.
    """
    token = get_token_from_request(request)
    # Verificar el token con el AuthServiceClient
    token_data = await auth_client.verify_token(token)
    if not token_data:
        raise HTTPException(status_code=401, detail="Invalid token")
    # Si el token es válido, retornamos el payload (datos del usuario)
    return token_data

