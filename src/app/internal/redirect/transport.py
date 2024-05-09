import logging

from fastapi import APIRouter, Request
from fastapi.responses import RedirectResponse

from config import settings
from config.settings import storage

redirect_router = APIRouter(prefix="", tags=["redirect"])
logger = logging.getLogger(__name__)


def concat_with_query_params(destination: str, query_string: str) -> str:
    if not query_string:
        return destination

    return f"{destination}?{query_string}"


@redirect_router.get("/{source:path}")
async def redirect(
    request: Request,
    source: str,
) -> RedirectResponse:
    logger.info(f'Redirect from {source}')
    destination = storage.get(source)
    logger.info(f'Redirect to {destination}')

    destination_with_query_params = concat_with_query_params(
        destination, str(request.query_params)
    )
    return RedirectResponse(destination_with_query_params, status_code=302)


@redirect_router.get("/")
async def default_redirect() -> RedirectResponse:
    return RedirectResponse(settings.DEFAULT_REDIRECT, status_code=302)
