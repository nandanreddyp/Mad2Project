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
import appHeader from '@/components/layout/header.vue'
export default {
    components: {
        appHeader
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