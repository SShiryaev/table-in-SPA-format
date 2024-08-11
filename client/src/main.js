import '@/assets/scss/index.scss';

import axios from 'axios';
import VueAxios from 'vue-axios'

import { createApp } from 'vue';
import App from './App.vue';

const app = createApp(App);
app.use(VueAxios, axios);
app.provide('axios', app.config.globalProperties.axios);

app.mount('#app');
