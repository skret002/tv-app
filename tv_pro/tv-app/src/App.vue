<template>
  <v-app>
      <TopPanelInfo v-if="defer(2)"/>
      <transition name="moveInUp">
      <router-view v-if="defer(2)"></router-view>
      </transition>
      <Reviews v-if="$route.name!='shop' && defer(4)"/>
      <ContactForm v-if="$route.name!='shop' && defer(5)"/>
      <Map v-if="defer(6)"/>
      <Footer v-if="defer(7)"/>

  </v-app>

</template>

<script>
import Defer from './components/mixins/Defer'
import TopPanelInfo from './components/TopPanelInfo';
export default {
  name: 'App',
  mixins: [ Defer() ],
  data(){
    return{

    }},
methods: {
},

  components: {
        TopPanelInfo,
       Reviews: () => import('./components/Reviews'),
       ContactForm: () => import('./components/ContactForm'),
       Map: () => import('./components/MapYandex'),
       Footer: () => import('./components/Footer'),
  },
};
</script>
<style scoped>
body{
  overflow: hidden !important;
}
.moveInUp-enter-active{
    animation: fadeIn 1.5s ease-in;
}
@keyframes fadeIn{
    0%{
        opacity: 0;
    }
    50%{
        opacity: 0.5;
    }
    100%{
        opacity: 1;
    }
}
</style>