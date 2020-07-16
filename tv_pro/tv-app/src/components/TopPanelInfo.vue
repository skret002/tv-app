<template>
<v-container fluid style="margin: 0px; padding: 0px; width: 100%" class="top_panel_info" id="topPanel" >
    <div class="page-wrap" v-if="hamburgerShowHidden">
        <v-row  >
            <v-col cols="2">
                <Bubble  >
                    <ul>
                        <li>
                         <router-link class="v-btn " :to="{name:'home'}">
                            <v-btn text class="line_transform_btn"><i id="home_icon" class="material-icons">home</i> Home</v-btn>
                        </router-link>
                        </li>
                        <li>
                        <router-link  v-if="$route.name!='staff'" class="v-btn" :to="{name:'staff', params:{ 'id':'about_company'}}">
                            <v-btn text class="line_transform_btn">
                                    О сервисе
                            </v-btn>
                         </router-link>
                             <a class="v-btn  router-link-active" v-else  @click="lazyScroll('about_company')">
                                <v-btn text class="line_transform_btn">
                                        О сервисе
                                </v-btn>
                            </a>
                         </li>
                        <li>
                        <a  v-if="$route.name== 'home'" class="v-btn  router-link-active"   @click="lazyScroll('price')">
                            <v-btn text class="line_transform_btn">Услуги & Цены</v-btn>
                        </a>
                        <router-link  v-else class="v-btn" :to="{name:'home', params:{ 'id':'price'}}">
                                <v-btn text class="line_transform_btn">Услуги & Цены</v-btn>
                        </router-link>
                        </li>
                        <li>
                            <router-link v-if="$route.name!='staff'" class="v-btn" :to="{name:'staff', params:{ 'id':'staff'}}">
                                <v-btn text class="line_transform_btn"> Наша команда </v-btn>
                            </router-link>
                            <a class="v-btn  router-link-active" v-else @click="lazyScroll('staff')">
                                <v-btn text class="line_transform_btn"> Наша команда </v-btn>
                            </a>
                        </li>
                        <li>
                        <router-link  class="v-btn" :to="{name:'portfolio'}">
                                <v-btn text class="line_transform_btn"
                                     v-if="oldELShowInFloatPanel===true">Фото</v-btn>
                        </router-link>
                        <li>
                        <router-link  class="v-btn" :to="{name:'shop'}">
                            <v-btn text class="line_transform_btn"
                                    v-if="oldELShowInFloatPanel === true">
                                    Магазин
                            </v-btn>
                        </router-link>
                        </li>
                        <li>
                        <a class="v-btn  router-link-active" @click="lazyScroll('map')">
                        <v-btn text class="line_transform_btn">Контакты</v-btn>
                        </a>
                        </li>
         </ul>
                </Bubble>
            </v-col>
            <v-col cols="10" class="smoll_head">
                <nav class="nav-head">
                    <ul>
                        <li>
                            <div class="nav-info">
                                <v-icon class="ic-s">phone_callback</v-icon>
                                <span>Тел:</span>
                                <h4>{{ $store.getters.HOME[0].phone}}</h4>
                                </div>
                        </li>
                        <li>
                                <div class="nav-info">
                                    <i class="material-icons ic-s">near_me</i>
                                    <span>Адрес</span>
                                    <h4>{{ $store.getters.HOME[0].adress}}</h4>
                                </div>
                        </li>
                            <li class="hidden540">
                                <div class="nav-info">
                                    <i class="material-icons ic-s">access_time</i>
                                        <span>График работы</span>
                                    <h4>{{ $store.getters.HOME[0].time_work}}</h4>
                                </div>
                            </li>
                             <li class="hidden690">
                                    <div class="nav-info">
                                            <i class="material-icons ic-s">email</i>
                                                <span>{{ $store.getters.HOME[0].email}}</span>
                                            <h4><a href="mailto:info@domain.com">{{ $store.getters.HOME[0].email}}</a></h4>
                                    </div>
                             </li>
                    </ul>
                    </nav>
            </v-col>
        </v-row>
    </div>
  <v-row class="top-row" v-if=showTopInfo>
      <v-col class="d-sm-none d-lg-flex"  cols="3"
      md="2"
        >
        <div class="menu-logo">
            <a class="navbar-brand scroll" :href="host" style="width:146px;">
            <img class="normal-logo" src="../assets/variant_1.png" alt="Logo">
             </a>
        </div>
      </v-col>
     <v-col  cols="9"
     md="10"
     sm="12" >
