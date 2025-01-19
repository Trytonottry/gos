import numpy as np

def assign_taxis(orders, taxis, routes):
    """Упрощенный алгоритм назначения такси."""
    assigned_orders = {}
    for taxi in taxis:
        if taxi['status'] == 'available':
            best_order = None
            min_distance = float('inf')
            for order in orders:
                if order['pier'] != taxi['current_pier']:
                    # Найдите расстояние (замените на более точный расчет)
                    distance = get_route_time(taxi['current_pier'], order['pier'], routes)
                    if distance < min_distance:
                        min_distance = distance
                        best_order = order

            if best_order:
                assigned_orders[taxi['taxi_id']] = best_order
                taxi['status'] = 'occupied'
                orders.remove(best_order)

    return assigned_orders


def get_route_time(pier1_id, pier2_id, routes):
    """Функция для получения времени в пути между причалами (заглушка)."""
    for route in routes:
        if (route['pier1'] == pier1_id and route['pier2'] == pier2_id) or (route['pier1'] == pier2_id and route['pier2'] == pier1_id):
            return route['travel_time'].total_seconds()  #Возвращает время в секундах
    return float('inf') #Нет маршрута

# Пример данных
orders = [
    {'order_id': 1, 'pier': 1, 'destination_pier': 3},
    {'order_id': 2, 'pier': 2, 'destination_pier': 4}
]
taxis = [
    {'taxi_id': 1, 'current_pier': 1, 'status': 'available'},
    {'taxi_id': 2, 'current_pier': 2, 'status': 'available'}
]
routes = [
    {'route_id': 1, 'pier1': 1, 'pier2': 3, 'travel_time': '00:15:00'},
    {'route_id': 2, 'pier1': 2, 'pier2': 4, 'travel_time': '00:20:00'}
]

assignments = assign_taxis(orders, taxis, routes)
print(assignments)
