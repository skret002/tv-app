<template>
<div>
  <div id="modal-container" class="out" v-on:click="closePopUp">
  <div class="modal-background">
    <div>
           <video
              sv-on:click="closePopUp"
              id="video1"
              :src="video_1"
              width="70%"  height="70%" controls autobuffer autoplay>
            </video>
    </div>
  </div>
</div>
<div id="main-slider" ref="mainSlider">
  <carousel  class="slider_head" v-if="showSlider===true"
  :autoplay="true" :nav="false"   :items=1  smartSpeed="2000"
  :autoWidth="false"  :autoplayTimeout="15000"  :dots="false"
   :style="{'height':slideHeight}"
  >
  <div  v-for="(item,i) in $store.getters.HOME[0]['slider']" :key="i" class="item"
  >
    <img class="slid_img animated zoomIn infinite delay-8s"
      :style="{'height':slideContentHeight}"
      style="max-width:auto"
      :src="item.image"
      >
      <h3 class="slide-caption animated infinite fadeInUp" v-html="item.slaid_title"></h3>
      <span class="slide-text animated infinite fadeInUp"
       :style="{'bottom' : bottomSlaidBtn, 'max-width': slaidTextW}">
        <div class="slaider_html" v-html="item.content"></div>
             <v-row class=" row_slaid_btn lg-12 md-12 xs-12 xl-12 sm-12"  justify="start" no-gutters>
                     <v-col lg="5" >
                          <v-btn @click="lazyScroll('price')" class="slaid_btn" id="slaid_btn_l" xs="12" >Больше информации</v-btn>
                     </v-col>
                       <v-col lg="5" xs="4" offset-lg="1" offset-md="1"  offset-sm="1" offset-xs="1">
                      <router-link   class="v-btn" :to="{name:'staff', params:{ 'id':'about_company'}}">
                         <v-btn class="slaid_btn" id="slaid_btn_r" cols="5">О  сервисе</v-btn>
                      </router-link>
                     </v-col>
      </v-row>
       </span>
  </div>

</carousel>
</div>
<div  id="malfunk">
<v-row class="row_in_center">
  <v-col cols="12"
                xl="3"
                lg="4"
               md="6"
                sm="12"
                xs="12"
                class="block_malfunk"
    v-for="(item,index)  in $store.getters.MALFUNC" :key="index"
    >
    <router-link :to="{name:'malfunc', params: {id:index}}">
      <v-card
          :loading="loading"
          class="mx-auto my-12 m-card">
            <div>
              <v-row>
                <div class="card_round hidden_round">
                    <v-img
                    id="img_round"
                      :src="item.icon"
                    ></v-img>
                  </div>
                  <v-card-title class="card-title-malf">{{item.title}}</v-card-title>
              </v-row>
              </div>

            <v-card-text  class="card-text-malf" style="font-family: 'Open Sans', Arial, sans-serif; font-size: 14px; text-align: justify;"
            v-html="item.content" >
            </v-card-text>
            <v-card-actions>
               <v-btn class="ma-2" outlined color="indigo"
               style=" position: absolute; bottom: 0px; right: 0;"
               >подробнее</v-btn>
            </v-card-actions>
        </v-card>
        </router-link>
  </v-col>
