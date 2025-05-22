# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def test_foo(self):
        items = [Item(name="foo", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_aged(self):
        items = [Item(name="Aged Brie", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Aged Brie", items[0].name)

    def test_backstage(self):
        items = [Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Backstage passes to a TAFKAL80ETC concert", items[0].name)

    def test_sulfuras(self):
        items = [Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Sulfuras, Hand of Ragnaros", items[0].name)
    
    def test_conjured(self):
        items = [Item(name="Conjured", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("Conjured", items[0].name)
        self.assertEqual(str(items[0]), "name='Conjured' sell_in=-1 quality=0")
        
if __name__ == '__main__':
    unittest.main()
