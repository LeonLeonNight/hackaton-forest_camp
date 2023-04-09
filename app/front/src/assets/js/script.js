import { FetchAPI } from "./FetchAPI";
import { ARRIVED_CARS_URL, STAY_CARS_URL, LOAD_CARS_URL, LOAD_AUTH_CARS_URL, LOAD_DEL_CARS_URL, INSIDE_CARS_URL, KPP_CARS_URL, fetchInterval, intervals, prevData, formNames, carsState } from "./constants";
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

    const createRadio = (classRadio, classLabel, name, text, clickFn, formId = null) => {
        const radio = document.createElement('input');
        const label = document.createElement('label');
        radio.type = 'radio';
        radio.name = name;
        radio.classList.add(...classRadio);
        radio.addEventListener('click', clickFn);
        label.classList.add(...classLabel);
        label.innerHTML = text;
        if(formId) radio.setAttribute('form', formId);
        label.append(radio);
        return label;
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

    const createComplexTd = (classNames, elements) => {
        const td = document.createElement('td');
        td.append(...elements);
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

    const deleteCheckedRadioState = (event) => {
        const e = event.target;
        const td = e.closest('td');
        for(const input of td.querySelectorAll('input[type="radio"]')) {
            if(input != e) input.oldChecked = false;
        }
        if(e?.oldChecked) {
            e.checked = false;
        }
        e.oldChecked = e.checked;
    }

    const setUpdateFetch = (form, url, intervalId, constData, state) => {
        if(!intervals[intervalId]) clearInterval(intervals[intervalId]);
        intervals[intervalId] = setInterval(() => {
            loadData(url)
                .then((resp) => {
                    resetData(form, formNewData(resp, state), constData, constData);
                })
        }, fetchInterval);
    }

    const resetData = (form, data, checkData, tableName) => {
        if(data === undefined) {
            console.log(tableName+'data is undefined');
            return;
        }
        if(isEqual(data, prevData[checkData])) return;
        let table = form.querySelector('table > tbody');
        if(!table) table = form.querySelector('table');
        switch(tableName) {
            case 'arrivedData':
                setArrivedTable(table, data);
            case 'stayData':
                setStayTable(table, data);
            case 'loadData':
                setLoadTable(table, data);
            case 'insideData':
                setInsideTable(table, data);
            case 'kppData':
                setKppTable(table, data);
            default:
                console.log('unknown data table')
        }
    }

    const formNewData = (resp, state) => {
        const cloneResp = [];
        for(const item of resp) {
            const cloneItem = {}
            for(const name of formNames[state]) {
                cloneItem[name] = item[name];
            }
            cloneResp.push(cloneItem);
        }
        return cloneResp;
    }

    // ARRIVED_FORM
    const arrivedForm = document.querySelector('#cars-arrived');

    const setArrivedTable = (table, data) => {
        if(data === undefined) {
            console.log('data is undefined')
            return;
        }
        clearTable(table);
        for(const item of data) {
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

        submit.disabled = true;
        loadData(ARRIVED_CARS_URL, formData)
            .then((resp) => {
                resetData(form, formNewData(resp, 1), 'arrivedData');
                submit.disabled = false;
            })
    }
    
    if(arrivedForm) {
        arrivedForm.classList.add('loading');
        loadData(ARRIVED_CARS_URL)
            .then((data) => {
                if(data === undefined) {
                    console.log('data is undefined')
                    return;
                }
                const newData = formNewData(data, 1);
                prevData.arrivedData = newData;
                arrivedForm.classList.remove('loading');
                let table = arrivedForm.querySelector('table > tbody');
                if(!table) table = arrivedForm.querySelector('table');
                setArrivedTable(table, newData);
            });
        arrivedForm.addEventListener('submit', handleArrivedForm);
        setUpdateFetch(arrivedForm, ARRIVED_CARS_URL, 'arrivedCarsInterval', 'arrivedData', 1);
    }

    // STAY_FORM
    const stayForm = document.querySelector('#cars-stay');

    const setStayTable = (table, data) => {
        if(data === undefined) {
            console.log('data is undefined')
            return;
        }
        clearTable(table);
        for(const item of data) {
            const tr = createTr(['main__tr'], ['main__td'], Object.values(item));
            table.append(tr);
        }
    }

    const handleStayForm = async (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);

        submit.disabled = true;
        loadData(STAY_CARS_URL, formData)
            .then((resp) => {
                resetData(form, formNewData(resp, 2), 'stayData', 'stayData');
                submit.disabled = false;
            })
    }
    
    if(stayForm) {
        stayForm.classList.add('loading');
        loadData(STAY_CARS_URL)
            .then((data) => {
                if(data === undefined) {
                    console.log('data is undefined')
                    return;
                }
                const newData = formNewData(data, 2);
                prevData.stayData = newData;
                stayForm.classList.remove('loading');
                let table = stayForm.querySelector('table > tbody');
                if(!table) table = stayForm.querySelector('table');
                setStayTable(table, newData);
            });
            stayForm.addEventListener('submit', handleStayForm);
        setUpdateFetch(stayForm, STAY_CARS_URL, 'stayCarsInterval', 'stayData', 2);
    }

    // INSIDE_FORM
    const insideForm = document.querySelector('#cars-inside');

    const setInsideTable = (table, data) => {
        if(data === undefined) {
            console.log('data is undefined')
            return;
        }
        clearTable(table);
        for(const item of data) {
            const radio1 = createRadio(['main__checkbox'], ['main__label'], item.id, 'Север', deleteCheckedRadioState);
            const radio2 = createRadio(['main__checkbox'], ['main__label'], item.id, 'Юг', deleteCheckedRadioState);
            const tr = createTr(['main__tr'], ['main__td'], Object.values(item));
            tr.append(createComplexTd(['main__td'], [radio1, radio2]));
            table.append(tr);
        }
    }

    const handleInsideForm = async (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);

        submit.disabled = true;
        loadData(INSIDE_CARS_URL, formData)
            .then((resp) => {
                resetData(form, formNewData(resp, 3), 'insideData');
                submit.disabled = false;
            })
    }
    
    if(insideForm) {
        insideForm.classList.add('loading');
        loadData(INSIDE_CARS_URL)
            .then((data) => {
                if(data === undefined) {
                    console.log('data is undefined')
                    return;
                }
                const newData = formNewData(data, 3);
                prevData.insideData = newData;
                insideForm.classList.remove('loading');
                let table = insideForm.querySelector('table > tbody');
                if(!table) table = insideForm.querySelector('table');
                setInsideTable(table, newData);
            });
        insideForm.addEventListener('submit', handleInsideForm);
        setUpdateFetch(insideForm, INSIDE_CARS_URL, 'insideCarsInterval', 'insideData', 3);
    }

    // LOAD_FORM
    const loadForm = document.querySelector('#cars-load');

    const setLoadTable = (table, data) => {
        if(data === undefined) {
            console.log('data is undefined')
            return;
        }
        clearTable(table);
        for(const item of data) {
            const tr = createTr(['main__tr'], ['main__td'], Object.values(item));
            table.append(tr);
        }
    }

    const handleLoadForm = async (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData(form);

        submit.disabled = true;
        loadData(LOAD_CARS_URL, formData)
            .then((resp) => {
                resetData(form, formNewData(resp, 4), 'loadData', 'loadData');
                submit.disabled = false;
            })
    }
    
    if(loadForm) {
        loadForm.classList.add('loading');
        loadData(LOAD_CARS_URL)
            .then((data) => {
                if(data === undefined) {
                    console.log('data is undefined')
                    return;
                }
                const newData = formNewData(data, 4);
                prevData.loadData = newData;
                loadForm.classList.remove('loading');
                let table = loadForm.querySelector('table > tbody');
                if(!table) table = loadForm.querySelector('table');
                setLoadTable(table, newData);
            });
            loadForm.addEventListener('submit', handleLoadForm);
        setUpdateFetch(loadForm, LOAD_CARS_URL, 'loadCarsInterval', 'loadData', 4);
    }

    // AUTH_FORM
    const authForm = document.querySelector('#auth');

    const handleAuthForm = (event) => {
        event.preventDefault();

        const form = event.target;
        const submit = form.elements['submit'];
        const formData = new FormData();

        formData.append('pass_number', form.talonId)

        submit.disabled = true;
        loadData(LOAD_AUTH_CARS_URL, formData)
            .then((resp) => {
                //resetData(form, resp, 'loadData', 'loadData');
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

        submit.disabled = true;
        loadData(LOAD_DEL_CARS_URL, formData)
            .then((resp) => {
                //resetData(form, resp, 'loadData', 'loadData');
                submit.disabled = false;
            })
    }

    if(delForm) {
        delForm.addEventListener('submit', handleDelForm)
    }

    // KPP_FORM
    const kppForm = document.querySelector('#cars-kpp');

    const setKppTable = (table, data) => {
        if(data === undefined) {
            console.log('data is undefined')
            return;
        }
        for(const item of data) {
            item.state = carsState[item.state];
        }
        clearTable(table);
        for(const item of data) {
            const tr = createTr(['main__tr'], ['main__td'], Object.values(item));
            table.append(tr);
        }
    }
    
    if(kppForm) {
        kppForm.classList.add('loading');
        loadData(KPP_CARS_URL)
            .then((data) => {
                if(data === undefined) {
                    console.log('data is undefined')
                    return;
                }
                const newData = formNewData(data, 5);
                prevData.kppData = newData;
                kppForm.classList.remove('loading');
                let table = kppForm.querySelector('table > tbody');
                if(!table) table = kppForm.querySelector('table');
                setKppTable(table, newData);
            });
        setUpdateFetch(kppForm, KPP_CARS_URL, 'loadKppInterval', 'kppData', 5);
    }

    // COLLAPSE_TABLE
    const toggleBtns = document.querySelectorAll('*[data-toggle-data');

    const hideOrShowData = (event) => {
        event.target.closest('form').querySelector('table').classList.toggle('collapse');
    }

    if(toggleBtns.length) {
        for(const btn of toggleBtns) {
            btn.addEventListener('click', hideOrShowData);
        }
    }

    // ACTIVATE_LINKS
    const links = document.querySelectorAll('.header__link');

    const highlightLinks = (event) => {
        const e = event.target;
        for(const link of links) {
            if(link != e) {
                link.classList.remove('active');
            } else {
                link.classList.add('active');
            }
        }
    }

    if(links.length) {
        for(const link of links) {
            link.addEventListener('click', highlightLinks)
        }
    }
}