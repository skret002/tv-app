<template>
<div>
<v-flex lg12 md12 xl12 xs12 sm12>
<v-row>
  <div style=" width: 100%;">
    <v-app-bar
      color="#403f3f accent-12"
      dense
      dark
    >
    <v-row align="center">
      <v-flex class="hidden-md-and-down" lg3 offset-lg1 xl3 offset-xl1>
        <v-select
          class="selected_category"
          :items="category "
          :menu-props="{ top: false, offsetY: true }"
          v-model="select"
          v-on:change="setInitData()"
          label="Фильтр по категории"
        ></v-select>
      </v-flex>
      <v-flex  offset-xl1 xl3 lg4 md6 sm6 xs6>
        <v-text-field
        v-model="search_val"
        v-on:input="setSearching()"
        class="mx-4"
        flat
        hide-details
        label="Найти..."
        prepend-inner-icon="search"
        solo-inverted
      ></v-text-field>
      </v-flex>
       <v-flex xl3 offset-xl1  lg4 md6 sm6 xs6>
         <v-row class="row_cart">
                <span class="material-icons hidden-md-and-down">
                    shopping_cart
                </span>
               <a @click="showCart=true" v-if="totalBy"> <p >В корзине товаров - {{totalBy}}шт. | {{totalPrice}} руб.  </p></a>
                <p v-else>Корзина пуста</p>
         </v-row>
       </v-flex>
  </v-row>
      <v-menu
        left
        bottom
      >
        <v-list>
          <v-list-item
            @click="() => {}"
          >
            <v-list-item-title>Option</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
    </v-app-bar>
  </div>
</v-row>
</v-flex>
<v-row v-if="notItem && !showCart">
  <v-flex
    class="cart_product"
    v-for="(i,id) in parts" :key="id"
    lg4  xl3>
      <v-card class="mx-auto" max-width="344">
        <a @click="addImgsForParts(i.id)">
            <v-img  class="img_part"
            height="200px"
            :src=i.f_img
          >
        </v-img>
        </a>
        <v-card-title>
          {{i.title}}
        </v-card-title>

        <v-card-subtitle>
          Цена: {{i.price}}руб.
        </v-card-subtitle>

    <v-card-actions>
      <v-btn text class="add_shop"
      @click="addCart(i.id, i.title, i.price, i.f_img, i.stock)"
      >
        <span class="material-icons">
        add_shopping_cart
        </span>
        Купить
      </v-btn>
      <v-spacer></v-spacer>

      <v-btn
        icon
        @click="showId(id)"
      >
        <v-icon>{{ show? 'mdi-chevron-up' : 'mdi-chevron-down' }}</v-icon>
      </v-btn>
    </v-card-actions>

    <v-expand-transition>
      <div v-show="show==id">
        <v-divider></v-divider>

        <v-card-text>
        <p v-if="i.stock==0">Товар в наличии</p>
        <p v-else-if="i.stock==1">Товара сейчас нет в наличии</p>
        <p v-else>Товар скоро появится</p>
        <p>Доставка по городу: {{i.delivery_of_spb}} руб.</p>
        <p v-if="i.delivery_of_region==true">Отправим в регион : СДЭК или Boxberry</p>
        <p v-else>Отправка в регион не возможна</p>
        <p v-if="i.status_part == 0 ">Состояние товара: БУ (снят с битика)</p>
        <p v-else-if="i.status_part == 1"> Запчасть НОВАЯ</p>
        <p v-else> Под восстановление или донор </p>
        <p>Гарантия: {{i.guarantee}}</p>
        </v-card-text>
      </div>
    </v-expand-transition>
  </v-card>

  </v-flex>
