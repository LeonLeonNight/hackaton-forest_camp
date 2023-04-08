import axios from 'axios';

const data = {
    propusk: [
        {
            id: '5000000429570',
            nomer: 'В029МХ/797',
        },
        {
            id: '5000000429750',
            nomer: 'Р125АН/797',
        },
    ]
}

class FetchAPIClass {
  /* getData = (url, request) => {
    return axios
      .get(url, {
        params: { request },
      })
      .then((response) => response.data);
  }; */
  getData = (url, request) => {
    return new Promise((res, rej) => {
        setTimeout(() => res(data), 1000);
    })
  }
}

export const FetchAPI = new FetchAPIClass();
