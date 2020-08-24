from restaurant_elements import RestaurantElements
from bs4 import BeautifulSoup


re = RestaurantElements()

class RestaurantParser():

    def __init__(self, html):
        self.soup = BeautifulSoup(html, features="lxml")

    def _get_name(self):
        tag = re.tag('NAME')
        attr = re.attr('NAME')
        value = re.value('NAME')
        try:
            return self.soup.find(tag, {attr: value}).text
        except AttributeError:
            return None

    def _get_phone_number(self):
        tag = re.tag('PHONE')
        attr = re.attr('PHONE')
        value = re.value('PHONE')
        try:
            return self.soup.find(tag, {attr: value}).text
        except AttributeError:
            return None

    def _get_address(self):
        self.soup.find(re.tag(
            'DISTANCE_ADDRESS'),
            {re.attr('DISTANCE_ADDRESS'):
            re.value('DISTANCE_ADDRESS')}).extract()
        tag = re.tag('ADDRESS')
        attr = re.attr('ADDRESS')
        value = re.value('ADDRESS')
        try:
            return self.soup.find(tag, {attr: value}).text
        except AttributeError:
            return None

    def _get_pop_items(self):
        pop_items = []
        pop_panel = self.soup.find(
            re.tag('POP_ITEMS_PANEL'),
            {re.attr('POP_ITEMS_PANEL'): re.value('POP_ITEMS_PANEL')})
        if pop_panel != None:
            pop_names = pop_panel.next_sibling.find_all(
                re.tag('POP_NAMES'), {re.attr('POP_NAMES'): re.value('POP_NAMES')})
            pop_prices = pop_panel.next_sibling.find_all(
                re.tag('POP_PRICE'), {re.attr('POP_PRICE'): re.value('POP_PRICE')})
            for idx, name in enumerate(pop_names):
                pop_items.append((name.text, pop_prices[idx].text))
            return pop_items
        else:
            return None

    def _get_menu_items(self):
        menu_items = []
        menu_cards = self.soup.find_all(re.tag('MENU'))
        for card in menu_cards:
            try:
                name = card.find(
                    re.tag('MENU_NAME'),
                    {re.attr('MENU_NAME'): re.value('MENU_NAME')}).text
                price = card.find(
                    re.tag('MENU_PRICE'),
                    {re.attr('MENU_PRICE'): re.value('MENU_PRICE')}).text
                menu_items.append((name, price))
            except AttributeError:
                continue
        return menu_items