</v-row>
<div v-else-if="showCart">
  <v-row>
    <v-flex lg10 offset-lg1 xs12 offset-xs0 class="row_cart_one"
    >

    <v-row>
      <v-flex lg10 offset-lg1  xs12 offset-xs0 >
      <div class="cart_status_info">
        <h4>Корзина</h4>
        <p @click="showCart=!showCart" class="back_sale"> вернуться к покупкам</p>
      </div>
      </v-flex>
      </v-row>

          <v-row>
              <v-flex  lg10 offset-lg1 md12 offset-md0 xs12 offset-xs0>
                <v-row class="separait_row" v-for="(i,id) in cart" :key="id">
                    <v-flex  class="col_cart_img hidden-md-and-down"  lg2 md-hidden>
                        <v-img  class="img_part"
                          height="100%"
                          :src=i.img
                        >
                      </v-img>
                    </v-flex>
                    <v-flex class="col_cart" lg3 md3 sm3 xs3> <v-text>{{i.title}}</v-text> </v-flex>
                    <v-flex class="col_cart" lg2 md2 sm2 xs2> <v-text> Цена: {{i.price}}</v-text> </v-flex>
                    <v-flex class="col_cart" lg2 md3 sm3 xs3>
                      <v-text v-if="i.stock==0">Товар в наличии</v-text>
                      <v-text v-else-if="i.stock==1">Товара сейчас нет в наличии</v-text>
                      <v-text v-else>Товар скоро появится</v-text>
                    </v-flex>
                    <v-flex class="col_cart_adj" lg1 sm1 xs1>
                      <div class="correction_c">
                         <v-btn class="cor_count" slot="append"
                           @click="addCart(i.id, i.title, i.price, i.f_img, i.stock, count = i.count +1, resetCount=true)"> <v-icon class="cor_count_icon" color="red">mdi-plus</v-icon>
                          </v-btn>
                        <p class="count_text">{{i.count}}</p>
                          <v-btn class="cor_count" slot="prepend" :disabled="i.count<=0"
                           @click="addCart(i.id, i.title, i.price, i.f_img, i.stock, count = i.count -1, resetCount=true)"><v-icon  class="cor_count_icon" color="green">mdi-minus</v-icon>
                          </v-btn>
                          </div>
                    </v-flex>
                    <v-flex class="col_cart" lg2 md2 sm2 xs2> <v-text> Итого: {{i.price* i.count}}</v-text> </v-flex>
                </v-row>
              </v-flex>
          </v-row>
    </v-flex>
  </v-row>
</div>

  <div class="text-center not_media" v-else-if="!notItem && !showCart"><h2>Пока больше нет! Зайдите к нам позже.</h2></div>
  <div class="text-center load-button">
          <v-btn rounded color="primary" dark v-if="notItem && !showCart"  @click="getMedia()">Загрузить еще</v-btn>
          <v-btn rounded color="primary" dark v-else-if="!notItem && !showCart" @click="restartMedia()">Показать сначала</v-btn>
  </div>

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
            <div class="item" :style="{'background-image':'url('+'http://localhost:8000'+item.img+')'}"></div>
            </v-carousel-item>
          </v-carousel>
           </v-flex>

      </v-card>
    </v-dialog>
  </v-row>

  </div>
<div class="float_bt_panel" v-if="totalPrice">
<div class="float_status">
            <v-btn @click="order_w=!order_w" class="ma-2" color="primary" dark>Оформить заказ
                <v-icon dark right>mdi-checkbox-marked-circle</v-icon>
            </v-btn>

            <v-btn @click="clearCart" class="ma-2" color="red" dark>Очистить корзину
              <v-icon dark right>mdi-cancel</v-icon>
            </v-btn>
</div>
</div>
<v-dialog  v-model="order_w">
  <v-flex class="order_w" lg6 offset-lg3>
