<template>
      <v-lazy
        v-model="isActive"
        :options="{
          threshold: .3
        }"
        min-height="1000"
        transition="expand-x-transition"
      >
<div class="rew">
  <div class="mono_title  row">
    <v-flex class="r_title"
    md3
    xs12
    sm12
    offset-sm0
    offset-xs0
    offset-md1
    >
    <h2>Отзывы Клиентов</h2>
    <div class="sep-element"><iframe
  src="https://yandex.ru/sprav/widget/rating-badge/182308908187"
  width="150"
  height="50"
  frameborder="0"
></iframe>
</div>
    </v-flex>
 <v-flex md2 offset-md5 class="hidden-sm-and-down">
    <div class="rew_bottom">
      <v-btn depressed large color="#333"  href="https://yandex.ru/profile/182308908187?intent=reviews&lr=2">Оставить отзыв</v-btn>
    </div>
  </v-flex>

  </div>
  <div class="swiper-container">
<swiper class="swiper-wrapper" ref="swiper" :options="swiperOption">
    <swiper-slide class="swiper-slide "
          v-for="(item,i) in $store.getters.REVIEWS.filter(i => i.show_flag === true)" :key="i"
           ref="item"
          >
          <div class="rewItem" ref="rewItem">
        <h3>{{item.name_user}}</h3>
        <div class="text-center">
          <v-rating v-model=item.review_rate></v-rating>
          <div class="review">{{item.review}}</div>
        </div>
        <div class="pix-border-shadow-overlay"></div>
        </div>
        <div class="avatar">
          <img :src="item.user_photo_link" alt="">
        </div>
    </swiper-slide>
    <div class="swiper-pagination" slot="pagination"></div>

  </swiper>
  </div>
  <div>{{rew}}</div>

</div>
</v-lazy>

</template>

<script>
import 'swiper/dist/css/swiper.css'
import { swiper, swiperSlide } from 'vue-awesome-swiper'

export default {
  data () {
return{
  isActive: false,
  rew:'',
  //start slider param
        swiperOption: {
            breakpoints: {
            640: {
               slidesPerView: 1,
              spaceBetween: 30,
              slidesPerGroup: 1,
              },
            960: {
               slidesPerView: 2,
              spaceBetween: 30,
              slidesPerGroup: 2,
              }
            },
          slidesPerView: 3,
          spaceBetween: 30,
          slidesPerGroup: 3,
          loop: true,
          grabCursor: true,
          loopFillGroupWithBlank: true,
          pagination: {
            el: '.swiper-pagination',
            type: 'progressbar'
          },
        },
      }
            },
      components: {
            swiper,
            swiperSlide
    },
methods:{
      getDirection() {
            /* eslint-disable no-console */
                console.log("СТАРТ", this.$refs.rewItem);
            /* eslint-enable no-console */
        }
},
computed: {
},

  created () {
  },
  mounted(){
    this.$store.dispatch('GET_REVIEWS');
    this.getDirection();

  }
}
</script>


<style >
.rew{
  background-color: #f7f8f9;
  padding-top: 50px;
  padding-bottom: 50px;
}
.rew_bottom a{
  color:white !important;
  padding: 10px 20px 10px 20px !important;
  font-family: 'Roboto', sans-serif;
  font-weight: 600;
}
.rew_bottom{
  font-family: 'Fira Sans', sans-serif;
  font-weight: 600;
  font-size: 32px;
  padding-bottom: 20px;
  line-height: 45px;
  color: black;
  margin-top: 2.5em;
}
.mono_title{
  margin-bottom:50px;
}
.sep-element{
  padding-top: 20px;
  width: 40px;
  border-top: 4px solid;
  border-color: #2052c9;
}
.r_title h2{
  font-family: 'Fira Sans', sans-serif;
  font-weight: 600;
  font-size: 37px;
  padding-bottom: 20px;
  line-height: 45px;
  color: black;
  margin-top: 2em;
}
.avatar img{
  object-fit: cover;
}
.avatar{
  margin: auto;
  width: 75px;
  height: 75px;
  -webkit-border-radius: 150px;
  border-radius: 150px;
  overflow: hidden;
  -webkit-box-shadow: 0 0 30px rgba(0,0,0,.1);
  box-shadow: 0 0 30px rgba(0,0,0,.1);
}
.rewItem h3{
  text-align: center;
}
/* полоса прокрутки (скроллбар) */
.review::-webkit-scrollbar-track {
	-webkit-box-shadow: inset 0 0 6px rgba(0,0,0,0.3);
	background-color: #F5F5F5;
	border-radius: 10px;
}

/* ползунок скроллбара */
.review::-webkit-scrollbar {
	width: 10px;
	background-color: #F5F5F5;
}

.review::-webkit-scrollbar-thumb{
  border-radius: 10px;
  background-image: linear-gradient(to bottom, #e0e3ed, #a8b6f4, #7587f5, #4556ef,
#0711e1);
}

.review{
  height:300px;
  overflow-y: auto;
}
.swiper-container{
  width: 90% !important;
    }

.pix-border-shadow-overlay{
    position: absolute;
    width: 100%;
    height: 20px;
    bottom: 0;
    left: 0;
    background-color: #fff;
    z-index: 1;
}
.rewItem{
    position: relative;
    padding-top: 45px;
    padding-bottom: 45px;
    padding-left: 20px;
    padding-right: 20px;
    background: #fff;
    -webkit-box-shadow: 0 0 40px rgba(0,0,0,.15);
    box-shadow: 0 0 40px rgba(0,0,0,.15);
    margin-bottom: 50px;
    box-shadow: 0px 2px 10px 0px rgba(0,0,0,0.1), 0px 10px 20px 0px rgba(0,0,0,0.05)
    }
    .rewItem:after{
    content: "";
    position: absolute;
    width: 0;
    height: 0;
    margin-left: -1.5em;
    bottom: -2em;
    left: 50%;
    box-sizing: border-box;
    border: 1em solid #333;
    border-color: transparent transparent #fff #fff;
    transform-origin: 0 0;
    transform: rotate(-45deg);
    box-shadow: -3px 2px 10px 0 rgba(0,0,0,.1), -3px 10px 20px 0 rgba(0,0,0,.05);
    }
    .swiper-container {
      width: 100%;
      height: 100%;
    }
    .swiper-slide {
      font-size: 18px;


      /* Center slide text vertically */
      display: -webkit-block;
      display: -ms-block;
      display: -webkit-block;
      display: block;
      -webkit-box-pack: center;
      -ms-flex-pack: center;
      -webkit-justify-content: center;
      justify-content: center;
      -webkit-box-align: center;
      -ms-flex-align: center;
      -webkit-align-items: center;
      align-items: center;
    }
        @media (max-width: 960px) and (min-width: 640px) {
      .r_title h2{
        margin-top:25px !important;
      }
      .mono_title{
        padding: 0px 25px 0px 25px !important;
      }
      }
    @media (max-width: 640px) and (min-width: 320px)and (orientation:portrait) {
      .rew{
        margin-bottom: 0px;
      }
      .section-title{
      font-size: 1.6rem;
      margin-top: 15px;
      }
      .review{
        max-height: 300px;
        height: auto !important;
      }
      .r_title h2{
        font-size: 1.6rem !important;
        margin-top: 0px;
      }
        .mono_title{
          padding: 10px 20px 10px 20px;
        }
    }
</style>