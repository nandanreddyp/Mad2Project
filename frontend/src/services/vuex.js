import { createStore } from 'vuex'
import createPersistedState from 'vuex-persistedstate'

const store = createStore({
    state() {
        return {
            user: {
                
            },
            isAuthenticated: false,
            showSideBar: true
        }
    },
    mutations: {
        setUser(state, user) {
            state.user = { ...user }
        },
        setAuthentication(state, isAuthenticated) {
            state.isAuthenticated = isAuthenticated
        },
        removeUser(state){
            state.user = {},
            state.isAuthenticated = false,
            state.showSideBar = true
        },
        toggleSideBar(state){
            state.showSideBar = !state.showSideBar
        }
    },
    actions: {

    },
    getters: {
        isAuthenticated: state => state.isAuthenticated,
        user: state => state.user
    },
    plugins: [createPersistedState()]
})

export default store                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               