<v-form ref="form" v-model="valid" lazy-validation v-if="!sendingOrder">
        <v-select
        class="content_in_form"
            :items="items"
            v-model="selectDelivery"

            v-on:change="deliverySelect()"
            label="Выбрать доставку"
            required
    ></v-select>

    <v-text-field
    class="content_in_form"
      v-model="name"
      :counter="10"
      :rules="nameRules"
      label="Как к вам обращаться?"
      required
    ></v-text-field>
    <p class="content_in_form"  v-if="showDeliveryInfo">
      Заказ будет доставлен завтра.
    </p>
    <v-text-field
      v-if="showDeliveryInfo"
      class="content_in_form"
      v-model="adressDelivery"
      :counter="100"
      label="Адрес доставки"
      required
    ></v-text-field>
    <p class="content_in_form"  v-if="indexInputField">
      Заказ будет отправлен в течении 3-ех дней, стоимость доставки будет рассчитана менеджером, после чего детали согласуются с Вами.
    </p>
    <v-text-field
      v-if="indexInputField"
      class="content_in_form"
      v-model="adressDelivery"
      :counter="100"
      label="Адрес доставки и ИНДЕКС"
      required
    ></v-text-field>
    <vue-tel-input v-model="value" placeholder='Контактный номер пожалуйста'
    :rules="rulesPhone"
    v-bind="bindProps"
    class="content_in_form"
    ref="phone"
    >
    </vue-tel-input>
    <p class="error"
    v-if="errorPhone ===true"
    >Пожалуйста заполните поле</p>
    <v-spacer></v-spacer>
    <div class="sum_order_float">
      <p>Сумма заказа {{totalPrice}}руб. + доставка.</p>
    </div>
<div class="space_bottom"></div>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate()"
      style="float: right;"
    >
        Заказать
    </v-btn>

  </v-form>
</v-flex>
    </v-dialog>
  <v-dialog  v-model="orderSuccess">
      <v-flex class="order_s" lg6 offset-lg3>
        <div class="order_success">
          <h3>Заказ принят в обработку. Скоро мы с вами свяжемся.</h3>
          <h5>№ Вашего заказа <span>{{numberOrder}}</span></h5>
        </div>
      </v-flex>
  </v-dialog>

  <v-dialog v-model="orderNotSuccess">
      <v-flex class="order_s" lg6 offset-lg3>
        <div class="order_not_success">
          <h3>Что то пошло не так, заказ не принят!</h3>
          <h4>Попробуйте оформить еще раз.</h4>
        </div>
      </v-flex>
  </v-dialog>


</div>
</template>

<script>
import { HTTP } from '../common';
import { VueTelInput } from 'vue-tel-input';

