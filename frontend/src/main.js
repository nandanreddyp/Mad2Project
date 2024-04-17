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
    const hasToken = store.state.isAuthenticated;
    if (to.meta.requiresAuth) {
        const roles = to.meta.role || []
        if (!hasToken) { // unauthenticated
            if (to.fullPath !== '/') { return next({name:'welcome',query:{login:false}}) } // if not coming from main route then warn
            else { return next({name:"welcome"}) } // since coming from main route, just welcome to register
        } else if (roles.includes(store.state.user.role)) { // authorized continue
            return next()
        } else { // unauthorized redirecting to their homes
            if (store.state.user.role === 'librarian') {
                return next({name:'librarian-home'})
            } else {
                return next({name:'user-home',query:{msg:'access denied'}})
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
