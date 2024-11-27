from fastapi import HTTPException, Request, Depends
from core.config import settings
from shared.http_client import AuthServiceClient

# Cliente para interactuar con el servicio de autenticación
auth_client = AuthServiceClient(base_url=settings.AUTH_SERVICE_URL)


def get_token_from_request(request: Request) -> str:
    """
    Obtiene y valida el formato del token JWT desde la cabecera Authorization de la solicitud.

    Args:
        request (Request): Solicitud HTTP entrante.

    Returns:
        str: Token JWT extraído de la cabecera Authorization.

    Raises:
        HTTPException: Si la cabecera Authorization está ausente o malformada.
    """
    token = request.headers.get("Authorization")
    if not token:
        raise HTTPException(status_code=401, detail="Authorization header is missing")
    if not token.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    return token.split(" ")[1]  # Extrae el token del formato "Bearer <token>"


async def check_token(request: Request):
    """
    Middleware para validar el token JWT en las solicitudes entrantes utilizando el AuthService.

    Args:
        request (Request): Solicitud HTTP entrante.

    Returns:
        dict: Información del usuario extraída del token si es válido.

    Raises:
        HTTPException: Si la validación del token falla.
    """
    # Extraer el token de la solicitud
    token = get_token_from_request(request)
    
    try:
        # Verificar el token usando AuthServiceClient
        token_data = await auth_client.verify_token(token)
        if not token_data:
            raise HTTPException(status_code=401, detail="Invalid token")
        return token_data  # Retorna los datos decodificados del usuario
    except HTTPException as e:
        # Repropaga errores de HTTPException
        raise e
    except Exception as e:
        # Maneja otros errores inesperados
        raise HTTPException(status_code=500, detail=f"Token validation failed: {str(e)}")
