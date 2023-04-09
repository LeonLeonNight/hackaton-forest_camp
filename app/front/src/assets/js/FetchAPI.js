import axios from 'axios';

const data = {
    propusk: [
        {
          pass_number: '5000000429570',
          auto_number: 'В029МХ/797',
          driver: 'qewqe qew qweq',
          client: 'sfdsfsdfsdfs',
          goods: 'sdvbtrhrtt',
          count: 10000,
          measurement_system_type: 'kg',
          gates: 'yug',
          state: 3
        },
        {
          pass_number: '5000000429571',
          auto_number: 'В011МХ/797',
          driver: 'qeweqf43 err erq',
          client: 'sfdsasdvsdvfsdfsdfs',
          goods: 'adwefe',
          count: 100020,
          measurement_system_type: 't',
          gates: 'sever',
          state: 1
        },
    ]
}

class FetchAPIClass {
  /* getData = (url, request) => {
    return axios
      .post('/swagger-ui'+url, {
        request,
      })
      .then((response) => response.data)
      .catch((e) => console.log('Get API '+e));
  }; */
  getData = (url, request) => {
    return new Promise((res, rej) => {
        setTimeout(() => res(data.propusk), 1000);
    })
  }
}

export const FetchAPI = new FetchAPIClass();
