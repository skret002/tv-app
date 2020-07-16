import {HTTP} from '../../common'
    const state = {
         home: '',
         malfunctions:'',
         about_in_home:'',
        about_order_block:'',
        reviews:"",

     }
    const getters = {
        REVIEWS: state => {
            return state.reviews;
        },
             HOME: state => {
                 return state.home;
             },
             MALFUNC: state =>{
                   return state.malfunctions;
             },
             ABOUT_IN_HOME: state =>{
                    return state.about_in_home;
             },
            ABOUT_ORDER_BLOCK: state =>{
                    return state.about_order_block;
             },
         }
      const mutations = {
          SET_REVIEWS: (state, payload) => {
              state.reviews = payload;
          },
             SET_HOME: (state, payload) => {
                 state.home = payload;
             },
            SET_MALFUNC: (state, payload1) => {
                state.malfunctions = payload1;
            },
            SET_ABOUT_IN_HOME: (state, payload) => {
                state.about_in_home = payload;
            },
            SET_ABOUT_ORDER_BLOCK: (state, payload) => {
                state.about_order_block = payload;
            },

         }
         const actions = {
             GET_REVIEWS: async (context, data) => {
                 return HTTP.get('/reviews/').then(response => {
                     data = response.data;
                     context.commit('SET_REVIEWS', data);
                 })
             },
             GET_HOME: async (context, data) => {
                 return HTTP.get('/home/').then(response => {
                     data = response.data;
                     context.commit('SET_HOME', data);
                 })
             },
             GET_MALFUNC: async  (context, data) => {
                 return HTTP.get('/malfunctions/').then(response => {
                     data = response.data;
                     context.commit('SET_MALFUNC', data);
                 })
             },
             GET_ABOUT_IN_HOME: async  (context, data) => {
                 return HTTP.get('/about_in_home/').then(response => {
                     data = response.data;
                     context.commit('SET_ABOUT_IN_HOME', data);
                 })
             },
             GET_ABOUT_ORDER_BLOCK: async  (context, data) => {
                 return HTTP.get('/about_order_block_in_home/').then(response => {
                     data = response.data;
                     context.commit('SET_ABOUT_ORDER_BLOCK', data);
                 })
             },
         }
export default {
    state,
    getters,
    mutations,
    actions
}