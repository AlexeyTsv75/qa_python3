import datetime


class OnlineSalesRegisterCollector:

    def __init__(self):
        self.__name_items = []
        self.__number_items = 0
        self.__item_price = {'чипсы': 50, 'кола': 100, 'печенье': 45, 'молоко': 55, 'кефир': 70}
        self.__tax_rate = {'чипсы': 20, 'кола': 20, 'печенье': 20, 'молоко': 10, 'кефир': 10}

    @property
    def name_items(self):
        return self.__name_items

    @property
    def number_items(self):
        return self.__number_items

    def add_item_to_cheque(self, name):
        if len(name) == 0 or len(name) > 40:
            raise ValueError('Нельзя добавить товар, если в его названии нет символов или '
                             'их больше 40')
        elif name not in self.__item_price:
            raise NameError('Позиция отсутствует в товарном справочнике')
        self.__name_items.append(name)
        self.__number_items += 1

    def delete_item_from_check(self, name):
        if name not in self.__name_items:
            raise NameError('Позиция отсутствует в чеке')
        self.__name_items.remove(name)
        self.__number_items -= 1

    def check_amount(self):
        total = []
        amount = 0
        for item in self.__name_items:
            total.append(self.__item_price[item])
        amount = sum(total)
        if len(total) > 10:
            amount = int(amount-amount * 0.1)
        return amount

    def twenty_percent_tax_calculation(self):
        twenty_percent_tax = []
        total = []
        tax_twenty_amount = 0
        for item in self.__name_items:
            if self.__tax_rate[item] == 20:
                twenty_percent_tax.append(item)
        for i in twenty_percent_tax:
            total.append(self.__item_price[i])
        tax_twenty_amount = sum(total)*0.2
        if len(self.__name_items) > 10:
            tax_twenty_amount = tax_twenty_amount-tax_twenty_amount * 0.1
        return tax_twenty_amount

    def ten_percent_tax_calculation(self):
        ten_percent_tax = []
        total = []
        tax_ten_amount = 0
        for item in self.__name_items:
            if self.__tax_rate[item] == 10:
                ten_percent_tax.append(item)
        for i in ten_percent_tax:
            total.append(self.__item_price[i])
        tax_ten_amount = sum(total)*0.1
        if len(self.__name_items) > 10:
            tax_ten_amount = tax_ten_amount-tax_ten_amount * 0.1
        return tax_ten_amount

    def total_tax(self):
        return self.ten_percent_tax_calculation()+self.twenty_percent_tax_calculation()


asd = OnlineSalesRegisterCollector()
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('кола')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('кола')
asd.add_item_to_cheque('чипсы')
asd.add_item_to_cheque('молоко')
print(asd.number_items)
print(asd.name_items)
print(asd.check_amount())
print(asd.twenty_percent_tax_calculation())
print(asd.ten_percent_tax_calculation())
print(asd.total_tax())
