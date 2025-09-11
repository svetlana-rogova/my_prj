def filter_by_state(dictionaries: list, state: str = "EXECUTED") -> list:
    """Поиск словаря со значением 'выполнено'"""
    return [meaning for meaning in dictionaries if meaning["state"] == 'EXECUTED']


if __name__ == "__main__":
    print(filter_by_state([
         {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
         {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
         {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
         {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]))


def sort_by_date(list_dict: list, order: bool = True):
    """Сортировка списка по дате"""
    return sorted(list_dict, key = lambda p:p["date"], reverse = order)


if __name__ == "__main__":
    print(sort_by_date([
         {"id": "41428829", "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
         {"id": "939719570", "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
         {"id": "594226727", "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
         {"id": "615064591", "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"}
    ]))
