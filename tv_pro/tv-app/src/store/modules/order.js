import {
    HTTP
} from '../../common'

const state = {
    status:''
}
const getters = {
       STATUS: state => {
         return state.status;
     },
}
const mutations = {
             SET_ORDER: (state, payload) => {
                 state.status = payload;
             },
}
const actions = {
        SEND_ORDER:async (context, data) => {
            return HTTP.post('/order/', {
                params: {
                    data: data
                }
            }).then(response => {
                data = response.data;
                context.commit('SET_ORDER', data);
            })
        },
}
export default {
    state,
    getters,
    mutations,
    actions
}