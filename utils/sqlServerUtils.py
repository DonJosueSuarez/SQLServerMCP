import httpx

RAG_API_BASE = "http://localhost:8000"
USER_AGENT = "rag-mcp/1.0"

headers = {
    "User-Agent": USER_AGENT,
    "Content-Type": "application/json"
}

async def get_db_views() -> str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(f"{RAG_API_BASE}/api/views", headers=headers)
            response.raise_for_status()
            data = response.json()
            return "\n".join(data.get("views", [])) if "views" in data else str(data)
        except Exception as e:
            return f"Error al obtener vistas: {str(e)}"

async def ejecutar_sql_query(sql: str) -> str:
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(f"{RAG_API_BASE}/api/query", headers=headers, json={"sql": sql})
            response.raise_for_status()
            data = response.json()
            return str(data)
        except Exception as e:
            return f"Error al ejecutar consulta SQL: {str(e)}"
