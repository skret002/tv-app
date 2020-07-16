import { HTTP } from '../../common'

const state = {
    brend: '',
    type_lcd: '',
    device: '',
    mulfunk_size: '',
}
const getters = {
    BREND: state => {
        return state.brend;
    },
    TYPE_LCD: state => {
        return state.type_lcd;
    },
    TYPE_SIZE: state => {
        return state.device;
    },
    MALFUNK_SIZE: state => {
        return state.mulfunk_size;
    },
}
const mutations = {
    SET_BREND: (state, payload) => {
        state.brend = payload;
    },
    SET_TYPELCD: (state, payload) => {
        state.type_lcd = payload;
    },
    SET_TYPE_SIZE: async(context, data) => {
        return HTTP.post('/price_size/', {
            params: {
                id: data
            }
        }).then(response => {
            data = response.data;
            state.device = data;
        })
    },
    SET_MALFUNK: async(context, data) => {
        return HTTP.post('/get_mulfunk/', {
            params: {
                data: data
            }
        }).then(response => {
            data = response.data;
            state.mulfunk_size = data;
        })
    },
}
const actions = {
    GET_BREND_PRICE: async(context, data) => {
        return HTTP.get('/price/').then(response => {
            data = response.data;
            context.commit('SET_BREND', data);
        })
    },
    GET_TYPE_LCD: async(context, data) => {
        return HTTP.get('/type_lcd/').then(response => {
            data = response.data;
            context.commit('SET_TYPELCD', data);
        })
    },
}
export default {
    state,
    getters,
    mutations,
    actions
}