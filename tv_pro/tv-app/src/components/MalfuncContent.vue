<template>
<div>
<v-flex class="post_mulfunk" id="article"
lg8 xl8 md10 sm10 xs10
offset-lg2 offset-xl2 offset-md1 offset-sm1 offset-xs1
>
<v-card>
<v-card-title v-html="post.title"></v-card-title>
<v-card-text v-html="post.content"></v-card-text>
<v-flex lg6 xl6 md10 sm10 xs10
offset-lg3 offset-xl3 offset-md1 offset-sm1 offset-xs1>
<v-row >
<div class="text-center btn_article">
  <router-link :to="{name:'home', params:{ 'id':'price'}}">
    <v-btn class="ma-2" outlined color="#2052c9">посмотреть прайс</v-btn>
  </router-link>
     <v-btn class="ma-2" outlined color="#2052c9"
     v-on:click="scrollToSale()"
     >посмотреть акции</v-btn>
</div>
</v-row>
</v-flex>
</v-card>
</v-flex>
</div>

</template>

<script>

export default {
data(){
    return{
      post:null,
    }
},
methods:{
  scrollToSale(){
      document.getElementById('sale').scrollIntoView();
  },
  afteRenderUpdate(){
    var postId  = this.$route.params.id;
    let topPanel = document.getElementById('topPanel');
    if (window.screen.width> 736){
    let floatPanel = document.getElementById('float_panel');
    if(topPanel){
        topPanel.style.backgroundColor='black';
        topPanel.style.position='static'
        floatPanel.style.marginBottom = '50px';
        this.post = this.$store.getters.MALFUNC[postId].link;
        this.$nextTick(() => document.getElementById('article').scrollIntoView());
    }else{
      setTimeout(() =>this.afteRenderUpdate(), 100);
    }
    }else if(window.screen.width<= 736 && topPanel){
        topPanel.style.backgroundColor='black';
        topPanel.style.position='static'
        topPanel.style.height = '100px';
        this.post = this.$store.getters.MALFUNC[postId].link;
        document.getElementById('body').scrollIntoView();
    }else{
      setTimeout(() =>this.afteRenderUpdate(), 100);
    }
}},
created: function (){
  this.afteRenderUpdate();
},
}
</script>

<style>
#article{
  margin-top:25px;
  margin-bottom: 25px;
}
.v-card__title{
  text-align: center;
  font-family: 'Roboto', sans-serif;
  font-size: 1.8rem;
  margin:15px;
}
.v-card__text{
  font-family: 'Roboto', sans-serif;
  font-size: 1.1rem;
  line-height: 1.4;
}
.btn_article{
   margin-bottom: 25px;
}
.btn_article a{
  text-decoration: none;
  font-family: 'Roboto', sans-serif;
}
@media (max-width: 736px){
  .v-card__text img{
    margin-left: auto !important;
    margin-right: auto !important;
    float: none !important;
    max-width: 90% !important;
    height: auto !important;
  }
  .card__text{
    font-size: 1.1rem;
  }
  .v-card__title{
  font-size: 1.6rem;
}

}
</style>