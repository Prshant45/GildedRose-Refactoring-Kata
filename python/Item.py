from pydantic import BaseModel, Field

class Item(BaseModel):
    name: str
    sell_in: int
    quality: int = Field(..., ge=0, le=80) 


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)