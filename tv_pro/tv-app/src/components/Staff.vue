<template>
<div>
<v-flex class="staff" id="staff"
lg10 xl10 md10 sm10 xs10
offset-lg1 offset-xl1 offset-md1 offset-sm1 offset-xs1
>
<v-row>
    <v-flex class="item_staff" v-for="(item,i) in staff" :key="i" md4 >
          <v-card dark style="height: 400px; overflow-y: auto;"
          >
            <div class="d-flex flex-no-wrap justify-space-between">
              <div>
                <v-card-title
                  class="headline"
                  v-text="item.name"
                ></v-card-title>

                <v-card-subtitle v-text="'Должность: ' +item.position"></v-card-subtitle>
              </div>
              <v-avatar
                class="ma-3"
                size="125"
                tile
              >
                <v-img :src=" 'http://localhost:8000'+item.avatar"></v-img>
              </v-avatar>

            </div>
            <v-card-text v-html="item.text"></v-card-text>
          </v-card>
    </v-flex>
</v-row>
</v-flex>
<v-flex class="about_company" id="about_company"
lg6 xl6 md8 sm10 xs10
offset-lg3 offset-xl3 offset-md2 offset-sm1 offset-xs1
>
<div id="player-overlay" v-if="staff[0].video.video">
  <video controls>
    <source :src="'http://localhost:8000' +staff[0].video.video" type="video/webm">
  </video>
</div>
<div class="not_video" v-else id="about_company">
    <h1>Видео еще не загружено, но мы над этим работаем!</h1>
</div>
</v-flex>
</div>

</template>

<script>
import { HTTP } from '../common'

export default {
data(){
    return{
      staff:null,
    }
},
methods:{
    scrollToBlock(){
            var el = this.$route.params.id;
            try {
            document.getElementById(el).scrollIntoView({block: "center", behavior: "smooth"});
            }catch{
              setTimeout(() =>this.scrollToBlock(), 200);
            }
            },
    getStaff(){
        HTTP.get('/staff/').then(response => {
            this.staff = response.data;
        })
    },
  afteRenderUpdate(){
    let topPanel = document.getElementById('topPanel');
    if (window.screen.width> 736){
    let floatPanel = document.getElementById('float_panel');
    if(topPanel){
        topPanel.style.backgroundColor='black';
        topPanel.style.position='static'
        floatPanel.style.marginBottom = '50px';
        this.getStaff();
        setTimeout(() =>this.scrollToBlock(), 300);
    }else{
      setTimeout(() =>this.afteRenderUpdate(), 100);
    }
    }else if(window.screen.width<= 736 && topPanel){
        topPanel.style.backgroundColor='black';
        topPanel.style.position='static'
        topPanel.style.height = '100px';
        document.getElementById('body').scrollIntoView({behavior: "smooth"});
        this.getStaff();
    }else{
      setTimeout(() =>this.afteRenderUpdate(), 100);
    }
}},
created: function (){
  this.afteRenderUpdate();
},

}
</script>

<style scoped>
.v-card__subtitle{
  width: max-content;
}
.not_video{
    background-color: #424242;
    border-radius: 6px;
    text-align: center;
    padding: 30px;
    color: white;
    margin-top: 100px;
    margin-bottom: 150px;
}
.not_video h1{
    font-family: 'Roboto', sans-serif;
    font-weight: 600;

}
video{
    max-width: 100%;
    height: auto;
    margin-top: 100px;
    margin-bottom: 150px;
}
.card__subtitle{
    line-height: 1.6rem !important;
    font-family: Roboto,sans-serif !important;
}
.item_staff{
    padding:30px 15px 15px 15px;
}
#article{
  margin-top:25px;
  margin-bottom: 25px;
}
.v-card__title{
  text-align: center;
  font-family: 'Roboto', sans-serif;
  font-size: 1.8rem;
  margin:15px;
  word-break: break-word;
}
.v-card__text{
  font-family: 'Roboto', sans-serif;
  font-size: 1.1rem;
}
.btn_article{
   margin-bottom: 25px;
}
.btn_article a{
  text-decoration: none;
  font-family: 'Roboto', sans-serif;
}
@media (max-width: 736px){

}


</style>