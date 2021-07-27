import logging as logger
from fastapi import APIRouter, Request, status, HTTPException
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

        if "sentences" not in req_body:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        sentences = req_body["sentences"]
        if not sentences:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

        res = embedder(sentences=sentences)

        return JSONResponse(status_code=status.HTTP_200_OK, content=res)
    except HTTPException as e:
        return JSONResponse(status_code=e.status_code)
    except Exception as e:
        logger.error(e)
        return JSONResponse(content={"error": str(e)})
