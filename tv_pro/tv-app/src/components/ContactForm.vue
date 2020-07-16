<template>
<v-container id="order">
<v-flex md5 lg4>
    <div class="section-heading  text-left default">
        <h2 class="section-title">Оставьте заявку сейчас</h2>
    <div class="sep-element">
    </div>
    </div>
    <div class="space"></div>
</v-flex>
<v-lazy
        v-model="isActive"
        :options="{
          threshold: .3
        }"
        min-height="500"
        transition="expand-x-transition"
      >
<div class="row">
    <v-flex md6 xs12>
        <div class="square ">
            <div class="pix-item-review pix-text-review-left">
                <div class="pix-overlay pix-color"></div>
                <div class="pix-block-content row">
                    <v-flex md2 sm1 offset-md0 offset-sm1 class="hidden-xs-only">
                    <div class="round pix-icon-m pix-icon-color  ">
                        <div class="icon">
                            <span class="material-icons">commute</span>
                                </div>
                    </div>
                    </v-flex>
                    <v-flex md8 sm8 offset-sm1 offset-md1>
                    <div class="block_text"> <h4>Доставить самим или заказать доставку?</h4><p>Наш сервис расположен не далеко от метро "Беговая".
                        Вы можете легко добраться до нас на метро или наземным транспортом. Если Вы не можете самостоятельно доставить аппарат в наш сервис,
                        мы рады предоставить Вам нашего курьера, просто оформите заявку выбрав удобное время.</p></div>
                    </v-flex>
                </div>
            </div>
        </div>
<div class="square ">
            <div class="pix-item-review pix-text-review-left">
                <div class="pix-overlay pix-color"></div>
                <div class="pix-block-content row">
                    <v-flex  md2 sm1 offset-md0 offset-sm1   class="hidden-xs-only">
                    <div class="round pix-icon-m pix-icon-color ">
                        <div class="icon">
                            <span class="material-icons">phone_in_talk</span>
                                </div>
                    </div>
                    </v-flex>
                    <v-flex md8 sm8 offset-sm1  offset-md1>
                    <div class="block_text">
                        <div class="text_style_block">
                            <p><strong> Понедельник - Пятница:</strong> c 11:00 до 20:00</p>
                            <p><strong> Суббота:</strong> c 12:00 до 18:00</p>
                            <p><strong> Воскресенье:</strong> Выходной</p>
                        </div>

                    </div>
                    </v-flex>
                </div>
            </div>
        </div>
<div class="square ">
            <div class="pix-item-review pix-text-review-left">
                <div class="pix-overlay pix-color"></div>
                <div class="pix-block-content row">
                    <v-flex  md2 sm1 offset-md0 offset-sm1  class="hidden-xs-only">
                    <div class="round pix-icon-m pix-icon-color ">
                        <div class="icon">
                            <span class="material-icons">pin_drop</span>
                                </div>
                    </div>
                    </v-flex>
                    <v-flex md8 offset-md1 sm8 offset-sm1 >
                    <div class="block_text">
                         <div class="text_style_block">
                             <p><strong> Адрес:</strong> Туристская ул., 18, корп. 1, Санкт-Петербург, Россия</p>
                            <p><strong> Телефон:</strong> 903-28-85</p>
                            <p><strong> WhatsApp:</strong> +7 (931)-331-29-64</p>
                            <p><strong> Email: :</strong> 79219032885@ya.ru</p>
                        </div>
                    </div>
                    </v-flex>
                </div>
            </div>
        </div>

    </v-flex>
<v-flex md5 offset-md0 lg5 offset-lg1 sm8 offset-sm2>
  <div class="flash_back"
  v-if="sendingOrder===true"
  >
  <h4>Ожидайте...</h4>
<v-progress-linear indeterminate color="cyan"></v-progress-linear>
  </div>
  <div class="order_ok"
  v-if="statusOrderOk===true"
  >
  <h4>Спасибо!</h4>
  <h5>Ваша заявка принята.</h5>
  <p>Мы свяжемся с Вами для уточнения деталий.</p>
  </div>
  <div class="order_have"
    v-if="statusOrderHave===true"
    >
    <h3>Заявка уже принята</h3>
    <h6>Скоро мы свяжемся с Вами.</h6>
  </div>
<div class="square"  v-if="showForm">

<v-form ref="form" v-model="valid" lazy-validation
 v-if="!sendingOrder"
>
        <v-select
        class="content_in_form"
            v-model="select"
            :items="items"
            v-on:change="openCart()"
            :rules="[v => !!v || 'Выбрать цель обращения']"
            label="Вызвать курьера | Получить консультацию"
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