<nav class="nav-head">
<ul>
    <li>
        <div class="nav-info">
            <i class="material-icons ic-s">email</i>
            <span>Email</span>
            <h4><a :href="'mailto:' + $store.getters.HOME[0].email">{{ $store.getters.HOME[0].email}}</a></h4>
            </div>
    </li>
    <li>
        <div class="nav-info">
            <v-icon class="ic-s">phone_callback</v-icon>
            <span>Тел:</span>
            <h4>{{ $store.getters.HOME[0].phone}}</h4>
            </div>
    </li>
    <li>
        <div class="nav-info">
            <i class="material-icons ic-s">access_time</i>
            <span>График работы</span>
            <h4>{{ $store.getters.HOME[0].time_work}}</h4>
            </div>
    </li>
    <li>
            <div class="nav-info">
                <i class="material-icons ic-s">near_me</i>
                <span>Адрес</span>
                <h4>{{ $store.getters.HOME[0].adress}}</h4>
            </div>
    </li>
</ul>
</nav>
      </v-col>
  </v-row>
 <!-- <v-row v-else> -->


  <!--                                                                                                                            -->
  <v-row class="top-row"
  ref="topRow"
   v-if=showTopInfo>
      <v-col cols="12">
            <div>
        <v-app-bar
                id="float_panel"
                ref="float_panel"
                color="#2052c9"
                dark
                style="border-radius: 6px"
                :style="{'background-color':floatTopPanel[0].backgroundColor , 'height':floatTopPanel[0].vToolbarContentHight}"
            >
     <v-toolbar-items
     style="margin: auto"
     >
     <router-link class="v-btn " :to="{name:'home'}">
        <v-btn text class="line_transform_btn"><i id="home_icon" class="material-icons">home</i> Home</v-btn>
     </router-link>

    <router-link  v-if="$route.name!='staff'" class="v-btn" :to="{name:'staff', params:{ 'id':'about_company'}}">
        <v-btn text class="line_transform_btn">
                О сервисе
        </v-btn>
        </router-link>
    <a class="v-btn  router-link-active" v-else  @click="lazyScroll('about_company')">
        <v-btn text class="line_transform_btn">
                О сервисе
        </v-btn>
    </a>
     <a  v-if="$route.name== 'home'" class="v-btn  router-link-active"   @click="lazyScroll('price')">
        <v-btn text class="line_transform_btn">Услуги & Цены</v-btn>
     </a>
       <router-link  v-else class="v-btn" :to="{name:'home', params:{ 'id':'price'}}">
            <v-btn text class="line_transform_btn">Услуги & Цены</v-btn>
        </router-link>

    <router-link v-if="$route.name!='staff'" class="v-btn" :to="{name:'staff', params:{ 'id':'staff'}}">
        <v-btn text class="line_transform_btn"> Наша команда </v-btn>
    </router-link>
        <a class="v-btn  router-link-active" v-else @click="lazyScroll('staff')">
            <v-btn text class="line_transform_btn"> Наша команда </v-btn>
        </a>
    <router-link  class="v-btn" :to="{name:'portfolio'}">
        <v-btn text class="line_transform_btn"
                v-if="oldELShowInFloatPanel===true">Фото</v-btn>
    </router-link>
    <router-link  class="v-btn"  :to="{ name: 'shop' }">
        <v-btn text class="line_transform_btn"
                v-if="oldELShowInFloatPanel === true">
                Магазин
        </v-btn>
        </router-link>
        <a class="v-btn  router-link-active" @click="lazyScroll('map')">
        <v-btn text class="line_transform_btn">Контакты</v-btn>
        </a>
        <router-link v-if="$route.name!='home'" class="v-btn" :to="{name:'home', params:{ 'id':'order'}}">
            <v-btn class="line_transform_btn call_to_action"
            v-if="orderBottom === true"
            style="border-radius: 5px;height:70% !important;"
            >Заказать ремонт
            </v-btn>
         </router-link>
         <a class="v-btn  router-link-active" v-else @click="lazyScroll('order')">
            <v-btn class="line_transform_btn call_to_action"
            v-if="orderBottom === true"
            style="border-radius: 5px;height:70% !important;"
            >Заказать ремонт
            </v-btn>
         </a>
                    </v-toolbar-items>
                </v-app-bar>
            </div>
      </v-col>
  </v-row>
