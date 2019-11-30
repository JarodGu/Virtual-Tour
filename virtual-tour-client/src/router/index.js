import Vue from 'vue';
import VueRouter from 'vue-router';
import Home from '../views/Home.vue';
import Tour from '../views/Tour.vue';

Vue.use(VueRouter);

const routes = [
    {
        path: '/',
        name: 'home',
        component: Home
    },
    {
        path: '/tour/:id',
        name: 'tour',
        component: Tour
    }
];

const router = new VueRouter({
    mode: 'history',
    base: process.env.BASE_URL,
    routes
});

export default router;
