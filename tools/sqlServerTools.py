from mcp.server.fastmcp import FastMCP
from utils.sqlServerUtils import get_db_views, ejecutar_sql_query

mcp = FastMCP()

@mcp.tool()
async def listar_vistas_db() -> str:
    """Lista las vistas disponibles en la base de datos SQL Server."""
    return await get_db_views()

@mcp.tool()
async def ejecutar_sql_directo(query: str) -> str:
    """Ejecuta directamente una sentencia SQL contra la base de datos"""
    return await ejecutar_sql_query(query)