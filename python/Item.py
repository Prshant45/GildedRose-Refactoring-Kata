from pydantic import BaseModel

class Item(BaseModel):
    name: str
    sell_in: int
    quality: int


    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)