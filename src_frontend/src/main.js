// Import Vue
import Vue from 'vue';
import Vuex from 'vuex';
import VueRouter from 'vue-router';
import Vuetify from 'vuetify';

// Import Vue App, routes, store
import App from './App';
import routes from './routes';
// import store from './store';

import 'vuetify/dist/vuetify.min.css'
import "./styles/main.scss";

Vue.use(VueRouter);
Vue.use(Vuetify)
Vue.use(Vuex);

// Configure router
const router = new VueRouter({
    routes,
    linkActiveClass: 'active',
    mode: 'history'
});

new Vue({
    el: '#app',
    render: h => h(App),
    router,
    // store,
});
