import pprint

DATA = [
 {
   "dept": "Отдел информационных систем",
   "name": "Сотрудник 1",
   "phone": "89999999999"
 },
 {
   "dept": "Отдел АСУ",
   "name": "Сотрудник 2",
   "phone": "88888888888"
 },
 {
   "dept": "Отдел информационных систем",
   "name": "Сотрудник 3",
   "hours": 165,
   "phone": "87777777777"
 },
 {
   "dept": "Отдел информационных систем",
   "name": "Сотрудник 4",
   "hours": 132,
   "phone": "86666666666"
 },
 {
   "dept": "Отдел АСУ",
   "name": "Сотрудник 5",
   "hours": 101,
   "phone": "85555555555"
 },
 {
   "dept": "Отдел информационных систем",
   "name": "Сотрудник 6",
   "hours": 98,
   "phone": "84444444444"
 }
]

def groups(data):
    result = {}     # пустой начальный словарь
    count = 0       # начальное количество сотрудников отдела
    people_up = 0   # начальное количество действующих сотружников отдела (тех, кто работал)
                    # в конце нужно будет убрать из выдачи
    avg_hours = 0   # начальная средняя выработка

    # 1 проход, формируем список отделов с начальными (нулевыми) данными
    for item in data:
        result[item.get('dept')] = {
            'count': count,
            'avg_hours': avg_hours,
            'people': [],
            'people_up': people_up
        }

    # 2 проход, реализуем логику подсчета
    for item in data:
        avg_hours = result[item.get('dept')]['avg_hours']

        result[item.get('dept')]['count'] = result[item.get('dept')]['count'] + 1 # считаем количество сотрудников в отделе
        result[item.get('dept')]['people'].append({'name': item.get('name'), 'phone': item.get('phone')}) # наполняем отдел сотрудниками
        if item.get('hours'):
            result[item.get('dept')]['people'].append({'hours': item.get('hours')})
            result[item.get('dept')]['people_up'] = result[item.get('dept')]['people_up'] + 1   # считаем количество действующих сотрудников
            result[item.get('dept')]['avg_hours'] = avg_hours + item.get('hours')               # суммируем часы


    # считаем среднюю наработку
    result[item.get('dept')]['avg_hours'] = round(
        result[item.get('dept')]['avg_hours'] / result[item.get('dept')]['people_up']
        )
    # удаляем people_up из выдачи
    result[item.get('dept')].pop('people_up')
    
    return result


def main():
    pprint.pprint(groups(DATA))



if __name__ == '__main__':
    main()

