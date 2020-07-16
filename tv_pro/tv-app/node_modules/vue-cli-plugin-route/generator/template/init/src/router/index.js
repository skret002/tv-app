import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = []

// eslint-disable-next-line no-new
const router = new VueRouter({
  <%_ if (history) { _%>
  mode: 'history',
  base: process.env.BASE_URL,
  <%_ } _%>
  routes
})

export default router
