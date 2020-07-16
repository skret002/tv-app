import {
    HTTP
} from '../../common'

const state = {
    staff: null,
    center_info:null,
    sale: '',
}
const getters = {
    STAFF: state => {
        return state.staff;
    },
    CONTET_FOOTER: state => {
            return state.center_info;
        },
    SALE: state => {
            return state.sale;
        },
}
const mutations = {
    SET_STAFF: (state, payload) => {
        state.staff = payload;
    },
    SET_CONTET_FOOTER: (state, payload) => {
        state.center_info = payload;
    },
    SET_SALE: (state, payload) => {
        state.sale = payload;
    },
}
const actions = {
    GET_STAFF: async (context, data) => {
        return HTTP.post('/footer_staff/', {
            params: {
                data: data
            }
        }).then(response => {
            data = response.data;
            context.commit('SET_STAFF', data);
            return response.data
        })
    },
        GET_CONTENT_FOOTER: async (context, data) => {
        return HTTP.get('/content_in_footer/', {
            params: {
                data: data
            }
        }).then(response => {
            data = response.data;
            context.commit('SET_CONTET_FOOTER', data);
            return response.data
        })
    },
        GET_SALE: async (context, data) => {
            return HTTP.get('/sale_in_footer/', {
                params: {
                    data: data
                }
            }).then(response => {
                data = response.data;
                context.commit('SET_SALE', data);
                return response.data
            })
        },
}
export default {
    state,
    getters,
    mutations,
    actions
}