</v-container>

</template>

<script>
import { Bubble } from 'vue-burger-menu'
export default {
     data () {
      return {
        host:window.location.hostname,
        elOld:null,
        orderBottom:false,
        pageYOffsetOld: 0,
        newELShowInFloatPanel:false,
         oldELShowInFloatPanel: true,
        floatTopPanel: [{
           backgroundColor: ' rgb(32, 82, 201)',
           borderColor: 'rgb(32, 82, 201)',
           vToolbarContentHight: '75 px',
        }],
         showTopInfo:Boolean,
         hamburgerShowHidden:Boolean,
      }},
components: {
        Bubble // Register your component
    },
  methods: {
      lazyScroll: function(el){
          document.getElementById(el).scrollIntoView({block: "start", behavior: "smooth"});
      },
    scrollToBlock(){
        var el = this.$route.params.id;
            try {
            document.getElementById(el).scrollIntoView({block: "center", behavior: "smooth"});
            }catch{
              setTimeout(() =>this.scrollToBlock(), 200);
            }
        },
      setterPanel: function(){
          if(pageYOffset>250){
              this.$refs.float_panel.$el.classList.add('float_panel');
              this.floatTopPanel[0].backgroundColor = 'rgba(0,0,0,.75)';
              this.floatTopPanel[0].vToolbarContentHight='50px';
              document.getElementsByClassName("v-toolbar__content")[0].style.height = '50px';
              this.newELShowInFloatPanel=true;
              this.oldELShowInFloatPanel= false;
          }
            else{
                if(window.innerWidth<960){
                    this.floatTopPanel[0].backgroundColor = 'rgb(32, 82, 201)';
                    this.floatTopPanel[0].vToolbarContentHight='50px';
                    document.getElementsByClassName("v-toolbar__content")[0].style.height = '50px';
                    this.newELShowInFloatPanel=false;
                    this.oldELShowInFloatPanel= true;
                }
                else{
                    this.floatTopPanel[0].backgroundColor = 'rgb(32, 82, 201)';
                    this.floatTopPanel[0].vToolbarContentHight='75px';
                    document.getElementsByClassName("v-toolbar__content")[0].style.height = '64px'
                    this.newELShowInFloatPanel=false;
                    this.oldELShowInFloatPanel= true;
                }
          }
      },
      getScroll: function (){
            var top = window.pageYOffset;
            if (this.pageYOffsetOld > top) {
                this.setterPanel();
                var elem = document.querySelector("#float_panel")
                elem.classList.remove("float_panel")
                this.orderBottom = false;
            }
            else if (this.pageYOffsetOld < top) {
                if(window.innerWidth>960){
                    this.orderBottom = true;
                    }
                this.setterPanel();
            }
            this.pageYOffsetOld = top;
        },
    getWidthPage: function () {

        if(window.screen.width>736){
            this.showTopInfo=true,
             this.hamburgerShowHidden=false
        }else{
            this.showTopInfo=false,
            this.hamburgerShowHidden=true
        }},
        onScroll:function () {
            this.floatTopPanel[0].onScrollOn='true'
        }
  },
      created() {
          window.addEventListener('resize', this.getWidthPage);
          this.getWidthPage();
          window.addEventListener('scroll', this.getScroll)
},
      beforeDestroy() {
          window.removeEventListener('resize', this.getWidthPage);
},
mounted(){
    this.$store.dispatch('GET_HOME'),
   this.$store.dispatch('GET_MALFUNC');
   this.scrollToBlock();
}

}
</script>

<style scoped>
.bm-item-list>ul>li>a>button{
    color: white;
}
.bm-item-list>ul>li{
    width: 100%;
    margin-bottom: 10px;
}
  /*float panel */
  .call_to_action{
     border-radius: 5px;
    height: 35px !important;
    background-color: #2052c9 !important;
    margin-top: 0.3em;
    margin-bottom: 0.3em;
    margin-left: 1%;
  }

