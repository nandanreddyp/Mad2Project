<template>
    <appHeader/>
    <div class="main">
        <div class="welcome-background" :style="{ 'background-image': 'url(' + require('@/assets/background/books.jpg') + ')' }">
        </div>
        <div class="welcome-foreground">
            <router-view />
        </div>
    </div>
</template>

<script>
import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

import appHeader from '@/components/layout/header.vue'

export default {
    components: {
        appHeader
    },
    mounted() {
        if (this.$route.query.logout) {
                    toast.success(`Logged out successfully!`,{autoClose: 6000,})    
        }
        if (this.$route.query.login) {
                    toast.warn(`Please login to access!`,{autoClose: 6000,})    
        }
    },
    watch: {
        $route(to, from) {
            if (this.$route.query) {
                if (this.$route.query.found === 'true') {
                    toast.info(`Account found!\nPlease login to continue`,{autoClose: 6000,})
                } else if (this.$route.query.found === 'false') {
                    toast.info(`Account not found!\nPlease register to create`,{autoClose: 6000,})
                }
                if (this.$route.query.exists === 'true') {
                    toast.error(`Account already exists!\nLogin to continue`,{autoClose: 6000,})
                } else if (this.$route.query.exists === 'false') {
                    toast.success(`Account created!\nPlease login to continue`,{autoClose: 6000,})             
                }
            }
        }
    }
}
</script>

<style scoped>
.main {
    position: relative;
    background-color: aquamarine;
    flex: 1;
    display: flex; flex-direction: column;
}
.welcome-background {
    background-size: cover; background-repeat: no-repeat; background-position: center;
    flex: 1; filter: blur(3px);
}
.welcome-foreground {
    width: 100%; height: 100%;
    position: absolute; overflow: auto;
    display: flex; justify-content: center;
    scrollbar-width: thin;
}
</style>