</v-row>
</div>
<div>
    <v-row no-gutter id="aih" class="gt30">
      <v-col
       xl="5" lg="5" md="10" sm="10" xs="10"
       offset="1"
        class="content_in_block_about_in_home "
        >
       <div class="title_about">
         <p> {{this.$store.getters.ABOUT_IN_HOME[0].title}}</p>
         </div>
         <div class="sep-element"></div>
         <div class="about_content"
         v-html="this.$store.getters.ABOUT_IN_HOME[0].content"
         >
         </div>
         <div class="button_left">
           <router-link   class="v-btn" :to="{name:'staff', params:{ 'id':'about_company'}}">
               <v-btn class="line_transform_btn call_to_action"
                  style="border-radius: 5px;"
              >
              <p class="call_to_action_p">О сервисе</p></v-btn>
           </router-link>

         </div>
      </v-col>
        <v-col class="img_in_block_about_in_home hidden-md-and-down"
        cols="5"
        :style="{'background-image':'url'+'('+this.$store.getters.ABOUT_IN_HOME[0].image+')'}"
        >
      </v-col>
    </v-row>
    <v-row no-gutter id="aih" style="background-color: #1e1e1e;">
       <v-col  class="time_line_wrap hidden-md-and-down"
        cols="6">
            <div>
      <v-timeline>
          <v-timeline-item
            color="red lighten-2"
            large
          >
            <v-card class="elevation-2">
              <v-card-title class="headline">Бесплатно!</v-card-title>
              <v-card-text>
               Диагнстику - мы всегда выполняем бесплатно, даже если в случае отказа от ремонта. Таким образом,
               если масштаб бедствий оказался слишком велик, вам это ни чего не будет стоить.
              </v-card-text>
            </v-card>
          </v-timeline-item>
          <v-timeline-item
            color="blue lighten-2"
            large
          >
            <v-card class="elevation-2">
              <v-card-title class="headline">Быстро!</v-card-title>
              <v-card-text>
               Для диагностики нам обычно достаточно одних суток, при очень сложных поломках может потреботься до трех суток.
               Ремонт выполняется в такие же сроки после диагностики.
              </v-card-text>
            </v-card>
          </v-timeline-item>
          <v-timeline-item
            color="yellow lighten-2"
            large
          >
            <v-card class="elevation-2">
              <v-card-title class="headline">Гарантия!</v-card-title>
              <v-card-text>
               Мы отвечаем за свои услуги по полной! Гарантия состовляет 90 дней на любой ремонт.
              </v-card-text>
            </v-card>
          </v-timeline-item>
          <v-timeline-item
            color="pink lighten-2"
            large
          >
            <v-card class="elevation-2">
              <v-card-title class="headline">Цена</v-card-title>
              <v-card-text>
              Мы обладаем одним из самых конкурентных прайс листов. Цена озвучивается один раз и не меняется во
              время ремонта :). Однако хочется заметить, наши мастера зачастую делают гораздо больше чем положено по
              прайсу - это называется "человечность"
              </v-card-text>
            </v-card>
          </v-timeline-item>
          <v-timeline-item
            color="green lighten-2"
            large
          >
            <v-card class="elevation-2">
              <v-card-title class="headline">Качество</v-card-title>
              <v-card-text>
              Слышали фразу - "компания которая борится за клиента"? Дак вот, это мы!
              Все делаем как для себя.
              </v-card-text>
            </v-card>
          </v-timeline-item>
           <v-timeline-item
            color="grey lighten-2"
            large
          >
            <v-card class="elevation-2">
              <v-card-title class="headline">Доставка!</v-card-title>
              <v-card-text>
             Если вам необходима помощь в доставке, мы можем предложить курьерские услуги.
              </v-card-text>
            </v-card>
          </v-timeline-item>
            </v-timeline>

            </div>
       </v-col>
      <v-col
       xl="6" lg="6" md="11" sm="11" xs="11"
        class="content_in_block_about_in_home"
        >
        <container class="aih text_about_order">
          <v-col
          class="smoll_width90"
          md="10"
          lg="10"
          xl="10"
          sm="12"
          xs="12"
          offset-md="1"
          offset-lg="1"
          offset-xl="1"
          offset-xs="0"
          offset-sm="0"
          >
                <div>
                     <h2> {{this.$store.getters.ABOUT_ORDER_BLOCK[0].title}}</h2>
                </div>
                <div class="sep-element"></div>
                <h5>{{this.$store.getters.ABOUT_ORDER_BLOCK[0].sub_title}}</h5>
                <div class="space"></div>
                <div class="pix-item-review pix-text-review-left">
                  <div class="pix-overlay pix-color"></div>
                  <div class="pix-block-content">
                    <div class="card_round pix-icon-m pix-icon-color ">
                      <i class="material-icons">perm_phone_msg</i>
                      </div>
                      <div class="text pix-middle">
                        <h2 id="order_step_slogun">Шаг первый - звоните нам. </h2>
                      <p>Мы дадим исчерпывающею консультацию по всем интересующим вас вопросам. В некоторых случаях, мы даже
                        можем с ориентировать Вас по цене и срокам.
                      </p>
                      </div></div></div>
                <div class="pix-item-review pix-text-review-left">
                  <div class="pix-overlay pix-color"></div>
                  <div class="pix-block-content">
                    <div class="card_round pix-icon-m pix-icon-color ">
                      <i class="material-icons">local_shipping</i>
                      </div>
                      <div class="text pix-middle">
                        <h2 id="order_step_slogun">Шаг второй - Доставка</h2>
                      <p>Вы можете самостоятельно доставить телевизор в наш сервис или заказать доставку (к нам и обратно).
                        Внимание:Доставка нашим курьером платная, стоимость зависит от вашей удаленности от СЦ.
                      </p>
                      </div></div></div>
                <div class="pix-item-review pix-text-review-left">
                  <div class="pix-overlay pix-color"></div>
                  <div class="pix-block-content">
                    <div class="card_round pix-icon-m pix-icon-color ">
                      <i class="material-icons">settings_applications</i>
                      </div>
                      <div class="text pix-middle">
                        <h2 id="order_step_slogun">Шаг третий - Диагностика</h2>
                      <p>После доставки телевизора в сервисный центр, потребуется от одного до трех дней для проведения диагностики
                        неисправностей (Обычно один день, но бывают сложные неисправности, на диагностику которых требуется больше времени.</p>
                      </div></div></div>
                <div class="pix-item-review pix-text-review-left">
                  <div class="pix-overlay pix-color"></div>
                  <div class="pix-block-content">
                    <div class="card_round pix-icon-m pix-icon-color ">
                      <i class="material-icons">check_circle</i>
                      </div>
                      <div class="text pix-middle">
                        <h2 id="order_step_slogun">Шаг четвертый - Одобрение</h2>
                      <p>Подсчитываем все необходимое для приведения телевизора в идиальное состояние и озвучиваем Вам.
                            Так же оговарием четкий срок готовности аппарата.
                      </p>
                      </div></div></div>
                <div class="pix-item-review pix-text-review-left">
                  <div class="pix-overlay pix-color"></div>
                  <div class="pix-block-content">
                    <div class="card_round pix-icon-m pix-icon-color ">
                      <i class="material-icons">done_all</i>
                      </div>
                      <div class="text pix-middle">
                        <h2 id="order_step_slogun">Шаг пятый - Все довольны.</h2>
                      <p>По готовности заказа мы вновь отзваниваемся вам. Забираете или доставляем мы, выдаем гарантийный талон
                        сроком на  90 дней. Не забыаем оставить отзыв нашему сервисному центру!
                      </p>
                      </div></div></div>
          </v-col>
        </container>
      </v-col>
    </v-row>
</div>
<div class="price" id="price">

      <v-row>
        <v-col
        cols="12">
        <h2 class="price_title" v-if="showTitlePriceInSmollLcd">Стоимость ремонта для вашего случая
        </h2>

        </v-col>
      </v-row>
        <v-container class="gutter_ten"  grid-list-md text-xs-center>
          <v-layout row >
              <v-flex md4
              xs12
              sm8
              offset-sm2
              offset-xs0
               offset-md1
               ref="RightPriceBlock">
                      <v-card  class="price_block_height">
                        <v-card-text class="px-0 v-card__price">
                          <ul class="list4a"
                              id="to"
                              ref="floatLeft"
                            >
                            <h3>Выбрать тип аппарата</h3>
                            <a class="action_type"
                            v-for="(item,i) in $store.getters.TYPE_LCD" :key="i"
                            v-on:click="GetBrend(item.id), selectTypeDevice=item.type_lcd"
                            v-on:mouseover="SetImageTypeLcd(item.type_lcd_img)"
                            >
                            <li :value="item.type_lcd_img">
                            {{item.type_lcd}}
                            </li>
                            </a>
                          </ul>
                          <ul class="list4a bounceInLeft animated  3s"
                              id="priceStep2"
                              ref="priceStep2List"
                              v-if="priceStep2==true"
                            >
                             <h3>Выбрать бренд производителя</h3>
                            <a class="action_type"
                            v-for="(item,i) in $store.getters.TYPE_SIZE" :key="i"
                            v-on:mouseover="SetBrendImg(item.brend_size.brend_name.logo.logo_brend)"
                            >
                            <li :value="item"
                            v-on:click="selectedBrend=item.brend_size.brend_name.id , selectedBrendName=item.brend_size.brend_name.brend_name
                              ,SelectedBrend(i)"
                            >
                            {{item.brend_size.brend_name.brend_name}}
                            </li>
                            </a>
                          </ul>
                          <ul class="list4a bounceInLeft animated  3s "
                                      id="priceStep3"
                                      ref="priceStep3List"
                                      v-if="selectedBrend"
                                    >
                                    <h3 >
                                    Выбрать неисправнсть</h3>
                                    <a class="action_type"
                                    v-for="(item,index)  in $store.getters.MALFUNC" :key="index"
                                    v-on:click="GetMalfank(item.id , item.title)"
                                    >
                                      <li
                                      v-on:mouseover="contentMalfunk=item.content"
                                      >
                                      {{item.title}}
                                      </li>
                                    </a>
                          </ul>
                          <ul class="list4a bounceInLeft animated  3s  d-none"
                                  id="priceStep4"
                                  ref="priceStep4List"
                                >
                                 <h3
                                 v-if="selectedMulfunk"
                                 >
                                 Выбрать диагональ</h3>
                                <a class="action_type"
                                v-for="(item,i) in $store.getters.MALFUNK_SIZE" :key="i"
                                v-on:click="GetPriceAndInfo(item)"
                                >
                                <li>
                                диагональ  "{{item.size}}"
                                </li>
                                </a>
                          </ul>
                        </v-card-text>
                      </v-card>
                    </v-flex>
                <v-flex md6 xs12
                v-if="showRightBlockPriceForSmoll"
                ref="LeftPriceBlock">
                      <v-card  class="right_price_info centre price_block_height" style="width:95%; float: right">
                          <img
                                 ref="floatRight"
                                class="white--text"
                                style="width: 85%;height: 85%;"
                                :src="type_lcd_img" alt="">
                            <img
                                v-if="priceStep2==true"
                                 ref="priceStep2Img"
                                class="white--text bounceInRight animated  3s"
                                style="width: 85%;height: 85%;"
                                :src="priceStep2Img" alt="">
                                <div
                                 ref="divAfteSelectMalfunkImg"
                                 class="">
                                    <img
                                        v-if="selectedBrend"
                                        v-show='!contentMalfunk'
                                        ref="afteSelectMalfunkImg"
                                        class="white--text"
                                        style="width: 85%;height: 85%;"
                                        src="malfunc.png" alt="Диагностика телевизора, туристская 18">
                                        <div class="content"
                                          v-html="contentMalfunk"
                                        >
                                        </div>
                                        <h5 class="h5InImg"
                                        v-if="selectedBrend"
                                        > Внимание: Диагностика бесплатна!</h5>
                                  </div>
                            <img
                                v-if="selectedMulfunk"
                                 ref="priceStep4Img"
                                class="white--text bounceInRight animated  3s d-none search"
                                style="width: 85%;height: 85%;"
                                src="DiagonaliTVinch.png" alt="Диагональ экрана в сантиметрах">
                                <h5 class="h5InImg"
                                v-if="selectedMulfunk"
                                > Диагональ ТВ можно узнать по первым цифрам в модели!</h5>
                      </v-card>
                </v-flex>
                    <v-flex  class="d-none finali_show_price"
                    md12
                     ref="FinaliShowPrice">
                     <v-row>
                            <v-flex md6 class="hidden-for-small-down">
                              <v-card class="centre">
                                  <h2>Сверим данные:</h2>
                                  <ul class="price_sub_title">
                                      <h4> <i class="material-icons" id="icon_done">done</i>Тип аппарата: {{selectTypeDevice}}</h4>
                                      <h4> <i class="material-icons" id="icon_done">done</i> Бренд производителя: {{selectedBrendName}}</h4>
                                      <h4> <i class="material-icons" id="icon_done">done</i> Диагональ "{{ selectedDevicePrice.size}}"</h4>
                                      <h4> <i class="material-icons" id="icon_done">done</i>Неисправность: "{{ selectMalfunkTitle}}"</h4>
                                  </ul>
                                  </v-card>
                                </v-flex>
                                <v-flex md6>
                                  <v-card class="centre">
                                  <h2 >Стоимость ремонта:</h2>
                                  <ul class="price_sub_title_too">
                                      <h4> <i class="material-icons" id="icon_done">search</i>Стоимость диагностики: 0 руб. </h4>
                                      <h4> <i class="material-icons" id="icon_done">attach_money</i>Стоимость ремонта приблизительно: {{selectedDevicePrice.price}}руб.</h4>
                                      <h4> <i class="material-icons" id="icon_done">build</i> Ремонт продлится: 1-3 дня.</h4>
                                  </ul>
                                  <div class="price_sub_info">
                                    <h5>Внимание:</h5>
                                    <p>После принятия аппарата в сервисный центр, наши специалисты обязательно проведут
                                              тщательную диагностику, это необходимо для точного определиния как стоимости,
                                              так и времени ремонта. Сама же диагностика для Вас будет стоить 0 руб. , даже в случаи отказа от дальнейшего ремонта.
                                              Однако если вы выбрали услугу по доставки вашего аппарата в сервис курьером, <b>услуга оплачивается Вами в независимоти
                                                от результата.
                                              </b></p>
                                              <hr>
                                              <p>Сам же процесс ремонта, начнется только после вашего устного согласия с ценой и сроком!</p>

                                    </div>
                                  </v-card>
                                </v-flex>
                     </v-row>


                    </v-flex>

          </v-layout>
        </v-container>
      <v-row no-gutter id="aih" style="background-color: #1e1e1e; margin-bottom:0px;"
        >
      <v-col
       xl="6" lg="6" md="11" sm="11" xs="11"
        >
        <container class="aih text_about_order">
          <v-col
          md="10"
          lg="10"
          xl="10"
          xs="12"
          offset-md="2"
          offset-lg="2"
          offset-xl="2"
          offset-xs="0"
          >
                <div>
                     <h2 id="space_top_3"> Самые популярные  неисправности  современных ТВ</h2>
                </div>
                <div class="sep-element"></div>
                <h5>{{this.$store.getters.ABOUT_ORDER_BLOCK[0].sub_title}}</h5>
                <div class="space"></div>

          <div class="pix-progress-bar-section">
                <div class="pix-progress-bar" data-percent="100" style="width: 5%;">
                      <span class="pix-progress-bar-label" style="visibility: hidden">Нет изображения, звук есть</span>
                      <span class="pix-progress-bar-count" style="opacity: 1; visibility: hidden">45%</span>
                 </div>
                 <div class="pix-progress-bar" data-percent="90" style="width: 5%;">
                      <span class="pix-progress-bar-label" style="visibility: hidden">Не включается</span>
                      <span class="pix-progress-bar-count" style="opacity: 1;visibility: hidden">30%</span>
                  </div>
                  <div class="pix-progress-bar" data-percent="70" style="width: 5%;">
                      <span class="pix-progress-bar-label" style="visibility: hidden">Искажено изображение.</span>
                      <span class="pix-progress-bar-count" style="opacity: 1;visibility: hidden">12%</span>
                  </div>
                  <div class="pix-progress-bar" data-percent="50" style="width: 5%;">
                      <span class="pix-progress-bar-label" style="visibility: hidden">Сломан разъём</span>
                      <span class="pix-progress-bar-count" style="opacity: 1;visibility: hidden">8%</span>
                  </div>
                  <div class="pix-progress-bar" data-percent="25" style="width: 5%;">
                      <span class="pix-progress-bar-label" style="visibility: hidden">Другое</span>
                      <span class="pix-progress-bar-count hidden-sm-and-down" style="opacity: 1;visibility: hidden">5%</span>
                  </div>

            </div>
          </v-col>
        </container>
      </v-col>
      <v-col
            class="video_wrap hidden-sm-and-down"
            v-show="$vuetify.breakpoint.lg"
            cols="6"
          >
                    <a id="one" class="pix-video-popup" v-on:click="popUp" >
                    <img class="play" src="https://irepair.true-emotions.studio/wp-content/themes/irepair/images/play.svg" alt="">
                  <div class="item-pulse"></div>
                  </a>
       </v-col>
    </v-row>
</div>
</div>
</template>

<script>
import carousel from 'vue-owl-carousel'

export default {
    data () {
      return {
        isActive: false,
        showTitlePriceInSmollLcd:true,
        showRightBlockPriceForSmoll:true,
        slideContentHeight:'',
        contentMalfunk:'',
        selectMalfunkTitle:'',
        selectedMulfunk:'',
        selectedBrendName:'',
        toggleSelectedBrend:true,
        selectTypeDevice:'',
        selectedDevicePrice:'',
        sizeSelectedIndex:'',
        selectedBrend:'',
        brendIndex:'',
        priceStep2Img:'logo-brand-TV.png',
        priceStep2:false,
        flag_type_lcd_img:false,
        type_lcd_img:'',
        video_1:'',
        slideHeight: ' ',
        slideWidth:' ',
        showSlider: true,
        bottomSlaidBtn: '25%',
        slaidTextW: '40%',
        loading: false,
        selection: 1,
      }
    },
     components: { carousel },

     methods: {
          lazyScroll: function(el){
          document.getElementById(el).scrollIntoView({block: "start", behavior: "smooth"});
          },
       CorectionPositionTextInSlider(){
          var test2 =  document.getElementsByClassName('slide-caption')[1];
          var test1 =  document.getElementsByClassName('top-row')[0];
          var distance = (test2.offsetTop - parseInt(window.getComputedStyle(test2).lineHeight,10)) - (test1.offsetTop +test1.offsetHeight);
          var test3 =  document.getElementsByClassName('slide-text');
          if (distance< 20){
            var t2_bottom= window.getComputedStyle(test2).bottom
            var t3_bottom= window.getComputedStyle(test3[1]).bottom

                   document.getElementsByClassName('slide-caption')[0].style.bottom=parseInt(t2_bottom, 10) - distance +"px";
                   document.getElementsByClassName('slide-caption')[1].style.bottom=parseInt(t2_bottom, 10) - distance - 25+"px";
                   test3[1].style.bottom=parseInt(t3_bottom, 10) - distance - 25+"px";
                   //test3[0].style.bottom=parseInt(t3_bottom, 10) +"px";
                   var LowHeight =(parseInt(t3_bottom, 10) - distance - 25)

                    if (LowHeight <0){
                          var ElSlider = document.getElementsByClassName('slider_head')[0].style.height;
                          document.getElementsByClassName('slider_head')[0].style.height = parseInt(ElSlider, 10) + parseInt(-LowHeight,10) + 25+"px";
                    }
          }
       },
       TrackingScroll(){
         var elems = document.getElementsByClassName('pix-progress-bar')[0]
          if(this.CheckVisibility(elems)=== true){
            this.SetPixProgressBar();
          }
          var price = document.getElementsByClassName('price')[0]
          if(this.CheckVisibility(price)=== true){
            this.SetPreImgLcdType();
          }
       },
       CheckVisibility(el){
          var dTop = window.scrollY;
        //  var dBot = dTop + window.innerHeight;
          var elTop = el.offsetTop - (window.innerHeight/2);
          //var elBot = elTop + el.offsetHeight;
          return ((elTop <= dTop));
        },
       SetPixProgressBar(){
        var elems = document.getElementsByClassName('pix-progress-bar');
        var i=0
        var s=0
            for(i; i < elems.length; i++) {
                elems[i].style.transitionDelay = i+"s";
                elems[i].style.width = elems[i].getAttribute("data-percent") + "%";
                for(s; s< elems[i].childNodes.length; s++){
                elems[i].childNodes[s].style.visibility="visible";
                elems[i].childNodes[s].style.transition ="0.75s";
                elems[i].childNodes[s].style.transitionDelay = i+0.1+"s";
                }
                s=0;
            }
       },
       GetMalfank(id, t){
         this.selectedMulfunk = id;
         this.selectMalfunkTitle = t;
        try{
              this.$refs.priceStep3List.classList.add("zoomOutLeft","animated", "2s");
              this.$refs.divAfteSelectMalfunkImg.classList.add("zoomOutRight","animated", "2s");
                  setTimeout(() => {
                    this.$refs.priceStep3List.classList.add("d-none");
                    this.$refs.divAfteSelectMalfunkImg.classList.add("d-none");
                    this.$store.commit('SET_MALFUNK', {data:[this.selectedBrend, id,  this.selectTypeDevice]});
                    this.$refs.priceStep4List.classList.remove("d-none");
                    this.$refs.priceStep4Img.classList.remove("d-none");
                    }, 1800);}
                    catch{
                      this.$refs.priceStep3List.classList.add("zoomOutLeft","animated", "2s");
                      this.$refs.priceStep3List.classList.add("d-none");
                      this.$store.commit('SET_MALFUNK', {data:[this.selectedBrend, id,  this.selectTypeDevice]});
                      this.$refs.priceStep4List.classList.remove("d-none");
                    }
       },
        GetPriceAndInfo(item){
              this.selectedDevicePrice = item;
              try{
              this.$refs.RightPriceBlock.classList.add("zoomOutLeft","animated", "3s");
              this.$refs.LeftPriceBlock.classList.add("zoomOutRight","animated", "3s");
              this.$refs.FinaliShowPrice.classList.remove("d-none");
              this.$refs.FinaliShowPrice.classList.add("bounceInDown","animated", "3s");
              this.showRightBlockPriceForSmoll=true;
              setTimeout(() => {
                    this.$refs.RightPriceBlock.classList.add("d-none");
                    this.$refs.LeftPriceBlock.classList.add("d-none");
                    }, 300);}
                    catch{
                      this.$refs.RightPriceBlock.classList.add("zoomOutLeft","animated", "3s");
                      setTimeout(() => { this.$refs.RightPriceBlock.classList.add("d-none"); this.$refs.LeftPriceBlock.classList.add("d-none");}, 300);
                      this.showRightBlockPriceForSmoll=true;
                       this.$refs.FinaliShowPrice.classList.remove("d-none");
                      this.$refs.FinaliShowPrice.classList.add("bounceInDown","animated", "3s");
                      this.showTitlePriceInSmollLcd =false;

                    }
        },
        SetBrendImg(img){
          this.priceStep2Img= 'http://localhost:8000'+img;
       },
       SelectedBrend(index){
        this.brendIndex= index
         try {
        this.$refs.priceStep2Img.classList.add("fadeOutRightBig","animated", "3s");
        this.$refs.priceStep2List.classList.add("fadeOutLeftBig","animated", "3s");
          setTimeout(() => {
               this.$refs.priceStep2Img.classList.add("d-none");
               this.$refs.priceStep2List.classList.add("d-none");
               }, 250);
         }catch{
           this.$refs.priceStep2List.classList.add("fadeOutLeftBig","animated", "3s");
            setTimeout(() => {
               this.$refs.priceStep2List.classList.add("d-none");
               }, 250);
         }
       },
       SetPreImgLcdType(){
         if(this.flag_type_lcd_img===false){
          this. type_lcd_img=this.$store.getters.TYPE_LCD[1].type_lcd_img;
          this.flag_type_lcd_img = true;}
       },
       SetImageTypeLcd(img){
               this. type_lcd_img=img;
       },
       GetBrend(id){
         this.typeLcdId=id;
         this.$store.commit('SET_TYPE_SIZE', id);
         try {
         this.$refs.floatRight.classList.add("fadeOutRightBig","animated", "3s");
         this.$refs.floatLeft.classList.add("fadeOutLeftBig","animated", "3s");
          setTimeout(() => {
               this.$refs.floatRight.classList.add("d-none");
               this.$refs.floatLeft.classList.add("d-none");
               }, 250);
         }catch{
           this.$refs.floatLeft.classList.add("fadeOutLeftBig","animated", "3s");
            setTimeout(() => {
               this.$refs.floatLeft.classList.add("d-none");
               }, 250);
         }
          setTimeout(() => {
               this.priceStep2=true;
               }, 250);
       },
       closePopUp(){
        document.getElementById('video1').pause();
        document.getElementById('modal-container').classList.remove("one");
        document.body.removeAttribute("class");
       },
       popUp () {
        document.getElementById('modal-container').removeAttribute("class");
        document.getElementById('modal-container').classList.add("one");
        document.body.classList.add('modal-active');
        this.video_1 = this.$store.getters.ABOUT_ORDER_BLOCK[0].video;
       },
        reserve () {
            this.loading = true;
            setTimeout(() => (this.loading = false), 2000)

      },
            onResize() {

                    if  (window.screen.height < window.screen.width){
                      this.slideHeight = window.screen.height +"px";
                      this.slideContentHeight =this.slideHeight;
                      this.showSlider = true;
                      if (window.screen.width >600 && window.screen.width <700){
                     this.slideHeight = window.screen.height +50 +"px";
                     this.showRightBlockPriceForSmoll=false;
                      }
                    }
                    else if (window.screen.width >360 && window.screen.width <420){
                      this.slideHeight = window.screen.height/1.7+"px";
                      this.showRightBlockPriceForSmoll=false;
                    }
                    else{
                      this.slideHeight = window.screen.height/2 +40+"px";
                    }
                    if (window.screen.width >=320 && window.screen.width <360){
                      this.showRightBlockPriceForSmoll=false;
                      this.slideHeight = window.screen.height/1.5+"px";
                    }

                    if(window.screen.width<320){
                      this.showRightBlockPriceForSmoll=false;
                        this.showSlider = false;
                    }
                     if (window.screen.width >1280 && window.screen.width <=1600){
                      this.slideHeight = window.screen.height+"px";
                    }
                    if (window.screen.width >851 && window.screen.width <=1280){
                           this.slideHeight = window.screen.height*0.8+"px";
                            this.slideContentHeight=window.screen.height*0.7+"px";
                          this.bottomSlaidBtn='0%';
                          this.slaidTextW='55%'
                    }
                       if (window.screen.width >781 && window.screen.width <850){
                         this.showRightBlockPriceForSmoll=false;
                        this.slideHeight = window.screen.height+ 50+"px";
                    }
                      if (window.screen.width >760 && window.screen.width <780){
                        this.showRightBlockPriceForSmoll=false;
                        this.slideContentHeight=(window.screen.height/3)*1.4 +"px";
                          this.bottomSlaidBtn='-5%';
                          this.slaidTextW='55%'
                    }
                    if (window.screen.width<= 1365 && window.screen.width>=1280 ){
                      this.bottomSlaidBtn='15%';
                      this.slaidTextW='45%'
                    }
                      if (window.screen.width<= 1600 && window.screen.width>= 1366){
                      this.bottomSlaidBtn='20%';
                      this.slaidTextW='45%'
                    }
                       if (window.screen.width<= 1920 && window.screen.width>= 1080){
                      this.bottomSlaidBtn='19%';
                      this.slaidTextW='40%'
                    }
                    if (window.screen.width>window.screen.height&& window.screen.width>= 900  && window.screen.width<= 1200){
                      this.bottomSlaidBtn='0%';
                      this.slaidTextW='50%'
                    }
                     if (window.screen.width<= 800&& window.screen.width>= 770){
                      this.bottomSlaidBtn='5%';
                      this.slaidTextW='60%'
                    }
                      if (window.screen.width<= 900&& window.screen.width>= 800){
                      this.bottomSlaidBtn='0%';
                      this.slaidTextW='60%'
                    }
                    if (window.screen.width>=600 && window.screen.width<= 769){
                      this.bottomSlaidBtn='0%';
                      this.slaidTextW='60%'
                    }
                     if (window.screen.width<= 600&& window.screen.width>= 420){
                       this.showRightBlockPriceForSmoll=false;
                      this.bottomSlaidBtn='5%';
                      this.slaidTextW='60%'
                    }
                     if (window.screen.width<= 420&& window.screen.width>= 320){
                       this.showRightBlockPriceForSmoll=false;
                      this.bottomSlaidBtn='2%';
                      this.slaidTextW='100%'
                    }
                    if (window.screen.width<= 960){
                      this.showRightBlockPriceForSmoll=false;
                    }
                    if (window.screen.width<= 600&& window.screen.width>= 420){
                      this.bottomSlaidBtn='18%';
                      this.slaidTextW='75%'
                    }
                    setTimeout(this.CorectionPositionTextInSlider, 1000);

  },
  afteRenderUpdate(){
    let topPanel = document.getElementById('topPanel');
    let floatPanel = document.getElementById('float_panel');
    floatPanel.style.marginBottom = '0px';
    topPanel.style.position = 'absolute';
    topPanel.style.backgroundColor='transparent';
},
    async scrollToBlock(){
      if(this.$route.params.id){
        var el = this.$route.params.id;
        this.$nextTick(() => document.getElementById(el).scrollIntoView({block: "start"}));
      }

}
},

  computed:{
    //
  },

    created() {
      this.scrollToBlock();
      window.addEventListener("orientationchange", function() {
          // Announce the new orientation number
          location.reload()
        }, false);
          this.handleDebouncedScroll = this.TrackingScroll ;
          window.addEventListener('scroll', this.handleDebouncedScroll);

},
  beforeUpdate() {
     this.afteRenderUpdate();
  },
      beforeDestroy() {
          window.removeEventListener('scroll', this.handleDebouncedScroll);
},
mounted(){
    this.onResize();
    this.$store.dispatch('GET_ABOUT_IN_HOME');
    this.$store.dispatch('GET_ABOUT_ORDER_BLOCK');
    this.$store.dispatch('GET_TYPE_LCD');
}
}

</script>


<style scoped>
#malfunk > .v-card__title{
margin: 15px 0px 15px 0px !important;
}
.m-card{
  height: 420px !important;
  overflow:hidden;
}
.time_line_wrap{
  background-image: url('../assets/black_man.jpg');
  background-size: auto 100%;
  background-position-x: 20%;
  background-repeat: no-repeat;
}
.text_about_order h2{
  margin-top:0em !important;
}
.right_price_info{
  height: 100%;
      }
