<template>
    <appHeader />
    <div class="main">
        <appSidebar v-if="this.$store.state.showSideBar"/>
        <div class="content">
            <router-view />
        </div>
    </div>
</template>

<script>
import { mapGetters, mapState } from 'vuex';

import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

import appHeader from '@/components/layout/header.vue'
import appSidebar from '@/components/layout/sidebar.vue'
export default {
    components: {
        appHeader, appSidebar,
    },
    data() {return{

    }},
    mounted() {
        if (this.$route.query.msg === 'access denied') {
            toast.error(`Access denied:\nYou don't have access!`,{autoClose: 6000,})
        }
        if (this.$route.query.login === 'success') {
            toast.success(`Hey, ${this.user.f_name}.\nWelcome back!`,{autoClose: 6000,})
        }
    },
    computed: {
        ...mapState(['user'])
    }
}
</script>

<style scoped>
.main {
    height: calc(100% - 50px);
    display: flex;
}
.content {
    flex: 1;
    display: flex; flex-direction: column;
    overflow: auto;
}
</style>