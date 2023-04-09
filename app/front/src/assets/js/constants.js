export const ARRIVED_CARS_URL = '';
export const STAY_CARS_URL = '';
export const LOAD_CARS_URL = '';
export const LOAD_AUTH_CARS_URL = '/registered_drivers_kpp/';
export const LOAD_DEL_CARS_URL = '';
export const INSIDE_CARS_URL = '';
export const KPP_CARS_URL = '';

export const fetchInterval = 3000;

export const intervals = {
    arrivedCarsInterval: null,
    stayCarsInterval: null,
    loadCarsInterval: null,
    insideCarsInterval: null,
    insideKppInterval: null,
}

export const prevData = {
    arrivedData: {},
    stayData: {},
    loadData: {},
    insideData: {},
    kppData: {},
}

// Состояния для отслеживания положения машины в процессе погрузки
export const carsState = {
    1: 'Зарегистрирована',
    2: 'На внут. стоянке',
    3: 'На внут. стоянке',
    4: 'Загрузка товара',
    5: 'Покинула территорию'
}

// Данные, нужные для формирования таблицы, исходя из состояния погрузки машины
export const formNames = {
    1: ['pass_number', 'auto_number', 'driver', 'client', 'goods', 'count', 'measurement_system_type'], //машина зарегистрирована (соответствует состоянию 1)
    2: ['pass_number', 'auto_number'], //машина приглашается на внутреннюю стоянку (соответствует состоянию 2)
    3: ['pass_number', 'auto_number', 'driver', 'client', 'goods', 'count', 'measurement_system_type'], //машина стоит на внутренней стоянке (соответствует состоянию 2)
    4: ['pass_number', 'auto_number', 'gates'], //машина приглашена к южным или северным воротам (соответствует состоянию 3 и 4)
    5: ['pass_number', 'auto_number', 'driver', 'client', 'goods', 'count', 'measurement_system_type', 'state'], //общий список машин и их состояний
}