.float_panel{
    height: 50px !important;
    transform: none;
    position: fixed;
    top: 0;
    width: 80%;
    margin-left: 10%;
    margin-right: 10%;
    border-radius: 0 0 5px 5px;
    background-color: rgba(0,0,0,.75);
    visibility: visible;
    transition: 300ms;
}
 .bm-burger-button >span {
    background-color: rgb(32, 82, 201) !important;
}
.top-row{
    padding: 0 5%;
}
.top_panel_info{
    position: absolute;
    top: 0;
    color: white;
    z-index: 200;
}
.nav-head{
    text-align: right;
}
ul{
    display: inline-block;
    height: 100%;
}
ul>li{
    display: inline-block;
    position: relative;
    font-size: 18px;
    font-weight: 700;
    padding-left: 30px;
    font-family: 'Roboto', sans-serif;
}
li>a , h4>a{
     text-decoration: blink;
     color:white;
}
.nav-info{
    position: relative;
    height: 50px;
    top: calc(50% - 25px);
}
.nav-info > span{
   color: #ccc;
   font-weight: 400;
   font-size: 16px;
   font-family: 'Roboto', sans-serif;
}
.ic-s{
    padding-right: 10px;
    color: #2052c9!important;
    font-size: 22px;
    vertical-align: text-bottom;
}
.menu-logo{
    text-align: center;
    height: 100%;
    padding-left: 0;
}
.menu-logo a{
    position: relative;
    display: block;
    height: 100%;
    line-height: 15px;
}
.menu-logo img{
    width: 75%;
    height: auto;
    position: absolute;
    top: 0;
    bottom: 0;
    left: 0;
    right: 0;

}
.line_transform_btn{
    display: inline-block;
    color:white;
    line-height: 1;
    text-decoration:none;
    cursor: pointer;
    position:relative;
    font-family: 'Roboto', sans-serif;
    font-weight: 600;
    font-size: 14px;
    padding: 0px 10px 0 10px;

}
.line_transform_btn:after {
    background-color: white;
    display: block;
    content: "";
    height: 2px;
    width: 0%;
    left:50%;
    position:absolute;
    -webkit-transition: width .5s ease-in-out;
    -moz--transition: width .5s ease-in-out;
    transition: width .5s ease-in-out;
    -webkit-transform:translateX(-50%);
    -moz-transform:translateX(-50%);
    transform:translateX(-50%);
}
.line_transform_btn:hover:after,
.line_transform_btn:focus:after {
    width: 100%;
}
#home_icon{
    margin: -5px 5px 0px 0;
}
 @media (max-width: 1150px) and (min-width: 980px) {
ul>li{
    display: inline-block;
    position: relative;
    font-size: 16px;
    font-weight: 700;
    padding-left: 30px;
    font-family: 'Roboto', sans-serif;
}
.line_transform_btn{
   padding: 0px 10px 0px 10px !important;
}
 }
  @media (max-width: 980px) and (min-width: 736px) {
      .nav-head{
          text-align: center;
      }
ul>li{
    display: inline-block;
    position: relative;
    font-size: 16px;
    font-weight: 700;
    padding-left: 25px;
    font-family: 'Roboto', sans-serif;
}
.nav-head >ul>li:first-child{
    padding-left: 0px !important;;
    }
.line_transform_btn{
    padding: 0px 5px 0px 5px !important;
    font-size: 12px !important;
}
 }
   @media (max-width: 736px) and (min-width: 320px) {
       .nav-head >ul>li:first-child{
        padding-left: 5px !important;;
    }
      .nav-head{
        top: 26px;
        position: absolute;
 }
    ul>li{
        font-size: 14px;
        padding-left: 15px;
    }

   }
      @media (max-width: 360px) and (min-width: 320px) {
        ul>li{
            font-size: 13px;
        }
      }
        @media (max-width: 540px) and (min-width: 320px) {
           .hidden540{
               display: none;
           }
      }
        @media (max-width: 690px) and (min-width: 320px) {
           .hidden690{
               display: none;
           }
      }

</style>