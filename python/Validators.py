from abc import ABC, abstractmethod
from Item import Item

class ItemUpdater(ABC):
    @abstractmethod
    def update(self, item: Item):
        pass

class NormalItemUpdater(ItemUpdater):
    def update(self, item: Item):
        item.sell_in -= 1
        degrade = 2 if item.sell_in < 0 else 1
        item.quality = max(0, item.quality - degrade)

class AgedBrieUpdater(ItemUpdater):
    def update(self, item: Item):
        item.sell_in -= 1
        increase = 2 if item.sell_in < 0 else 1
        item.quality = min(50, item.quality + increase)

class BackstagePassUpdater(ItemUpdater):
    def update(self, item: Item):
        item.sell_in -= 1
        if item.sell_in < 0:
            item.quality = 0
        elif item.sell_in < 5:
            item.quality = min(50, item.quality + 3)
        elif item.sell_in < 10:
            item.quality = min(50, item.quality + 2)
        else:
            item.quality = min(50, item.quality + 1)

class SulfurasUpdater(ItemUpdater):
    def update(self, item):
        pass

class ConjuredItemUpdater(ItemUpdater):
    def update(self, item: Item):
        item.sell_in -= 1
        degrade = 4 if item.sell_in < 0 else 2
        item.quality = max(0, item.quality - degrade)
