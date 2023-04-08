import { FetchAPI } from "./FetchAPI";
import { ARRIVED_CARS_URL, STAY_CARS_URL, LOAD_CARS_URL, LOAD_AUTH_CARS_URL, LOAD_DEL_CARS_URL, fetchInterval, intervals, prevData } from "./constants";
import { isEqual } from "lodash";

export default function() {
    console.log('scripts')

    // GLOBAL
    const loadData = async (url, body = {}) => {
        return await FetchAPI.getData(url, body);
    }

    const createCheckbox = (classNames, name, formId = null) => {
        const check = document.createElement('input');
        check.type = 'checkbox';
        check.name = name;
        check.classList.add(...classNames);
        if(formId) check.setAttribute('form', formId);
        return check;
    }

    const createTd = (classNames, text) => {
        const td = document.createElement('td');
        if(typeof text === 'string') {
            td.innerHTML = text;
        } else {
            td.append(text);
        }
        td.classList.add(...classNames);
        return td;
    }

    const createTr = (classNamesTr, classNamesTd, tds) => {
        const tr = document.createElement('tr');
        for(const td of tds) {
            tr.append(createTd(classNamesTd, td));
        }
        tr.classList.add(...classNamesTr);
        return tr;
    }

    const clearTable = (table) => {
        for(const tr of table.querySelectorAll('tr')) {
            if(tr.classList.contains('table-heading')) continue;
            tr.remove();
        }
    }

    const setUpdateFetch = (form, url, intervalId, constData) => {
        if(!intervals[intervalId]) clearInterval(intervals[intervalId]);
        intervals[intervalId] = setInterval(() => {
            loadData(url)
                .then((resp) => {
                    resetData(form, resp, constData, constData);
                })
        }, fetchInterval);
    }

    const resetData = (form, data, checkData, tableName) => {
        if(isEqual(data, prevData[checkData])) return;
        let table = form.querySelector('table > tbody');
        if(!table) table = form.querySelector('table');
        switch(tableName) {
            case 'arrivedData':
                setArrivedTable(table, data);
            case 'stayData':
                setStayTable(table, data);
            default:
                console.log('unknown data table')
        }
    }

    // ARRIVED_FORM
    const arrivedForm = document.querySelector('#cars-arrived');

    const setArrivedTable = (table, data) => {
        clearTable(table);
        for(const item of data.propusk) {
            const checkbox = createCheckbox(['main__checkbox'], item.id);
            const tr = createTr(['main__tr'], ['main__td'], Object.values(item));
            tr.append(createTd(['main__td'], checkbox));
            table.append(tr);
        }
    }

    const handleArrivedForm = async (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);
        /* for(const input of form.elements) {
            if(input.type === 'checkbox') formData.append(input.name, input.checked);
        } */

        submit.disabled = true;
        loadData(ARRIVED_CARS_URL, formData)
            .then((resp) => {
                resetData(form, resp, 'arrivedData');
                submit.disabled = false;
            })
    }
    
    if(arrivedForm) {
        arrivedForm.classList.add('loading');
        loadData(ARRIVED_CARS_URL)
            .then((data) => {
                prevData.arrivedData = data;
                arrivedForm.classList.remove('loading');
                let table = arrivedForm.querySelector('table > tbody');
                if(!table) table = arrivedForm.querySelector('table');
                setArrivedTable(table, data);
            });
        arrivedForm.addEventListener('submit', handleArrivedForm);
        setUpdateFetch(arrivedForm, ARRIVED_CARS_URL, 'arrivedCarsInterval', 'arrivedData');
    }

    // STAY_FORM
    const stayForm = document.querySelector('#cars-stay');

    const setStayTable = (table, data) => {
        clearTable(table);
        for(const item of data.propusk) {
            const tr = createTr(['main__tr'], ['main__td'], Object.values(item));
            table.append(tr);
        }
    }

    const handleStayForm = async (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);
        /* for(const input of form.elements) {
            if(input.type === 'checkbox') formData.append(input.name, input.checked);
        } */

        submit.disabled = true;
        loadData(STAY_CARS_URL, formData)
            .then((resp) => {
                resetData(form, resp, 'stayData', 'stayData');
                submit.disabled = false;
            })
    }
    
    if(stayForm) {
        stayForm.classList.add('loading');
        loadData(STAY_CARS_URL)
            .then((data) => {
                prevData.stayData = data;
                stayForm.classList.remove('loading');
                let table = stayForm.querySelector('table > tbody');
                if(!table) table = stayForm.querySelector('table');
                setStayTable(table, data);
            });
            stayForm.addEventListener('submit', handleStayForm);
        setUpdateFetch(stayForm, STAY_CARS_URL, 'stayCarsInterval', 'stayData');
    }

    // LOAD_FORM
    const loadForm = document.querySelector('#cars-load');

    const setLoadTable = (table, data) => {
        clearTable(table);
        for(const item of data.propusk) {
            const tr = createTr(['main__tr'], ['main__td'], Object.values(item));
            table.append(tr);
        }
    }

    const handleLoadForm = async (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);
        /* for(const input of form.elements) {
            if(input.type === 'checkbox') formData.append(input.name, input.checked);
        } */

        submit.disabled = true;
        loadData(LOAD_CARS_URL, formData)
            .then((resp) => {
                resetData(form, resp, 'loadData', 'loadData');
                submit.disabled = false;
            })
    }
    
    if(loadForm) {
        loadForm.classList.add('loading');
        loadData(LOAD_CARS_URL)
            .then((data) => {
                prevData.loadData = data;
                loadForm.classList.remove('loading');
                let table = loadForm.querySelector('table > tbody');
                if(!table) table = loadForm.querySelector('table');
                setLoadTable(table, data);
            });
            loadForm.addEventListener('submit', handleLoadForm);
        setUpdateFetch(loadForm, LOAD_CARS_URL, 'loadCarsInterval', 'loadData');
    }

    // AUTH_FORM
    const authForm = document.querySelector('#auth');

    const handleAuthForm = (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);
        /* for(const input of form.elements) {
            if(input.type === 'checkbox') formData.append(input.name, input.checked);
        } */

        submit.disabled = true;
        loadData(LOAD_AUTH_CARS_URL, formData)
            .then((resp) => {
                resetData(form, resp, 'loadData', 'loadData');
                submit.disabled = false;
            })
    }

    if(authForm) {
        authForm.addEventListener('submit', handleAuthForm)
    }

    // DEL_FORM
    const delForm = document.querySelector('#del');

    const handleDelForm = (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);
        /* for(const input of form.elements) {
            if(input.type === 'checkbox') formData.append(input.name, input.checked);
        } */

        submit.disabled = true;
        loadData(LOAD_DEL_CARS_URL, formData)
            .then((resp) => {
                resetData(form, resp, 'loadData', 'loadData');
                submit.disabled = false;
            })
    }

    if(delForm) {
        delForm.addEventListener('submit', handleDelForm)
    }
}