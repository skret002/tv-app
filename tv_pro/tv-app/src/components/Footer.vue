<template>
  <v-footer dark padless class="footer_block" >
    <v-card flat tile class="footer  lighten-1 white--text text-center">
      <v-card-text>
        <v-btn v-for="icon in icons" :key="icon" class="mx-4 white--text" icon>
          <a class="links_icon" :href="icon[1]"> <v-icon size="24px">{{ icon[0] }}</v-icon></a>
        </v-btn>
      </v-card-text>
      <v-divider class="hidden-md-and-down" ></v-divider>
<v-lazy
  v-model="isActive"
  :options="{
    threshold: .2
  }"
  min-height="200"
  transition="expand-x-transition"
>
<v-row>
    <v-flex lg4 md4 sm10 xs10
    offset-sm1
    offset-xs1
     offset-md0
    >
    <v-card class="mx-auto footer_list_contact " max-width="90%" tile>
      <v-list
      class="footer_list_contact"
        :disabled="disabled"
        :dense="dense"
        :two-line="twoLine"
        :shaped="shaped"
        :flat="flat"
        :subheader="subheader"
        :sub-group="subGroup"
        :nav="nav"
        :avatar="avatar"
        :rounded="rounded"
      >
        <v-list-item-group v-model="item" color="primary">
          <v-list-item
            v-for="(item, i) in items"
            :key="i"
            :inactive="inactive"
          >
            <v-list-item-avatar v-if="avatar">
              <v-img :src="item.avatar"></v-img>
            </v-list-item-avatar>
            <v-list-item-content>
              <v-list-item-title v-html="item.title"></v-list-item-title>
              <v-list-item-subtitle v-if="twoLine || threeLine" v-html="item.subtitle"></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-card>
    <v-divider class="divider  hidden-md-and-up" ></v-divider>
    </v-flex>
    <v-flex  lg4 md4 sm10 xs10
        offset-sm1
        offset-xs1
        offset-md0
        >
        <v-card-text class="white--text pt-0 footer_center " >
        <div v-html="content_in_center"></div>
        <v-flex lg10 offset-lg1>
            <img :src="logo"
            style="width:100px; height:auto;"
            alt="логотип">
        </v-flex>
      </v-card-text>
    </v-flex>
    <v-divider class="divider hidden-md-and-up" ></v-divider>
    <v-flex lg4 md4 sm12 xs12>
        <v-row align="center">
            <v-col cols="8"
            offset="2">
            <v-select
                id="sale"
                v-on:change="selectSale()"
                v-model="select_sale"
                :items="keys_sale"
                :menu-props="{ top: false, offsetY: false }"
                label="Выбрать акцию"
            ></v-select>
            <div class="content_sale"  v-html="content_sale">
            </div>
            </v-col>
        </v-row>
    </v-flex>
</v-row>
</v-lazy>

      <v-divider></v-divider>

      <v-card-text class="white--text">
       {{ new Date().getFullYear() }} — <strong>Название сайта</strong>
      </v-card-text>
    </v-card>
  </v-footer>
</template>



<script>
import '@fortawesome/fontawesome-free/css/all.css';
import '@fortawesome/fontawesome-free/js/all.js';
export default {
  data () {
    return {
        isActive: false,
        select_sale:null,
        content_sale:'<div class="not_select_sale"><h3 style="font-size:1.6rem">Скидки до </h3><h2 style="font-size:1.8rem; color:red">20%</h2><h3 style="font-size:1.6rem"> выбирайте! </h3></div>',
        keys_sale:[],
        item: [],
        logo:null,
        content_in_center:null,
        items: [],
        disabled: false,
        dense: false,
        twoLine: true,
        threeLine: false,
        shaped: false,
        flat: true,
        subheader: false,
        inactive: true,
        subGroup: false,
        nav: true,
        avatar: true,
        rounded: false,
        icons: [
        ['fab fa-vk', 'https://vk.com/allservicesspb'],
        ['fab fa-whatsapp','https://wa.me/+79219032885?text=Здравствуйте' ],
        ['fab fa-viber', ' viber://forward?text=+79219032885'],
        ['fab fa-yandex', ' https://yandex.ru/profile/182308908187?lr=2'],
        ]
  }
},
methods:{
        content: function(){
            var cont = this.$store.state.footer["center_info"][0];
            this.content_in_center = cont.content;
            this.logo = 'http://localhost:8000' +cont.logo;
        },
        staff: function () {
            var st = this.$store.state.footer["staff"];
            for (var key in st) {
                this.items.push({
                        avatar: 'http://localhost:8000' +st[key].avatar,
                        title: st[key].name +' - ' + st[key].phone_number,
                        subtitle:st[key].area
                });
            }
    },
    setSale: function (){
        var sale=this.$store.state.footer["sale"];
        for (var key in sale) {
            this.keys_sale.push(sale[key].name_sale)
        }
    },
    selectSale(){
        var sale=this.$store.state.footer["sale"];
        for (var key in sale) {
            if (sale[key].name_sale === this.select_sale){
                this.content_sale ='<div class="select_sale"><h3 style="font-size:1.8rem; color:red">Условие:</h3> <p>'+sale[key].description_sale+'</p><h4>Скидка</h4><h2>' +
                                                    sale[key].size_sale +'%' +'</h2></div>'
            }
        }

    }
},
created () {
  this.$store.dispatch('GET_STAFF').then(() => {this.staff();});
  this.$store.dispatch('GET_CONTENT_FOOTER').then(() => { this.content(); });
  this.$store.dispatch('GET_SALE').then(() => { this.setSale(); });

},
}
</script>

<style>
.footer_block{
    margin-top: 15px;
}
.divider{
    margin-bottom: 25px;
    width: 90%;
}
.not_select_sale, .not_select_sale h3, .not_select_sale h2, .not_select_sale p{
    font-family: 'Roboto', sans-serif;
    font-size: 5rem;
}
.footer_list_contact{
    background-color: transparent !important;
    box-shadow: none !important;
}
.footer{
    background-color: #212121 !important;
}
.links_icon{
    color: white !important;
}
.footer_center{
    margin-top: 25px;
    }
</style>