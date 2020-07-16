import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)
const routes = [

	{
		path: '',
		name: 'home',
		component: () => import('../components/DefaultHome'),
	},
	{
		path: '/malfunc/:id/',
		name: 'malfunc',
		component: () => import('../components/MalfuncContent'),
	},
	{
		path: '/staff/',
		name: 'staff',
		component: () => import('../components/Staff'),
  },
    {
    path: '/portfolio/',
    name: 'portfolio',
    component: () => import('../components/Portfolio'),
  },
{
    path: '/shop/',
    name: 'shop',
    component: () => import('../components/Shop'),
  },
];


const router = new VueRouter({
  mode: 'history',
  routes,

})

export default router