#space_top_3{
  margin-top:3em;
  text-align: inherit;
}
.pix-progress-bar span.pix-progress-bar-count {
    position: absolute;
    font-size: 14px;
    color: #fff;
    font-weight: 600;
    line-height: normal;
    right: 25px;
    top: 0;
    bottom: 0;
    margin: auto 0;
    height: 20px;
}
.pix-progress-bar-section{
  margin-bottom: 100px;
}
.pix-progress-bar .pix-progress-bar-label {
    font-family: 'Roboto', sans-serif;
    font-size: 14px;
    color: #fff;
    font-weight: 600;
    line-height: normal;
    white-space: nowrap;
}
.pix-progress-bar{
  background: linear-gradient(to right, #2052c9,#21a5dd);
  position: relative;
    width: 100%;
    margin: 15px 0;
    padding: 25px;
    -webkit-border-radius: 100px;
    border-radius: 100px;
    transition: .75s;
}
.price_sub_info{
  padding-left: 5%;
  padding-right: 5%;
}
.price_sub_info h5{
    margin-top: 15px;
    line-height: 40px;
    font-size: 1.2rem;
    font-family: 'Roboto', sans-serif;
}
.price_sub_info p{
    font-family: 'Open Sans', sans-serif;
}
.price_sub_title_too{
    text-align: start;
    font-family: 'Roboto', sans-serif;
    font-weight: 600;
    font-size: 1.2rem;
    padding-left: 20%;
    line-height: 40px;

}
.price_title{
    font-size: 2.4rem;
    color: black; /* #0936a0;*/
}
.price_sub_title{
    text-align: start;
    font-family: 'Roboto', sans-serif;
    font-weight: 600;
    font-size: 1.2rem;
    padding-left: 20%;
    line-height: 40px;
}
#icon_done{
    font-family: 'Material Icons';
    font-weight: normal;
    font-style: normal;
    font-size: 1.2rem;
    vertical-align: text-top;
    color: #074007;
    padding-right: 5px;
}
.price h2{
  text-align: center;
  font-family: 'Fira Sans', sans-serif;
  font-weight: 600;
  font-size: 2.4rem;
  padding-bottom: 20px;
  line-height: 45px;
}
.h5InImg{
font-size: 1.1rem;
}
.list4a h3{
  text-align: center;
  margin-bottom: 25px;
  font-family: 'Fira Sans', sans-serif;
  font-weight: 600;
}
.d-none{
  display: none;
}
.floatRight{
  position: relative;
  right: -1000px;
  transition: transform 2s ease-in-out;
}
.floatLeft{
  position: relative;
  left: -1000px;
  transition: transform 2s ease-in-out;
}
.centre{
  text-align: center;
}
.v-card__price{
  height: 450px;
  overflow-x: hidden;
  margin-left:5%;
  font-family: 'Roboto', sans-serif;
  font-weight: 600;
 font-size: 18px !important;
}
/* style for list price */
.list4a { padding:0; list-style: none; counter-reset: li; } .list4a li {
position: relative; padding:12px 20px 20px 28px; margin-left: 40px;
transition-duration: 0.3s; } .list4a li:before { border: 6px solid transparent;
line-height: 30px; position: absolute; top: 0; left:-30px; width:42px;
text-align:center; font-size: 13px; font-weight: bold; color: #77AEDB;
counter-increment: li; content: counter(li); transition-duration: 0.3s;
-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing:
border-box; } .list4a li:hover:before { color: #337AB7; } .list4a li:after {
position: absolute; top: 0; left: -30px; width: 42px; height: 42px; border: 6px
solid #3399FF; border-radius: 50%; content: ''; opacity: 0.5;
-webkit-box-sizing: border-box; -moz-box-sizing: border-box; box-sizing:
border-box; } .list4a li:hover:after { animation: 500ms ease-in-out 0s bounceIn;
opacity: 1; } @keyframes bounceIn { 0% { opacity: 0; transform: scale3d(.3, .3,
.3); } 20% { transform: scale3d(1.3, 1.3, 1.3); } 40% { transform: scale3d(.9,
.9, .9); } 60% { opacity: 1; transform: scale3d(1.03, 1.03, 1.03); } 80% {
transform: scale3d(.97, .97, .97); } to { opacity: 1; transform: scale3d(1, 1,
1); } }
/* style for list price */

