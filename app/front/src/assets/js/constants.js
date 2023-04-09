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