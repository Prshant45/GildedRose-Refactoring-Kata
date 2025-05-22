# -*- coding: utf-8 -*-
from Validators import *

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def get_updater(self, item):
        if item.name == "Aged Brie":
            return AgedBrieUpdater()
        elif item.name == "Backstage passes to a TAFKAL80ETC concert":
            return BackstagePassUpdater()
        elif item.name == "Sulfuras, Hand of Ragnaros":
            return SulfurasUpdater()
        elif item.name.startswith("Conjured"):
            return ConjuredItemUpdater()
        else:
            return NormalItemUpdater()

    def update_quality(self):
        for item in self.items:
            updater = self.get_updater(item)
            updater.update(item)
            
