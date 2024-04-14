<template>
    <!--vif isAuthenticated-->
    <header v-if="isAuthenticated" :class="{'librarian' : (user.role === 'librarian')}">
        <div id="header-start">
            <svg id="menu-logo" @click="toggleSideBar" fill="none" height="24" viewBox="0 0 24 24" width="24" xmlns="http://www.w3.org/2000/svg">
                <path d="M4 6H20M4 12H20M4 18H20" stroke="#4A5568" stroke-linecap="round" stroke-linejoin="round" stroke-width="2"/>
            </svg>
            <a href="/"><img id="logo" src="@/assets/logos/DarkModeLogo.png" alt=""></a>
        </div>
        <div id="header-center">
            <form class="main-header-search" @submit.prevent="" >
                <input placeholder="Search" type="search" id="search-input">
                <button id="search-button">
                    <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="20" height="20" viewBox="0 0 50 50">
                        <path d="M 21 3 C 11.621094 3 4 10.621094 4 20 C 4 29.378906 11.621094 37 21 37 C 24.710938 37 28.140625 35.804688 30.9375 33.78125 L 44.09375 46.90625 L 46.90625 44.09375 L 33.90625 31.0625 C 36.460938 28.085938 38 24.222656 38 20 C 38 10.621094 30.378906 3 21 3 Z M 21 5 C 29.296875 5 36 11.703125 36 20 C 36 28.296875 29.296875 35 21 35 C 12.703125 35 6 28.296875 6 20 C 6 11.703125 12.703125 5 21 5 Z"></path>
                    </svg>
                </button>
            </form>
        </div>
        <div id="header-end">
            <img id="user-logo" :src="user.img_path" alt="">
            <svg @click="toggleLogout" width="25px" height="25px" style="background-color: white; border-radius: 50px; cursor: pointer;" viewBox="0 0 24 24" fill="none" xmlns="http://www.w3.org/2000/svg">
                <g id="SVGRepo_bgCarrier" stroke-width="0"/>
                <g id="SVGRepo_tracerCarrier" stroke-linecap="round" stroke-linejoin="round"/>
                <g id="SVGRepo_iconCarrier"> <path d="M10 12H20M20 12L17 9M20 12L17 15" stroke="#fa0000" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/> <path d="M4 12C4 7.58172 7.58172 4 12 4M12 20C9.47362 20 7.22075 18.8289 5.75463 17" stroke="#fa0000" stroke-width="1.5" stroke-linecap="round"/> </g>
            </svg>
        </div>
    </header>
    <!--vif not isAuthenticated-->
    <header v-else>
        <a href="/">
            <img id="logo" src="@/assets/logos/DarkModeLogo.png" alt="">
        </a>
        <nav>
            <router-link :to="{name:'login'}" v-if="$route.path !== '/login'">Login</router-link>
            <router-link :to="{name:'register'}" v-if="$route.path !== '/register'">Register</router-link>
        </nav>
    </header>
    <!--vif logout-->
    <logoutComp v-if="logout" :toggleLogout="toggleLogout"/>
</template>
<script>
import { mapGetters, mapState } from 'vuex';
import logoutComp from "@/components/layout/logout.vue"
export default {
    data(){return {
        logout : false,
    }},
    methods: {
        toggleLogout() {
            this.logout = !this.logout
        },
        toggleSideBar() {
            this.$store.commit('toggleSideBar')
        }
    },
    computed: {
        ...mapGetters(['isAuthenticated','user']),
        ...mapState(['user'])
    },
    components: {
        logoutComp
    }
}
</script>
<style scoped>
.librarian {
    background-color: grey;
}
a {
    -webkit-user-drag: none;
}
header {
    display: flex; align-items: center; justify-content: space-between;
    height: 50px; padding: 20px;
    background-color: #9b864e;
    overflow: hidden;
}

/* start */
#header-start {
    display: flex; align-items: center; gap: 6px;
}
#menu-logo {
    cursor: ew-resize;
}
img#logo {
    width: 120px;
    user-select: none; -webkit-user-drag: none;
}

/* center */
#header-center {
    flex: 1;
    display: flex; justify-content: center;
}
.main-header-search {
    display: flex; width: 50%;
    align-items: center;
    background-color: white; border-radius: 25px;
}
#search-input {
    flex: 1;
    padding: 10px;
    border: none;
    border-radius: 25px;
    outline: none;
}
#search-button {
    border: none;
    outline: none;
    border-top-right-radius: 25px;
    border-bottom-right-radius: 25px;
    padding: 0px 10px 0px 0px;
    cursor: pointer;
}


/* end */
#header-end {
    display: flex; align-items: center; gap: 6px;
}
#user-logo {
    width: 40px; height: 40px;
    object-fit: cover;
    border-radius: 50px;
    -webkit-user-drag: none;
}
#user-logo:hover {
    border: 3px solid black;
    cursor: pointer;
}

/* welcome header stylings */
nav {
    width: 50%;
    display: flex; justify-content: space-evenly;
}
nav a {
    display: inline-block; flex: 0.1;
    color: white; background-color: red;
    padding: 5px; border-radius: 4px;
    text-decoration: none;
    transition: background-color 0.3s;
    text-align: center;
}
nav a:active {
    background-color: rgb(70, 0, 0);
    transform: translate(1px)
}

</style>