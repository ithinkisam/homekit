// Import our custom CSS
import './scss/styles.scss'

// Import all of Bootstrap's JS
import * as bootstrap from 'bootstrap'

import { createApp } from 'vue'
import App from './App.vue'
// import router from './router'

const app = createApp(App)

// app.use(router)

app.mount('#app')
