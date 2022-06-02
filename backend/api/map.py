from fastapi import APIRouter
import urllib.parse

router = APIRouter(prefix="/admin/api")

"""
Returns the map object more information about that can be found on the official workadventure documentation
"""
@router.get("/map")
async def map(playUri):
    """
    The map-endpoint. It returns a static JSON.
    """
    map_url = urllib.parse.unquote(playUri)
    map_url = "https://play.hs-kl.de/maps/" + map_url.split("maps/")[1] if "maps" in map_url else map_url

    return {
        "mapUrl": map_url,
        "policy_type": 1,
        "tags": [],
        "authenticationMandatory": False,
        "roomSlug": None,
        "contactPage": None,
        "group": "wa",
        "iframeAuthentication": None,
        "miniLogo": None,
        "loadingLogo": None,
        "loginSceneLogo": None,
        "showPoweredBy": True,
        "loadingCowebsiteLogo": None
    }
