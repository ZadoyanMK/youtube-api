import axios from 'axios';

const urlEntripoint = "http://localhost:8000/api"

let headers = {
    "Content-Type": "application/json",
}

const actions = {
    loginAction({dispatch, commit, state}, payload){
        console.log(payload)
        commit('setLoadingStatus', true);
        axios({
            method: 'post',
            url: `${urlEntripoint}/auth/login/`,
            data: payload,
            headers: headers
        })
        .then((response) => {
            console.log(response);
            commit('setLoadingStatus', false);
        })
        .catch((error) => {
            console.log(error.response);
            commit('setLoadingStatus', false);
        })
        // axios.post(`${urlEntripoint}/${}`) {

        // }
    }
}

export default actions;