export default {
  data () {
    return {
      orderNotSuccess:false,
      numberOrder:null,
      orderSuccess:false,
      orderState:null,
      order_w: false,
      showCart:false,
      totalPrice:null,
      totalBy:null,
      cart: new Array,
      search_val:'',
      select:null,
      carHeight:500,
      dopmedia:[],
      dialog: false,
      notItem:true,
      parts:[],
      stepPage:9,
      starPage:0,
      endPage:9,
      show: null, //show full cart
      category:[],
      cartTotal:0,
      elKey:0,
      deliveryS:null,
//order form
      adressDelivery:null,
      showDeliveryInfo:false,
      indexInputField:false,
      selectDelivery:null,
      items: [
        'Заберу сам',
        'Доставка по Санкт-Петербургу',
        'Доставка в регион'
      ],
      bindProps:{
        onlyCountries:['RU'],
        defaultCountry: "RU",
        required: true,
        autocomplete: "on",
        name: "telephone",
        maxLen: 11,
        wrapperClasses: "wrap_phone",
        inputClasses: "input_phone",
        validCharactersOnly:'true'
        },
        errorPhone:false,
        countryCode: null,
        valid:false,
        name: '',
        nameRules: [
          v => !!v || 'Поле c именем нужно заполнить',
          v => (/^[А-ЯЁ][а-яё]+$/.test(v)) || 'Имя в формате: "Александр" ',
        ],
        rulesPhone:[
            v => !!v || 'Номер обязательно',
            v => (v&& v.lenght <= 10)
        ],
    }
  },
    components: {
    VueTelInput,
  },
  methods: {
    sendOrder(){
          HTTP.post('/shop_order/', {
            params: { cart:this.cart, adress:this.adressDelivery, type_delivery:this.deliveryS, name:this.name, total_price:this.totalPrice, phone:this.$refs.phone.phone,
                tp:this.totalPrice}
                  }).then(response => {
                    this.orderState = response.data.status;
                    this.numberOrder = response.data.id;
                      if (this.orderState == "ok"){
                          this.order_w=false;
                          this.orderSuccess=true;
                          this.clearCart();
                      }else{
                          this.order_w=false;
                          this.orderNotSuccess=true;
                      }
            })
    },
    deliverySelect(){
      if(this.selectDelivery=='Доставка по Санкт-Петербургу'){
        this.deliveryS=0;
        this.indexInputField =false;
        this.showDeliveryInfo = true;
      }else if(this.selectDelivery=='Доставка в регион'){
        this.deliveryS=1;
        this.showDeliveryInfo=false;
        this.indexInputField = true;
      }else{
        this.deliveryS=2;
        this.indexInputField =false;
        this.showDeliveryInfo=false;
      }
    },
      countrySelected(val) {
        this.countryCode = val.dialCode;
        },
      validate () {
        if (this.$refs.form.validate() ===true){
            if(this.$refs.phone.phone.length >16){
              this.errorPhone =false;
              this.sendingOrder = true;
              this.sendOrder();
            }else{
                this.errorPhone =true;
            }
        }
      },
      reset () {
        this.$refs.form.reset()
      },
      resetValidation () {
        this.$refs.form.resetValidation()
      },
    clearCart(){
      this.cart= new Array;
      this.showCart=false;
      this.totalPrice=0;
      this.totalBy=null;
    },
    addCart(id, title, price, img, stock, count=1, resetCount=false){
      let addCount = true;
      if(this.cart.length >0 ){
      for( let key in this.cart){
        if (this.cart[key]['title'] == title){
            addCount = false;
            if (resetCount==false){
            this.cart[key]['count'] = this.cart[key]['count'] + 1;
            }else{
              this.cart[key]['count'] = count;
            }
        }
      }}
      if(addCount == true){
        this.cart.push({'id':id, 'title':title, 'price':price, 'img':String(img), 'stock':stock, 'count':count, });
        }
      this.totalPrice = 0;
      this.totalBy = this.cart.length
      for( let key in this.cart){
          this.totalPrice = this.totalPrice +(this.cart[key]['price'] * this.cart[key]['count'])
      }
    },
    preSetCart(){
          if (localStorage.getItem('cart')) {
              let cartCach = JSON.parse(localStorage.getItem('cart'));
              for(var key in cartCach){
                this.addCart(cartCach[key]['id'],cartCach[key]['title'],cartCach[key]['price'],cartCach[key]['img'],cartCach[key]['stock'],cartCach[key]['count'])
            }
        }
    },
    restartMedia(){
        this.search_val=null;
        this.notItem=true;
        this.starPage=0;
        this.endPage=9;
        this.setInitData();
    },
    getMedia(){
      this.starPage = this.starPage + this.stepPage;
      this.endPage = this.endPage + this.stepPage;
      this.setInitData();
    },
    showId(id){
      if (id !=this.show){
      this.show = id;
      }else{
        this.show = null;
      }
    },
    setSearching(){
      if (this.search_val.length>=3){
          this.setInitData();
      }else if (this.search_val.length<3){
          this.restartMedia();
      }
    },
    setInitData(){
       HTTP.get('/shop_categoty/').then(response => {
                     for (var item in response.data){
                       this.category.push(response.data[item].title)
                     }
                 })
      HTTP.post('/shop_parts/', {
            params: {
                start:this.starPage,
                end:this.endPage,
                category:this.select,
                search:this.search_val
            }
        }).then(response => {
                  if(response.data.length==0){
                        this.notItem = false;
                      }else{
                      this.media = response.data
                      for(var i in  response.data ){
                          response.data[i]['f_img'] = 'http://127.0.0.1:8000'+response.data[i]['f_img']
                        }
                        this.parts = response.data;
                      }
        })
    },
    addImgsForParts(id){
          HTTP.post('/shop_parts_img/', {
            params: { id:id}
              }).then(response => {
                this.dopmedia = response.data;
        })
        setTimeout(() => this.dialog=true, 100);

  },
    scrollToBlock () {
      var el = this.$route.params.id
      document.getElementById(el).scrollIntoView()
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
      } else {
        setTimeout(() => this.afteRenderUpdate(), 100)
      }
    }
  },
    watch: {
    totalPrice() {
      const parsed = JSON.stringify(this.cart);
      localStorage.setItem('cart', parsed);
    }
  },
  created: function () {
    this.afteRenderUpdate()
  },
    mounted(){
      this.setInitData();
      this.preSetCart();
  }
}
</script>

