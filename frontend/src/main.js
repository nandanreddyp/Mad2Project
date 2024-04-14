import { createApp } from 'vue'
import App from './App.vue'
import { createRouter, createWebHistory } from 'vue-router'
import Routes from './routes/index.js'
import store from './services/vuex.js'

const router = createRouter({
    history: createWebHistory(),
    routes: Routes
})

router.beforeEach((to, from, next) => {
    console.log(to)
    const hasToken = store.state.isAuthenticated;
    if (to.meta.requiresAuth) {
        const roles = to.meta.role || []
        if (!hasToken) {
            return next('/in')
        } else if (roles.includes(store.state.user.role)) {
            return next()
        } else {
            if (store.state.user.role === 'librarian') {
                return next('/librarian')
            } else {
                return next('/')
            }
        }
    } else {
        return next(); // Don't forget to call next() if the route doesn't require authentication
    }
})

const app = createApp(App)

app.use(router)
app.use(store)

app.mount('#app')
