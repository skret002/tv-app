(window["webpackJsonp"]=window["webpackJsonp"]||[]).push([["chunk-5a2246fd"],{3408:function(t,e,s){},8212:function(t,e,s){"use strict";s("a9e3");var a=s("5530"),o=(s("3408"),s("a9ad")),i=s("24b2"),n=s("a236"),r=s("80d2"),l=s("58df");e["a"]=Object(l["a"])(o["a"],i["a"],n["a"]).extend({name:"v-avatar",props:{left:Boolean,right:Boolean,size:{type:[Number,String],default:48}},computed:{classes:function(){return Object(a["a"])({"v-avatar--left":this.left,"v-avatar--right":this.right},this.roundedClasses)},styles:function(){return Object(a["a"])({height:Object(r["f"])(this.size),minWidth:Object(r["f"])(this.size),width:Object(r["f"])(this.size)},this.measurableStyles)}},render:function(t){var e={staticClass:"v-avatar",class:this.classes,style:this.styles,on:this.$listeners};return t("div",this.setBackgroundColor(this.color,e),this.$slots.default)}})},a6e8:function(t,e,s){"use strict";var a=s("e9fc"),o=s.n(a);o.a},e78f:function(t,e,s){"use strict";s.r(e);var a=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("v-flex",{staticClass:"staff",attrs:{id:"staff",lg10:"",xl10:"",md10:"",sm10:"",xs10:"","offset-lg1":"","offset-xl1":"","offset-md1":"","offset-sm1":"","offset-xs1":""}},[s("v-row",t._l(t.staff,(function(e,a){return s("v-flex",{key:a,staticClass:"item_staff",attrs:{md4:""}},[s("v-card",{staticStyle:{height:"400px","overflow-y":"auto"},attrs:{dark:""}},[s("div",{staticClass:"d-flex flex-no-wrap justify-space-between"},[s("div",[s("v-card-title",{staticClass:"headline",domProps:{textContent:t._s(e.name)}}),s("v-card-subtitle",{domProps:{textContent:t._s("Должность: "+e.position)}})],1),s("v-avatar",{staticClass:"ma-3",attrs:{size:"125",tile:""}},[s("v-img",{attrs:{src:"http://localhost:8000"+e.avatar}})],1)],1),s("v-card-text",{domProps:{innerHTML:t._s(e.text)}})],1)],1)})),1)],1),s("v-flex",{staticClass:"about_company",attrs:{id:"about_company",lg6:"",xl6:"",md8:"",sm10:"",xs10:"","offset-lg3":"","offset-xl3":"","offset-md2":"","offset-sm1":"","offset-xs1":""}},[t.staff[0].video.video?s("div",{attrs:{id:"player-overlay"}},[s("video",{attrs:{controls:""}},[s("source",{attrs:{src:"http://localhost:8000"+t.staff[0].video.video,type:"video/webm"}})])]):s("div",{staticClass:"not_video",attrs:{id:"about_company"}},[s("h1",[t._v("Видео еще не загружено, но мы над этим работаем!")])])])],1)},o=[],i=s("69d9"),n={data:function(){return{staff:null}},methods:{scrollToBlock:function(){var t=this,e=this.$route.params.id;try{document.getElementById(e).scrollIntoView({block:"center",behavior:"smooth"})}catch(s){setTimeout((function(){return t.scrollToBlock()}),200)}},getStaff:function(){var t=this;i["a"].get("/staff/").then((function(e){t.staff=e.data}))},afteRenderUpdate:function(){var t=this,e=document.getElementById("topPanel");if(window.screen.width>736){var s=document.getElementById("float_panel");e?(e.style.backgroundColor="black",e.style.position="static",s.style.marginBottom="50px",this.getStaff(),setTimeout((function(){return t.scrollToBlock()}),300)):setTimeout((function(){return t.afteRenderUpdate()}),100)}else window.screen.width<=736&&e?(e.style.backgroundColor="black",e.style.position="static",e.style.height="100px",document.getElementById("body").scrollIntoView({behavior:"smooth"}),this.getStaff()):setTimeout((function(){return t.afteRenderUpdate()}),100)}},created:function(){this.afteRenderUpdate()}},r=n,l=(s("a6e8"),s("2877")),f=s("6544"),c=s.n(f),d=s("8212"),u=s("b0af"),h=s("99d9"),v=s("0e8f"),m=s("adda"),p=s("0fd9"),b=Object(l["a"])(r,a,o,!1,null,"5bf27b52",null);e["default"]=b.exports;c()(b,{VAvatar:d["a"],VCard:u["a"],VCardSubtitle:h["b"],VCardText:h["c"],VCardTitle:h["d"],VFlex:v["a"],VImg:m["a"],VRow:p["a"]})},e9fc:function(t,e,s){}}]);
//# sourceMappingURL=chunk-5a2246fd.f2c9e22e.js.map