<style scoped>
body{
  overflow:hidden;
  overflow-y:hidden;  /*для вертикального*/
  overflow-x:hidden;  /*для горизонтального*/
}
.order_s{
  background-color: transparent;
}
.order_not_success{
  background-color: black;
  padding: 25px;
}
.order_not_success h3{
  color: red;
  font-size: 1.6rem;
}
.order_success{
  padding: 25px;
  background-color: black;
  color: green;
  font-size: 1.6rem;
}
.sum_order_float{
  margin-top:15px;
  margin-bottom: 15px;
  text-align: centre;
}
.space_bottom{
  margin-top:30px;
  margin-bottom: 50px;
}
.order_w{
  background-color: white;
  max-width: 50%;
  padding:50px;
}
.back_sale{
  float: right;
  cursor: pointer;
}
.float_bt_panel{
    width: 100%;
    text-align: center;
    background-color: #000000cf;
    position: fixed;
    bottom: 0;
}
.cart_status_info{
  margin-top: 100px;
}
.cart_status_info h4{
  margin-top: 10px;
}
.separait_row{
  border-bottom: 1px solid grey;
  margin-bottom: 20px;
}
.count_text{
  margin-top: 10px;
  margin-bottom: 10px;
}
.col_cart_adj{
  text-align: center;
  margin-top:15px;
}
.col_cart_img{
  padding:10px;
}
.col_cart{
  text-align: center;
  padding: 30px 0% 0% 5%;
}
.cor_count{
  min-width: 15px !important;
  height: 15px !important;
  padding: 10px !important;
}
.cor_count_icon{
  position: absolute !important;
}
.cart_status_info h4{
  font-family: 'Roboto', sans-serif;
  font-size: 1.4rem;
}
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
.not_media{
  margin-top:100px;
  text-align: center;
  font-size: 1.8rem;
}
.img_parts{
  height: 250px;
  background-size: contain;
  background-position: center;
}
.load-button{
  margin-top: 50px;
  margin-bottom: 50px;
}
.add_shop{
  background-color: #1640a2;
  color: white;
}
.v-card__text{
  position: absolute;
  z-index: 9999;
  background-color: white;
  border: 0px gray;
}
.cart_product{
  margin-top:40px;
}
.row_cart p{
  font-family: 'Roboto', sans-serif;
  font-size: 16px;
  color: #fff;
  margin-left: 10px;
}
.row_cart{
  padding-top: 15px;
}
.selected_category{
  height: 25px;
}
.selected_category label{
  text-align: center;
}
@media (max-width: 600px) {
.col_cart{
  padding: 50px 0% 0% 5px;
}
.row_cart_one{
  margin-left: 40px;
  margin-right: 40px;
}
.cart_status_info{
  margin-top: 50px;
}
}
@media (min-width: 600px) and (max-width:960px){
.col_cart{
  padding: 50px 0% 0% 5px;
}
.row_cart_one{
  margin-left: 40px;
  margin-right: 40px;
}
.cart_status_info{
  margin-top: 50px;
}
}
@media (min-width: 960px) and (max-width:1264px){
.row_cart_one{
  margin-left: 40px;
  margin-right: 40px;
}
}
</style>

