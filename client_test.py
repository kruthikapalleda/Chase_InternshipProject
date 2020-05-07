import unittest
from client import getDataPoint, getRatio

class ClientTest(unittest.TestCase):

#Unit Test Cases for getDataPoint;

  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]

    for n in quotes:
      self.assertEqual(getDataPoint(n),(n['stock'], n['top_bid']['price'], n['top_ask']['price'], (n['top_bid']['price'] + n['top_ask']['price'])/2))
    """ ------------ Add the assertion below ------------ """

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    for n in quotes:
      self.assertEqual(getDataPoint(n),(n['stock'], n['top_bid']['price'], n['top_ask']['price'], (n['top_bid']['price'] + n['top_ask']['price'])/2))
    """ ------------ Add the assertion below ------------ """

    #Check for null(value) inputs in top_ask with respect to top_price and size;

  def test_ForNull_valueForTop_ask(self):
     n = [
       {'top_ask': {'price': 0, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 115.48, 'size': 67}, 'id': '0.109974697771', 'stock': 'ABC'},
       {'top_ask': {'price': 110.89, 'size': 0}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 100.09, 'size': 99}, 'id': '0.109974697771', 'stock': 'ABC'},
     ]
     for n in n:
       self.assertEqual(getDataPoint(n), (n['stock'], n['top_bid']['price'], n['top_ask']['price'],(n['top_bid']['price'] + n['top_ask']['price']) / 2))

    #Check for null(value) inputs in top_bid with respect to top_price and size;


  def test_ForNull_valueForTop_bid(self):
     quotes = [
       {'top_ask': {'price': 96.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 10}, 'id': '0.109974697771', 'stock': 'ABC'},
       {'top_ask': {'price': 96.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 44, 'size': 0}, 'id': '0.109974697771', 'stock': 'ABC'},
     ]
     for n in quotes:
       self.assertEqual(getDataPoint(n), (n['stock'], n['top_bid']['price'], n['top_ask']['price'],(n['top_bid']['price'] + n['top_ask']['price']) / 2))

    #Check if the testcase has duplicates stocks , datas ;

  def test_ForDuplicate_value(self):
     quotes = [
       {'top_ask': {'price': 96.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 89.05, 'size': 66}, 'id': '0.109974697771', 'stock': 'DEF'},
       {'top_ask': {'price': 96.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 89.05, 'size': 66}, 'id': '0.109974697771', 'stock': 'DEF'},
     ]
     for n in quotes:
      self.assertEqual(getDataPoint(n), (n['stock'], n['top_bid']['price'], n['top_ask']['price'], (n['top_bid']['price'] + n['top_ask']['price']) / 2))

  """ ------------ Add more unit tests ------------ """

  # Check for null(value) inputs in stock;

  def test_ForNull_valueForStock(self):
     quotes = [
       {'top_ask': {'price': 96.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 0, 'size': 10}, 'id': '0.109974697771', 'stock': ''},
       {'top_ask': {'price': 96.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 44, 'size': 0}, 'id': '0.109974697771', 'stock': ''},
     ]
     for n in quotes:
       self.assertEqual(getDataPoint(n), (n['stock'], n['top_bid']['price'], n['top_ask']['price'],(n['top_bid']['price'] + n['top_ask']['price']) / 2))


#Unit test cases for getRation;

  #Check for actual result which equals to expected result;

  def test_value_ActualResult_Equals_ExpectedResults(self):
    quotes = [
        {'price_a' : 10.8 , 'price_b' : 5.7 }
    ]
    for q in quotes:
      self.assertEqual(getRatio(q['price_a'],q['price_b']) , 1.8947368421052633)

  #Check for negative result value;

  def test_Negative_ValueResult(self):
      quotes = [
          {'price_a': -10.8 , 'price_b' : 5.7 }
      ]
      for q in quotes:
          self.assertEqual(getRatio(q['price_a'],q['price_b']), -1.8947368421052633)


if __name__ == '__main__':
    unittest.main()
