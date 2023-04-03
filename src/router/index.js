import Vue from 'vue';
import VueRouter from 'vue-router';
import MainPage from '../components/MainPage.vue';
import About from '../components/About.vue';
import Questionnaire from '../components/Questionnaire.vue';

Vue.use(VueRouter);

const routes = [
  { path: '/', component: MainPage },
  { path: '/about', component: About },
  { path: '/contact', component: Questionnaire }
];

const router = new VueRouter({
  routes,
  mode: 'history'
});

export default router;
