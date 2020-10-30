class Luhn:
    def __init__(self, card_num):
        self.card_num = card_num.replace(" ", "")

    def valid(self):
        card_num_lst = list(self.card_num)
        if len(card_num_lst) <= 1:
            return False
        for i in range(len(card_num_lst)):
            if card_num_lst[i].isdigit():
                if i % 2 == 0:
                    card_num_lst[i] = int(card_num_lst[i]) * 2
                    if card_num_lst[i] > 9:
                        card_num_lst[i] = int(card_num_lst[i]) - 9
                else:
                    card_num_lst[i] = int(card_num_lst[i])
            else: return False
        return sum(card_num_lst) % 10 == 0