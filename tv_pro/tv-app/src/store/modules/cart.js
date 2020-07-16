//import { HTTP } from '../../common'

const state = {
    totalPrice: 0,
    totalBy: null,
    cart: new Array,
}
const getters = {
    TOTALPRICE: state => {
        return state.totalPrice;
    },
    TOTALBY: state => {
        return state.totalBy;
    },
    CARTSTATE: state => {
        return state.cart;
    },
}
const mutations = {
    SET_TOTALPRICE: (state, payload) => {
        state.totalPrice = payload;
    },
    SET_TOTALBY: (state, payload) => {
        state.totalBy = payload;
    },
    SET_CARTSTATE: (state, payload) => {
        /* eslint-disable no-console */
        console.log("STORE SET", payload['data'])
            /* eslint-enable no-console */
        state.cart.push({
            'id': payload['data']['id'],
            'title': payload['data']['title'],
            'price': payload['data']['price']
        })
    },
}
const actions = {
    GET_CARTSTATE: async(context, data) => {
        context.commit('SET_CARTSTATE', data)
    },
}
export default {
    state,
    getters,
    mutations,
    actions
}