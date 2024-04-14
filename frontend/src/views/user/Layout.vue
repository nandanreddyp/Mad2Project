<template>
    <appHeader/>
    <div class="main">
        <appSidebar v-if="this.$store.state.showSideBar" />
        <div class="content">
            <router-view />
        </div>
    </div>
</template>

<script>
import appHeader from '@/components/layout/header.vue'
import appSidebar from '@/components/layout/sidebar.vue'
export default {
    components: {
        appHeader, appSidebar
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
}
</style>