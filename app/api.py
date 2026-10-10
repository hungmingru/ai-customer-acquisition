from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from app.campaign import CampaignEngine
from app.config import settings
from app.copywriter import CopyWriter
from app.phone_controller import PhoneController
from app.poi_search import POISearch
from app.qq_controller import QQController

app = FastAPI(title="AI Auto Lead Generation")

poi = POISearch(amap_key=settings.amap_key, baidu_key=settings.baidu_key)
writer = CopyWriter(api_key=settings.openai_api_key, model=settings.openai_model)
qq = QQController(token=settings.qq_platform_token, group_ids=settings.qq_group_ids)
phone = PhoneController(serial=settings.adb_serial)
engine = CampaignEngine(poi=poi, writer=writer, qq=qq, phone=phone)


class CampaignRequest(BaseModel):
    keyword: str
    city: str
    product: str


@app.get("/health")
async def health():
    return {"status": "ok", "app": settings.app_name}


@app.post("/campaign/run")
async def run_campaign(req: CampaignRequest):
    try:
        result = await engine.run(
            keyword=req.keyword,
            city=req.city,
            product=req.product,
            target_group_ids=settings.qq_group_ids,
        )
        return result
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))


@app.get("/devices")
async def get_devices():
    try:
        return {"devices": phone.get_devices()}
    except Exception as exc:
        raise HTTPException(status_code=500, detail=str(exc))
