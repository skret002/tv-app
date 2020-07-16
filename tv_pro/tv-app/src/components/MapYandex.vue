<template>
<v-container class="map_static" id="map">
    <v-flex md12 lg12
    xs10
    offset-xs1
    offset-md0
    offset-lg0
    >
<!--    <h2> Нас легко найти</h2> -->
<iframe
  :src="src"
  width="100%"
  height="500"
  frameborder="0"
  scroll=false
></iframe>
</v-flex>
</v-container>
</template>


<script>
export default {
data () {
  return{
    src:null
  }
  },
  methods:{
    async goMap(){
      this.src="https://yandex.ru/map-widget/v1/?z=12&ol=biz&oid=182308908187&scroll=false"
    }
  },
 mounted() {
   this.goMap();
  },
}
</script>

<style scoped>
.container{
     max-width: 100%;
     padding:20px 20px 20px 20px;
}
  .map_static h2{
    font-size: 2.4rem !important;
    margin-bottom: 20px !important;
    font-family: 'Fira Sans', sans-serif;
    font-weight: 600;
    text-align: center;
  }
  .map_static{
    margin-top: 50px !important;
  }
@media (max-width: 960px) and (min-width: 640px){
  .map_static h2{
    font-size: 2.4rem !important;
    margin-bottom: 20px !important;
  }
  .map_static{
    margin-top: 50px !important;
  }
}
    @media (max-width: 640px) and (min-width: 320px)and (orientation:portrait) {
      .map_static{
        max-height: 400px;
        overflow: hidden;
      }
    }
       @media (max-width: 640px) and (min-width: 320px){
      .map_static h2{
        font-size: 2rem !important;
      }
    }
</style>