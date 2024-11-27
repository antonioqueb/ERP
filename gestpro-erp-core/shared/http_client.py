import httpx
from typing import Optional, Dict, Any


class HTTPClient:
    """
    Cliente HTTP genérico para realizar solicitudes a servicios externos.
    """

    def __init__(self, base_url: str, timeout: int = 10):
        """
        Inicializa el cliente HTTP.

        Args:
            base_url (str): URL base del servicio con el que se comunicará el cliente.
            timeout (int): Tiempo límite en segundos para las solicitudes.
        """
        self.base_url = base_url
        self.timeout = timeout

    async def get(self, endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Realiza una solicitud GET a un endpoint específico.

        Args:
            endpoint (str): Endpoint relativo (ejemplo: "/health").
            params (Optional[Dict[str, Any]]): Parámetros de consulta opcionales.

        Returns:
            Dict[str, Any]: Respuesta JSON del servidor.

        Raises:
            httpx.RequestError: Si ocurre un error en la solicitud.
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.get(f"{self.base_url}{endpoint}", params=params)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise RuntimeError(f"Error during GET request to {endpoint}: {e}")

    async def post(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Realiza una solicitud POST a un endpoint específico.

        Args:
            endpoint (str): Endpoint relativo (ejemplo: "/login").
            json (Optional[Dict[str, Any]]): Datos en formato JSON para enviar en el cuerpo.

        Returns:
            Dict[str, Any]: Respuesta JSON del servidor.

        Raises:
            httpx.RequestError: Si ocurre un error en la solicitud.
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.post(f"{self.base_url}{endpoint}", json=json)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise RuntimeError(f"Error during POST request to {endpoint}: {e}")

    async def put(self, endpoint: str, json: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """
        Realiza una solicitud PUT a un endpoint específico.

        Args:
            endpoint (str): Endpoint relativo (ejemplo: "/users/1").
            json (Optional[Dict[str, Any]]): Datos en formato JSON para enviar en el cuerpo.

        Returns:
            Dict[str, Any]: Respuesta JSON del servidor.

        Raises:
            httpx.RequestError: Si ocurre un error en la solicitud.
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.put(f"{self.base_url}{endpoint}", json=json)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise RuntimeError(f"Error during PUT request to {endpoint}: {e}")

    async def delete(self, endpoint: str) -> Dict[str, Any]:
        """
        Realiza una solicitud DELETE a un endpoint específico.

        Args:
            endpoint (str): Endpoint relativo (ejemplo: "/users/1").

        Returns:
            Dict[str, Any]: Respuesta JSON del servidor.

        Raises:
            httpx.RequestError: Si ocurre un error en la solicitud.
        """
        async with httpx.AsyncClient(timeout=self.timeout) as client:
            try:
                response = await client.delete(f"{self.base_url}{endpoint}")
                response.raise_for_status()
                return response.json()
            except httpx.HTTPError as e:
                raise RuntimeError(f"Error during DELETE request to {endpoint}: {e}")
