<template>
  <div>
    <v-flex
      class="portfolio"
      id="portfolio"
      lg10 xl10 md10   sm10 xs10
      offset-lg1 offset-xl1 offset-md1 offset-sm1 offset-xs1
    >
    <div class="life_sc"><h2>Из жизни сервисного центра</h2></div>
      <v-row v-if="notItem">
            <v-flex class="media" v-for="(item, i) in media" :key="i" md4>
              <v-card>
                <v-img
                  :src="'http://localhost:8000'+item.prew_img"
                  class="white--text align-end"
                  gradient="to bottom, rgba(0,0,0,.1), rgba(0,0,0,.5)"
                  height="200px"
                >
                  <v-card-title v-text="item.title"></v-card-title>
                </v-img>
                <v-card-actions>
                  <v-spacer></v-spacer>
                 <v-btn  v-on:click="setModal(item.id, item.prew_img)" class="ma-2" outlined color="#2052c9">подробнее</v-btn>
                </v-card-actions>
          </v-card>
            </v-flex>
      </v-row>
      <div class="text-center not_media" v-else><h2>Пока больше нет! Зайдите к нам позже.</h2></div>
      <div class="text-center bottom">
              <v-btn rounded color="primary" dark v-if="notItem"  @click="getMedia()">Загрузить еще</v-btn>
              <v-btn rounded color="primary" dark v-else @click="restartMedia()">Показать сначала</v-btn>
            </div>

    </v-flex>
  <div class="modal">
    <v-row justify="center">
    <v-dialog v-model="dialog" fullscreen hide-overlay transition="dialog-bottom-transition">
      <v-card class="stor_cart">
        <v-toolbar dark color="primary">
          <v-btn style="position: absolute;right: 0;" icon dark @click="dialog = false, dopmedia=[], dopcontent=[]">
            <v-icon>mdi-close</v-icon>
          </v-btn>
          <v-spacer></v-spacer>
        </v-toolbar>
           <v-flex id="carusel"
              lg8 xl8 md10   sm10 xs10
              offset-lg2 offset-xl2 offset-md1 offset-sm1 offset-xs1
            >
        <v-carousel
        :height="carHeight"
        >
            <v-carousel-item
              v-for="(item,i) in dopmedia"
              :key="i"
              reverse-transition="fade-transition"
              transition="fade-transition"
            >
            <div class="item" :style="{'background-image':'url('+'http://localhost:8000'+item.path+')'}"></div>
            </v-carousel-item>
          </v-carousel>
          <div class="content" v-if="dopcontent[0]">
              <v-card-title v-text="dopcontent[0]['title']"></v-card-title>
              <v-card-text v-html="dopcontent[1]['content']"></v-card-text>
          </div>
           </v-flex>

      </v-card>
    </v-dialog>
  </v-row>

  </div>
  </div>
</template>

<script>
import { HTTP } from '../common'

export default {
  data () {
    return {
      carHeight:500,
      notItem:true,
      start:0,
      end:9,
      dopcontent:[],
      dopmedia:[],
      dialog: false,
      notifications: false,
      sound: true,
      widgets: false,
      media: null
    }
  },
  methods: {
    restartMedia(){
    this.start=0;
    this.end=9;
    this.getMedia();
    this.notItem=true;
    },
    setModal(id,f_img){
      if (window.screen.width<960){
        this.carHeight=250;
      }
      this.dialog = true;
     HTTP.post('/portfolio_img/',
     {params: {data:[{"id":id}]}}).then(response => {
        this.dopcontent.push({'title':response.data[0]['portfolio']['title']})
        this.dopcontent.push({'content':response.data[0]['portfolio']['content']})
       for(var i  in response.data){
          this.dopmedia.push({'path':response.data[i]["img"]})
       }
      })
        this.dopmedia.push({'path':f_img})
    },
    scrollToBlock () {
      var el = this.$route.params.id
      document.getElementById(el).scrollIntoView()
    },
    getMedia () {
      HTTP.post('/portfolio/',
     {params: {data:[{"start":this.start,"end":this.end}]}}).then(response => {
        if(response.data.length==0){
          this.notItem = false;
        }else{
        this.media = response.data
        }
      })
      this.start = this.start +9;
      this.end = this.end +9;
    },
     afteRenderUpdate () {
      let topPanel = document.getElementById('topPanel')
      if (window.screen.width > 736) {
        let floatPanel = document.getElementById('float_panel')
        if (topPanel) {
          topPanel.style.backgroundColor = 'black'
          topPanel.style.position = 'static'
          floatPanel.style.marginBottom = '50px'
        } else {
          setTimeout(() => this.afteRenderUpdate(), 100)
        }
      } else if (window.screen.width <= 736 && topPanel) {
        topPanel.style.backgroundColor = 'black'
        topPanel.style.position = 'static'
        topPanel.style.height = '100px'
        document.getElementById('body').scrollIntoView()
        this.getMedia()
      } else {
        setTimeout(() => this.afteRenderUpdate(), 100)
      }
    }
  },
  created: function () {
    this.afteRenderUpdate()
    this.getMedia();
  }
}
</script>

<style scoped>
.item {
   background-size: contain !important;
   width: 100%;
   height: 100%;
   background-position: center;
   background-repeat: no-repeat;
}
#carusel{
  margin-top:50px;
}
.bottom{
  margin-top:50px;
  margin-bottom: 100px;
}
.not_media{
  margin-top:100px;
  text-align: center;
  font-size: 1.8rem;
}
  .portfolio{
    margin-top: 30px;
  }
  .media{
    padding: 20px;
  }
  .life_sc {
    text-align: center;
    margin-top:50px;
    margin-bottom: 30px;
  }
  .life_sc h2{
    font-family: 'Roboto', sans-serif;
    font-size: 2rem;
  }
@media (max-width: 736px) {
}
</style>
