
import { createRouter, createWebHistory } from 'vue-router';
import BookPage from '../components/BookPage.vue';
import Questionnaire from '../components/Questionnaire.vue';


const routes = [
  {
    path: '/',
    name: 'Questionnaire',
    component: Questionnaire
  },
  {
    path: '/book/:id',
    name: 'BookPage',
    component: BookPage,
    props: true
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
})



export default router;
