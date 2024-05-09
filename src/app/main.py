from fastapi import FastAPI
from fastapi.responses import PlainTextResponse, RedirectResponse
from starlette.exceptions import HTTPException

from app.internal.redirect.transport import redirect_router
from config import settings


def get_docs():
    if settings.DEBUG:
        return dict(debug=True)

    return dict(debug=False, docs_url=None, redoc_url=None, openapi_url=None)


async def plain_http_exception_handler(request, exc):
    return PlainTextResponse(str(exc.detail), status_code=exc.status_code)


def build_redirect_app() -> FastAPI:
    redirect_app = FastAPI(**get_docs())
    redirect_app.include_router(
        redirect_router, default_response_class=RedirectResponse
    )
    redirect_app.add_exception_handler(HTTPException, plain_http_exception_handler)
    return redirect_app


def build_app() -> FastAPI:
    app = FastAPI(**get_docs())
    app.mount("", build_redirect_app())

    return app


app = build_app()
