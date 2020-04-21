# Greedy Algorithm
"""
Given all three lists, write a function to check that my service is first-come, first-served. All food should come out in the same order customers requested it.

We'll represent each customer order as a unique integer.

As an example,

  Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 4, 6, 5, 3]
would not be first-come, first-served, since order 3 was requested before order 5 but order 5 was served first.

But,

  Take Out Orders: [1, 3, 5]
 Dine In Orders: [2, 4, 6]
  Served Orders: [1, 2, 3, 5, 4, 6]
would be first-come, first-served.
"""

def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    take_out_index = 0
    dine_in_index = 0
    take_out_max_index = len(take_out_orders) - 1
    dine_in_max_index = len(dine_in_orders) - 1
    
    for order in served_orders:
        if (take_out_index <= take_out_max_index) and (take_out_orders[take_out_index] == order):
            take_out_index += 1
        elif (dine_in_index <= dine_in_max_index) and (dine_in_orders[dine_in_index] == order):
            dine_in_index += 1
        else:
            return False
            
    if (take_out_index != len(take_out_orders)) or (dine_in_index != len(dine_in_orders)):
            return False
            
    return True
    
    """ FIRST PASS 
    # take_count = 0
    # dine_count = 0
    # for i in range(len(served_orders)):
    #     current_order = served_orders[i]
    #     if current_order in take_out_orders:
    #         if take_out_orders.index(current_order) != take_count:
    #             return False
    #         take_count += 1
    #     elif current_order in dine_in_orders:
    #         if dine_in_orders.index(current_order) != dine_count:
    #             return False
    #         dine_count += 1
    #     else:
    #         return False
    
    # if (take_count != len(take_out_orders)) or (dine_count != len(dine_in_orders)):
    #     return False
    
    # return True
"""

"""
# Tests

class Test(unittest.TestCase):

    def test_both_registers_have_same_number_of_orders(self):
        result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
        self.assertTrue(result)

    def test_registers_have_different_lengths(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
        self.assertFalse(result)

    def test_one_register_is_empty(self):
        result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
        self.assertTrue(result)

    def test_served_orders_is_missing_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
        self.assertFalse(result)

    def test_served_orders_has_extra_orders(self):
        result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
        self.assertFalse(result)

    def test_one_register_has_extra_orders(self):
        result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
        self.assertFalse(result)

    def test_one_register_has_unserved_orders(self):
        result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
        self.assertFalse(result)


unittest.main(verbosity=2)

"""