import Vue from 'vue'
import Vuex from 'vuex'
import home from './modules/home'
import price from './modules/price'
import order from './modules/order'
import footer from './modules/footer'


Vue.use(Vuex)
export default new Vuex.Store({
    state: {},
    getters: {},
    mutations: {},
    actions: {},
    modules: {
        home,
        price,
        order,
        footer,
    }
})