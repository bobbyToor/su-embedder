from dotenv import load_dotenv

load_dotenv()

import logging as logger
import uvicorn
from fastapi import FastAPI
from api.api import api_router

fastapp = FastAPI()

fastapp.include_router(api_router)


@fastapp.on_event("startup")
def startup():
    logger.info("App started")


@fastapp.on_event("shutdown")
def shutdown():
    logger.warning("App shutting down")


if __name__ == "__main__":
    uvicorn.run(app=fastapp, host="0.0.0.0", port=3002)
