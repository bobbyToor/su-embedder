import logging as logger
from fastapi import APIRouter, Request, status
from fastapi.params import Depends
from fastapi.responses import JSONResponse
from api.dependencies import validate_admin
from services.embedder import embedder

router = APIRouter()


@router.post("/get_embedding")
async def get_embedding(
    request: Request,
    auth_valid: bool = Depends(validate_admin),
):
    if not auth_valid:
        return JSONResponse(status_code=status.HTTP_401_UNAUTHORIZED, content="🤐")

    try:
        req_body = await request.json()

        if "input" not in req_body:
            raise Exception("Missing argument")

        input = req_body["input"]
        if not input:
            raise Exception("Missing argument")

        vector = embedder(input)
        vector = vector.tolist()

        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=vector,
        )
    except Exception as e:
        logger.error(e)
        return JSONResponse(
            status_code=status.HTTP_400_BAD_REQUEST,
            content={"error": str(e)},
        )
