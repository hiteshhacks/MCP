from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP


mcp = FastMCP("weather")

NWS_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"

async def make_nws_request(url:str)-> dict[str,Any] | None:
    """" make request to nws api"""
    headers = {
        "USER_AGENT":USER_AGENT,
        "Accept": "application/geo+json"
    }

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception:
            return None
        

def format_alert(features:dict)-> str:
    """format alert frature into readble string"""
    props= features["properties"]
    return f"""
            Event:{props.get('event','Unknown')}
            Area:{props.get('areaDesc','Unknown')}
            Severity:{props.get('serverity','Unknown')}
            Description:{props.get('description','No description available')}
            Instructions:{props.get('instruction','No specific instruction provided ')}
"""
@mcp.tool()
async def get_alerts(state:str)-> str:
    """
     get weather alerts for US state.

     Args:
        state: Two-letter US state code (e.g. CA, NY)
    """
 

    url= f"{NWS_API_BASE}/alerts/active/area/{state}"
    data = await make_nws_request(url)

    if not data or "features" not in data:
        return "no alert found"
    if not data["features"]:
        return "no active alerts for this state"
    
    alerts= [format_alert(features)for features in data["features"]]
    return "\n----\n".join(alerts)

@mcp.resource("config://app")
def get_config() -> str:
    """Static configuration data"""
    # This would normally read from disk
    return  "App configuration here"




if __name__ == "__main__":
    mcp.run( )