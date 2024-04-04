import pytest
import httpx
import secrets

@pytest.fixture
async def prerrequisito_crear_categoria():
    async with httpx.AsyncClient() as client:
        randomString = secrets.token_hex(5)
        nombreCategoria = f"Categoria_{randomString}"
        response = await client.post(
            "http://localhost:8000/api/v1/categorias", 
            json={
                "nombre": nombreCategoria,
            }
        )
        return response.json()