import pprint
from pypred import Predicate
p = Predicate('country is "Russia" and city is "Moscow" and comment contains "Как заказать такси?" and result is "Заказать такси можно в приложении и на сайте «https://taxi.yandex.ru/»"')
assert p.is_valid()
assert p.evaluate({'country': 'Russia', 'city': 'Moscow', 'comment': 'Как заказать такси?', 'result': 'Заказать такси можно в приложении и на сайте «https://taxi.yandex.ru/»'})
res, ctx = p.analyze({'country': 'Russia', 'city': 'Moscow', 'comment': 'Как заказать такси?', 'result': 'Заказать такси можно в приложении и на сайте «https://taxi.yandex.ru/»'})
assert res
assert p.description()
pprint.pprint(ctx.literals)

