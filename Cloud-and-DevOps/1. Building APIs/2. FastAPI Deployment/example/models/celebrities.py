from pydantic import BaseModel
from typing import Optional

class Celebrity(BaseModel):
    '''
    This class gives some information about a celebrity. It is intended to be 
    used with the FastAPI example

    Attributes
    ----------
    first_name: str
        The first name of the celebrity
    last_name: str
        The last name of the celebrity
    middle_name: Optional[str]
        The middle name of the celebrity
    city: bool
        If True, the API will also returns the city where the celebrity was born
    '''
    first_name: str
    last_name: str
    middle_name: Optional[str] = None
    city: bool = False