<!-- Time-->
    <v-dialog
    class="content_in_form"
    ref="dialog"
    v-model="modal2"
    :return-value.sync="time"
    persistent
    width="300px"
    >
        <template v-slot:activator="{ on }">
          <v-text-field
            v-model="time"
            label="В какое время Вам позвонить?"
            prepend-icon="access_time"
            :rules="rulesTime"
            readonly
            v-on="on"
          ></v-text-field>
        </template>
        <v-time-picker
        class="mt-2"
          v-if="modal2"
          v-model="time"
            :fullWidth="false"
            :disabled="disabled"
            :readonly="readonly"
            :landscape="landscape"
            :ampm-in-title="ampmInTitle"
            :use-seconds="useSeconds"
            :format="format"
            :no-title="noTitle"
            :scrollable="scrollable"
        >
          <v-spacer></v-spacer>
          <v-btn text color="primary" @click="modal2 = false">Атмена</v-btn>
          <v-btn text color="primary" @click="$refs.dialog.save(time)">Готово </v-btn>
        </v-time-picker>
      </v-dialog>
<!-- END Time-->


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

<div class="space_bottom"></div>

    <v-btn
      :disabled="!valid"
      color="success"
      class="mr-4"
      @click="validate"
      style="float: right;"
    >
        ОТПРАВИТЬ ЗАЯВКУ
    </v-btn>

  </v-form>

</div>

</v-flex>
</div>
</v-lazy>
<!-- Modal cart -->
<div class="text-center" >
    <v-dialog hide-overlay
      v-model="dialog"
      fullscreen = true
    >

      <v-card class="pop_up_map">
        <v-card-title
          class="pop_up_map_title justify-center"
          primary-title
        >
          Стоимость доставки в сервис и обратно!
        </v-card-title>

        <v-card-text class="open_float_cart">
          <v-flex md10 lg10 xl10 xs10 offset-1 style="text-align: center">
          <div class="under_cart" ref="underMap" :style="{'font-size':mapFontSize}">
            Кликните по вашему району,
            <div class="square_red" :style="{'width':mapFontSize, 'height':mapFontSize}"></div>
            <div class="square_green" :style="{'width':mapFontSize, 'height':mapFontSize}"></div>
            <div class="square_el"  :style="{'width':mapFontSize, 'height':mapFontSize}"></div>
            для получения стоимости.
          </div>
          </v-flex>
            <iframe :style="{'margin-left':marginL}"
            src="https://yandex.ru/map-widget/v1/?um=constructor%3A946b9ce4385b97b02ac0961b210cdff63785d7b0ea78ba189a344f069693ef22&amp;source=constructor"
            :width="myWidth" :height="myHeight" frameborder="0"
            >
            </iframe>
        </v-card-text>

        <v-divider></v-divider>

        <v-card-actions>

          <v-spacer></v-spacer>
          <v-btn
            color="primary"
            text
            @click="dialog = false"
          >
            Я ознакомился | Закрыть
          </v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
</v-container>
</template>

