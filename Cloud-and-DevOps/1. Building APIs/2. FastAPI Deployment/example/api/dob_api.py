import fastapi
from fastapi import Depends
import json
from models.celebrities import Celebrity
# from services.dob_service import get_dob
from services.dob_service_async import get_dob
router = fastapi.APIRouter()


@router.get('/api/dob/{first_name}')
async def dob(celebrity: Celebrity = Depends()):
    report = await get_dob(celebrity.first_name, celebrity.last_name, celebrity.city)
    return fastapi.Response(content=json.dumps(report),
                                media_type='application/json')