.gutter_ten{
  max-width: 95%;
}
.text>p{
  color: #ccc;
  font-size: 16px;
}
.space{
  width: 100% ;
  height: 75px;
}
#order_step_slogun{
  font-size: 22px;
  padding-bottom:5px;
}
.pix-icon-m>i{
      margin-left: 25%;
      margin-right: auto;
      margin-bottom: auto;
      margin-top: 25%;
      color: aliceblue;
      font-size: 45px;
}
.pix-item-review .text {
    display: inline-block;
}
.pix-icon-m .icon svg, .pix-icon-m .icon img {
    width: 35px;
    max-height: 35px;
}
.pix-item-review .round .icon {
    fill: #fff;
    margin: auto;
}
html .pix-item-review .round{
    background: linear-gradient(to right, #2052c9,#21a5dd);

}
.pix-item-review .pix-block-content {
    display: grid;
    grid-template-columns: auto 1fr;
    grid-column-gap: 30px;
    padding-bottom: 25px;
}
.pix-overlay {
    opacity: 0;
    position: absolute;
    width: 100%;
    height: 100%;
    left: 0;
    top: 0;
    content: '';
    background: #333;
    -webkit-transition: .35s;
    -o-transition: .35s;
    transition: .35s;
}
html .pix-overlay.pix-color {
    background: #2052c9;
    background: -webkit-linear-gradient(left, #2052c9,#21a5dd);
    background: -o-linear-gradient(right, #2052c9,#21a5dd);
    background: -moz-linear-gradient(right, #2052c9,#21a5dd);
    background: linear-gradient(to right, #2052c9,#21a5dd);
}
.pix-item-review {
    position: relative;
}
.aih h5{
    font-family: 'Fira Sans', sans-serif;
    font-weight: 400;
    font-size: 20px;
    padding-bottom: 20px;
    line-height: 25px;
    color: white;
}
.aih h2{
    font-family: 'Fira Sans', sans-serif;
    font-weight: 600;
    font-size: 38px;
    padding-bottom: 20px;
    line-height: 45px;
    color:white;
    margin-top:2em;
}
.item-pulse {
    content: "";
    width: 70px;
    height: 70px;
    -webkit-border-radius: 150px;
    border-radius: 150px;
    background: #2052c9;
    position: absolute;
    z-index: 3;
    cursor: pointer;
    -webkit-transition: .35s;
    -o-transition: .35s;
    transition: .35s;
    top: 50%;
    left: 50%;
    margin-top: -35px;
    margin-left: -35px;
    animation: shadow 1s ease infinite;
}
@keyframes shadow {
  0% {
    box-shadow: 0 0 0 0 rgba(55, 141, 250, .8);
  }
  100% {
    box-shadow: 0 0 0 20px rgba(55, 141, 250, 0);
  }
}
.play {
    position: absolute;
    left: 50%;
    top: 50%;
    margin-left: -10px;
    margin-top: -14px;
    width: 30px;
    height: 30px;
    z-index: 50;
    -webkit-filter: none;
    filter: none;
    cursor: pointer;
}
.video_wrap{
  background-image: url("https://irepair.true-emotions.studio/wp-content/uploads/2018/06/kompetente-techniker.jpg?id=3189");
  background-size: cover;
  position: relative;
  background-position-x: center;
}
.call_to_action{
    border-radius: 5px;
    height: 50px !important;
    background-color: #2052c9 !important;
    margin-top: 0.3em;
    margin-bottom: 0.3em;
    margin-left: 1%;
}
.call_to_action_p{
  padding: 15px 10px 15px 10px;
  margin-bottom: 0px;
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
.button_left{
text-align: left;
margin-top: 25px;
margin-bottom: 25px;
}
.about_content{
  font-size: 16px;
  font-weight: 400;
  line-height: 28px;
  font-family: 'Open Sans', sans-serif;
}
.sep-element{
  padding-top: 20px;
  width: 40px;
  border-top: 4px solid;
  border-color: #2052c9;
}
.title_about{
  font-family: 'Fira Sans', sans-serif;
  font-weight: 600;
  font-size: 35px;
  line-height: 45px;
}
.content_in_block_about_in_home{
  padding-left: 25px;
  padding-right: 50px;
  padding-top: 15%;
  padding-bottom: 50px;
}
#aih{
  margin-top: 50px;
  margin-bottom: 75px;
}
.img_in_block_about_in_home{
    background-size: contain;
    background-repeat: no-repeat;
    background-position-x: 50px;
    background-position-y: -50px;
}
.v-card__title{
    font-size: 22px;
    font-family: 'Roboto', sans-serif;
}
.v-card__text{
  font-size: 16px;
}
.row_in_center a{
  text-decoration: none;
}
#malfunk{
  padding-top:50px;
  padding-bottom: 75px;
  background-color: #f7f8f9;
}
.v-card:hover #img_round{
    margin: 10px;
    transition: .75s;
    transition-timing-function: cubic-bezier(0, -0.38, 0.45, 1.56);
}
.v-card{
  padding-top: 10px;
}
.row_in_center{
  width: 90%;
  margin-left: 5%;
  margin-right: 5%;
  padding: 0% 5% 0% 5%;
}
#img_round{
  border-radius: 50%;
  margin: 15px;
  overflow: hidden;
}
.card_round{
  margin-top:15px;
  border-radius: 150px;
  width: 75px;
  height: 75px;
  overflow: hidden;
  background:linear-gradient(to right, #2052c9,#21a5dd);
  margin-left: 15px;
}
.slider_head{
 background-color:black;
 overflow: hidden;
}
.slid_img{
  margin-top: 40px;
  overflow: hidden;
}
.slid_img {
    animation-duration: 15001ms;
    animation-fill-mode: both;
}
      .item {
        position: relative;
        }

        .slide-caption{
         max-width: 40%;
         white-space: normal;
         font-size: 60px;
         line-height: 62px;
         font-weight: 600;
         color: rgb(255, 255, 255);
         letter-spacing: 0px;
         font-family: 'Fira Sans', sans-serif;
         visibility: inherit;
         text-align: left;
         border-width: 0px;
         margin: 0px;
         padding: 0px;
         min-height: 0px;
         max-height: none;
          display: block;
          left: 10%;
          bottom: 40%;
          position: absolute;
          animation-iteration-count: 1;
          animation-duration: 1s;
          animation-delay: 1.5s;
          margin-bottom: 40px;
            }
        .slide-text{
          max-width: 40%;
          white-space: normal;
          font-size: 16px;
          line-height: 24px;
          font-weight: 500;
          color: rgb(145, 145, 145);
          letter-spacing: 0px;
          font-family: 'Open Sans', sans-serif;
          visibility: inherit;
          text-align: left;
          border-width: 0px;
          margin: 0px;
          padding: 0px;
          min-height: 0px;
          max-height: none;
          position: absolute;
          bottom: 20%;
          left: 10%;
          animation-iteration-count: 1;
          animation-duration: 1s;
          animation-delay:  2s;
        }
        #slaid_btn_l{
        white-space: nowrap;
        font-size: 15px;
        line-height: 17px;
        font-weight: 600;
        color: rgb(255, 255, 255);
        font-family: 'Roboto', sans-serif;
        background-color: rgb(0, 122, 255);
        border-color: rgba(255, 255, 255, 0);
        border-style: solid;
        border-width: 2px;
        border-radius: 5px;
        outline: none;
        box-shadow: rgb(153, 153, 153) 0px 0px 0px 0px;
        box-sizing: border-box;
        cursor: pointer;
        visibility: inherit;
        transition: none 0s ease 0s;
        text-align: inherit;
        padding: 18px 30px 18px;
        letter-spacing: 0px;
        height: auto;
        }
        #slaid_btn_l:hover{
          background-color: transparent;
          border-color:rgb(0, 122, 255);
        }
        #slaid_btn_r{
        white-space: nowrap;
        font-size: 15px;
        line-height: 17px;
        font-weight: 600;
        color: rgb(255, 255, 255);
        font-family:  'Roboto', sans-serif;
        background-color: transparent;
        border-color: rgb(255, 255, 255);
        border-style: solid;
        border-width: 2px;
        border-radius: 5px;
        outline: none;
        box-shadow: rgb(153, 153, 153) 0px 0px 0px 0px;
        box-sizing: border-box;
        cursor: pointer;
        visibility: inherit;
        transition: none 0s ease 0s;
        text-align: inherit;
       padding: 18px 30px 18px;
        letter-spacing: 0px;
        height: auto;
        }
    .row_slaid_btn{
      margin-top:5%;
    }
    @media (max-width: 960px) and (min-width: 640px) {
      #space_top_3{
        margin-top: 20px !important;
      }
      .content_in_block_about_in_home{
        padding-top:0px !important;
        padding-bottom: 50px !important;
      }
    }
     @media (max-width: 640px) and (min-width: 320px)and (orientation:portrait) {
       .smoll_width90{
         width: 90% ;
       }
       .pix-progress-bar-section{
         margin-bottom: 25px !important;
       }
       .pix-progress-bar{
         padding: 15px;
       }
       .pix-progress-bar-count{
         top: 40% !important;
         height: auto !important;
       }
       .pix-progress-bar-label, .pix-progress-bar-count{
         font-size: 12px !important;
       }
       #space_top_3{
        margin: 0px 0px 0px 0px;
        font-size: 1.5rem;
       }
       .price_sub_info p {
         font-size: 0.8rem;
       }
       .price_sub_title_too{
        padding-left: 10%;
        padding-right: 10%;
        margin-top: 30px;
        font-family: 'Fira Sans', sans-serif;
        font-size: 1rem;
        font-weight: 400;
        text-align: center;
       }
       .hidden-for-small-down{
         display: none;
       }
       .v-card__price{
         margin-left: 0px;
       }
       .list4a h3{
        text-align: center;
        margin-bottom: 25px;
        font-family: 'Fira Sans', sans-serif;
        font-weight: 600;
        font-size: 1rem;
      }
       .price h2{
        font-size: 1.5rem;
        line-height: 30px;
        margin: 0px 25px 0px 25px;
        padding-bottom: 0px;
        padding-top: 10px;
       }
      .row_slaid_btn{
        margin-left: 10px;
      }
      .right_price_info{
        width: 100% !important;
      }
      .price_block_height{
        height: 450px;
        overflow-y: scroll;
        overflow-x: hidden;
      }

     }
      @media (max-width: 1920px) and (min-width: 1600px) {
      .slide-caption{
        font-size: 76px;
        bottom: 46%;
        line-height: 100px;

      }
      .slide-text{
        font-size: 32px;
        line-height: 42px;
      }
       #slaid_btn_l,  #slaid_btn_r{
        padding: 20px 40px 20px;
         font-size: 24px;
     }
      }
      @media (max-width: 1600px) and (min-width: 1460px) {
      .slide-caption{
        font-size: 72px;
        bottom: 47%;
      }
      .slide-text{
        font-size: 26px;
        line-height: 37px;
      }
       #slaid_btn_l,  #slaid_btn_r{
        padding: 15px 30px 15px;
        font-size: 20px;
     }
     }
        @media (max-width: 1460px) and (min-width: 1366px) {
      .slide-caption{
        font-size: 58px;
        bottom: 46%;
      }
      .slide-text{
        font-size: 22px;
        line-height: 37px;
      }
       #slaid_btn_l,  #slaid_btn_r{
        padding: 15px 30px 15px;
        font-size: 16px;
     }
     }
     @media (max-width: 1366px) and (min-width: 960px) {
      #slaid_btn_l,  #slaid_btn_r{
        padding: 15px 20px 15px
     }
    .content_in_block_about_in_home{
        padding-top:0%;
    }
     }