<script>
import { VueTelInput } from 'vue-tel-input';
export default {
     data () {
    return {
    isActive: false,
    showForm:true,
    orderStatus:'',
    mapFontSize:'22px',
    statusOrderOk:false,
    statusOrderHave:false,
    sendingOrder:false,
    myWidth: window.innerWidth *0.8,
    myHeight:window.innerHeight   *0.7,
    marginL:(window.innerWidth - (window.innerWidth*0.8))*0.5 +'px',
    dialog: false,
    picker: null,
    disabled: false,
    readonly: false,
    landscape: false,
    ampmInTitle: false,
    useSeconds: false,
    format: 'pm',
    fullWidth: false,
    noTitle: false,
    scrollable: false,
    time: null,
    menu2: false,
    modal2: false,
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
       rulesTime:[
        v => (v&& v.lenght <= 2)
    ],
    select: null,
    items: [
      'Вызвать курьера',
      'Получить консультацию',
    ],
      checkbox: false,
      }
},
  components: {
    VueTelInput,
  },
    methods: {
      corectFloatCart(){
        if (window.innerWidth<=768&&window.innerWidth<window.innerHeight){
            this.myHeight = "400px";
            this.mapFontSize='16px';
        }
      },
      postOrder(){
        this.sendingOrder = false;
      },
        checkRespons(){
          if (this.orderStatus.length>0){
            return this.$store.getters.STATUS;
          }
          else if(this.$store.state.order.status.lenght >0){
            this.$store.state.order.status
          }
          else{
            return "true"
          }
        },
      sendOrder(){
        this.$store.dispatch('SEND_ORDER', {data:[{"type":this.select, "name": this.name, "time":this.time, "phone":this.$refs.phone.phone}]});
        setTimeout(function () { this.sendingOrder = false; }.bind(this), 2000);
        this.checkRespons();
        var status = this.checkRespons();
        setTimeout(function () {
        if (status == "true"){
          this.statusOrderOk = true;
          this.showForm=false;
        }else{
          this.statusOrderHave = true;
        }
        }.bind(this), 500);
      },
        openCart(){
            if (this.select =="Вызвать курьера"){
                this.dialog="true"
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
    },
    beforeDestroy() { window.removeEventListener('resize',  this.corectFloatCart());
    },
    created(){
      this.orderStatus =this.$store.getters.STATUS
    },
    mounted(){
       this.corectFloatCart();
    }
}
</script>

<style scoped>
.under_cart{
  text-align: center;
  font-family:'Fira Sans', sans-serif !important;
  display:inline-flex;
  margin-bottom: 30px;
}
.square_red, .square_green, .square_el{
  border-radius: 50px;
  margin-left:10px;
  margin-right:10px;
}
.square_red{
  background-color: red;
}
.square_green{
  background-color: green;
}
.square_el{
  background-color: yellow;
}
.v-dialog > .v-card > .v-card__title{
  font-family:'Fira Sans', sans-serif !important;
  font-size: 28px !important;
  text-align: center !important;
}
.pop_up_map_title{
  text-align: center;
  color:white;
  background-color: darkblue;
  font-family:'Fira Sans', sans-serif;
  font-size: 40px;
}
.order_ok, .order_have{
  color: whitesmoke;
  background-color: #205ccb;
  font-family:'Fira Sans', sans-serif;
  font-size: 24px;
  text-align: center;
  padding-top: 50%;
  width: 100%;
  position: relative;
  height: 100%;
}
.order_ok h4, .order_have h4{
  font-size: 48px;
}
.order_ok h5 , .order_have h5{
  font-size: 28px;
}
.order_ok h6 , .order_have h6{
  font-size: 22px;
}
.flash_back{
  color: #205ccb;
  font-family:'Fira Sans', sans-serif;
  font-size: 24px;
  text-align: center;
  padding-top: 50%;
  width: 100%;
  position: relative;
  height: 100%;
}
.flash_back h4 {
  margin-bottom: 40px;
}
.error{
  text-align: center;
  color: white;
  font-family:'Fira Sans', sans-serif;
  font-size: 18px;
  transition:0.5s;
}

.space_bottom{
  height: 50px;
}
.open_float_cart{
    margin-top:50px;
    padding-left: 0px !important;
}
.content_in_form{
    margin-top:30px;
}
.text_style_block p{
    margin-bottom: 5px;
}
.block_text h4{
    font-size: 20px;
    color: black;
    font-family:'Fira Sans', sans-serif;
}
.block_text{
    padding-top: 5px;
    margin-top: 0;
    line-height: 1.8;
    color: #797979;
    font-family:'Fira Sans', sans-serif;
}
.block_text strong{
    color: black;
}
.square {
    margin-left: 50px;
    margin-top: 50px;
}
.icon{
    margin-top: 15px;
    width: 90px;
    height: 90px;
    background: linear-gradient(to right, #2052c9,#21a5dd);
    border-radius: 180px;
    overflow: hidden;
}
.material-icons{
    font-size: 35px;
    color: white;
    margin: 27.5px;
}
.section-title{ margin-top: 50px; font-size: 2rem; }

@media (max-width: 1350px) and (min-width: 960px){
  .section-title{
    margin-top: 50px;
    font-size: 2rem;
  }
  .square {
    margin-left: 0px !important;
  }
}
@media (max-width: 960px) and (min-width: 640px){
  .section-title{
    margin-top: 50px !important;
    font-size: 2rem !important;
  }
}
@media (max-width: 640px) and (min-width: 320px)and (orientation:portrait) {
  .section-title{
    margin-top: 10px !important;
  }
  .order_ok, .order_have{
    padding-top: 5% !important;
    padding-bottom: 5% !important;
    height: auto !important;
  }
  .block_text{
    margin-left: 15px;
    margin-right: 15px;
  }
  .square{
    margin-left: 10px !important;
    margin-right: 10px !important;
  }

}
@media (max-width: 420px) and (min-width: 320px) {
.order_ok, .order_have h4{
  font-size: 26px;
}
.order_ok, .order_have h5{
  font-size: 4vh;
}
.order_ok, .order_have h5{
  font-size: 22px;
}
}
</style>