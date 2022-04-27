import fastapi

router = fastapi.APIRouter()

@router.get('/')
def index():
    return 'Welcome to the AI Core DOB Service'