@media (max-width: 1200px) and (min-width: 961px){
        .slide-caption{
        margin-bottom: -5%;
        line-height: 45px;
        font-size: 32px;
        }
}
@media (max-width: 1200px) and (min-width: 961px)and (orientation:portrait) {

        .slide-caption{
        margin-bottom: -15%;
        line-height: 45px;
        font-size: 32px;
        }
}
    @media (max-width: 750px) and (min-width: 600px) {

    .slide-caption{
      margin-bottom: -2%;
      line-height: 35px;
      font-size: 28px;
      }
      #slaid_btn_l,  #slaid_btn_r{
        padding: 8px 16px 8px;
         font-size: 13px;
     }
      .slide-text{
        max-width: 60% !important;
        color: rgb(214, 209, 209);
      }
    }
    @media (max-width: 960px) and (min-width: 750px) {

    .slide-caption{
      margin-bottom: -5%;
      line-height: 45px;
      font-size: 36px;
      }
      #slaid_btn_l,  #slaid_btn_r{
        padding: 8px 16px 8px;
         font-size: 13px;
     }
      .slide-text{
        max-width: 60% !important;
        color: rgb(214, 209, 209);
      }
    }
       @media (max-width: 420px) and (min-width: 320px) {
         .hidden_round{
           display: none;
         }
         .section-title{
           margin-top:0px !important;
         }
         .title_about{
           font-size: 1.6rem !important;
         }
         .block_malfunk{
           height:480px !important;
         }
         .slaider_html{
           margin-left: 10px;
           margin-right: 10px;
         }
         #aih{
           margin-top: 5px; margin-bottom: 20px;
         }
         .gt30{
           padding-right: 30px;
         }
         .card-title-malf{
          margin: 0px 0px 0px 20px!important;
          width: 100%;
         }
        .card-text-malf{
          font-size: 13px !important;
          text-align: inherit !important;
         }
         #order_step_slogun{
          padding-left: 30%;
         }
         .pix-block-content, .pix-middle{
           display: block !important;
         }
         .pix-middle p{
           padding-left: 5%
         }
         .space{
        height: 40px;
         }
         .card_round{
            border-radius: 102px;
            width: 45px;
            height: 45px;
            float: left;
         }
         .card_round i{
           font-size: 24px;
         }
         .text_about_order h2{
        font-size: 24px;
        line-height: 37px;
         }
        .text_about_order h5{
         font-size: 14px;
        }
      .slide-caption{
        font-size: 18px;
         max-width: 90%;
         margin-bottom:10px ;

      }
      #slaid_btn_l,  #slaid_btn_r{
        padding: 6px 12px 6px;
         font-size: 13px;
     }
      #slaid_btn_l{
        margin-right: 10px;
      }

      .slide-text{
        position: inherit;
        color: rgb(214, 209, 209);
        left: 1%;
        font-size: 14px;
      }
    }
    @media (max-width: 600px) and (min-width: 420px) {
      #aih{ margin-top: 5px; margin-bottom: 20px; }
       .gt30{ padding-right: 30px; }

      .slide-caption{
        font-size: 28px;
         max-width: 90%;
         margin-bottom:5%;
         padding-bottom: 15px;
         left: 5%;

      }
      #slaid_btn_l,  #slaid_btn_r{
        padding: 6px 12px 6px;
         font-size: 13px;
     }
      #slaid_btn_l{
        margin-right: 10px;
      }

      .slide-text{
        position: absolute;
        color: rgb(214, 209, 209);
        left: 5%;
        font-size: 14px;
      }
    }
    @media (max-width: 980px) and (min-width: 320px) {
      .content_in_block_about_in_home{
      padding-left: 25px;
      padding-right: 0px;
      padding-top: 5%;
      padding-bottom: 15%;

      }
    }

