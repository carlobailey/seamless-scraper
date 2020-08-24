class RestaurantElements():

    '''
        Current DOM structure for the individual restaurant pages on the
        Seamless site
    '''
    def __init__(self):

        self.version = "Seamless_DOM_Elements_200701"

        self.elements = {
        'NAME':{'tag': 'h1', 'attr': 'class', 'value': 'ghs-restaurant-nameHeader',
                'hint': 'tag containing restaurant name'},
        'PHONE':{'tag': 'span', 'attr':'class', 'value':'restaurant-phone',
                  'hint': 'tag containing phone number'},
        'DISTANCE_ADDRESS':{'tag': 'div', 'attr':'at-distancefromdiner',
                            'value':'true',
                            'hint': 'tag for distance between address and restaurant, required for removing from address text'},
        'ADDRESS':{'tag': 'a', 'attr':'class',
                   'value':'restaurantAbout-info-address',
                   'hint': 'tag containing address'},
        'POP_ITEMS_PANEL':{'tag': 'div', 'attr':'id',
                           'value':'menuSectionpopularItemsExpansionPanel',
                           'hint': 'container for popular items banner, following elements are the popular item names + prices'},
        'POP_NAMES':{'tag': 'div', 'attr':'class',
                     'value':'menuItem-name',
                     'hint': 'tag containing popular item name'},
        'POP_PRICE':{'tag': 'div', 'attr':'class',
                     'value':'menuItem-price',
                     'hint': 'tag containing popular item price'},
        'MENU':{'tag': 'ghs-restaurant-menu-item', 'attr': None, 'value': None,
                'hint': 'section containing all restaurant menu elements'},
        'MENU_NAME':{'tag': 'a', 'attr':'class', 'value':'menuItem-name',
                     'hint': 'tag containing menu item name'},
        'MENU_PRICE':{'tag': 'span', 'attr':'class',
                      'value':'menuItem-displayPrice',
                      'hint': 'tag containing menu item price'}
        }

    def tag(self,k):
        '''
            getting tag for a key
            :param k: the key
            :return tag
        '''
        return(self.elements[k]['tag'])

    def attr(self,k):
        '''
            getting attribute for a key
            :param k: the key
            :return attr
        '''
        return(self.elements[k]['attr'])

    def value(self,k):
        '''
            getting value for a key
            :param k: the key
            :return value
        '''
        return(self.elements[k]['value'])

    def override(self,key,subkey,value):
        '''
            override an existing sub-key of key with value
        '''
        assert key
        assert subkey
        assert value
        if key in self.elements:
            self.elements[key][subkey]=value
            return
        raise Exception("Unknown key")
