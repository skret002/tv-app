import Vue from 'vue'
import App from './App.vue'
import vuetify from './plugins/vuetify'
import store from './store'
import router from './router'
import vueDebounce from 'vue-debounce'

Vue.config.productionTip = false

new Vue({
    vueDebounce,
    vuetify,
    store,
    router,

    render: (h) => h(App),
}).$mount('#app');