/* MODAL UP */
html.modal-active, body.modal-active {
  overflow: hidden;
}

#modal-container {
  position: fixed;
  display: table;
  height: 100%;
  width: 100%;
  top: 0;
  left: 0;
  transform: scale(0);
  z-index: 999;
}
#modal-container.one {
  transform: scaleY(0.01) scaleX(0);
  animation: unfoldIn 1s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
}
#modal-container.one .modal-background .modal {
  transform: scale(0);
  animation: zoomIn 0.5s 0.8s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
}
#modal-container.one.out {
  transform: scale(1);
  animation: unfoldOut 1s 0.3s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
}
#modal-container.one.out .modal-background .modal {
  animation: zoomOut 0.5s cubic-bezier(0.165, 0.84, 0.44, 1) forwards;
}
#modal-container .modal-background {
  display: table-cell;
  background: rgba(0, 0, 0, 0.89);
  text-align: center;
  vertical-align: middle;
}
#modal-container .modal-background .modal {
  background: white;
  padding: 50px;
  display: inline-block;
  border-radius: 3px;
  font-weight: 300;
  position: relative;
}
#modal-container .modal-background .modal h2 {
  font-size: 25px;
  line-height: 25px;
  margin-bottom: 15px;
}
#modal-container .modal-background .modal p {
  font-size: 18px;
  line-height: 22px;
}
#modal-container .modal-background .modal .modal-svg {
  position: absolute;
  top: 0;
  left: 0;
  height: 100%;
  width: 100%;
  border-radius: 3px;
}
#modal-container .modal-background .modal .modal-svg rect {
  stroke: #fff;
  stroke-width: 2px;
  stroke-dasharray: 778;
  stroke-dashoffset: 778;
}
@keyframes unfoldIn {
  0% {
    transform: scaleY(0.005) scaleX(0);
  }
  50% {
    transform: scaleY(0.005) scaleX(1);
  }
  100% {
    transform: scaleY(1) scaleX(1);
  }
}
    /*
    font-family: 'Roboto', sans-serif;
font-family: 'Open Sans', sans-serif;
font-family: 'Fira Sans', sans-serif;
*/
</style>