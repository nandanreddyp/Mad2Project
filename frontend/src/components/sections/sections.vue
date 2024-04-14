<template>
    <div class="sections-list">
        <router-link v-for="section in sections" :key="section.id" :to="user.role==='user' ? {name:'user-section',params:{id:section.id}} : {name:'librarian-section',params:{id:section.id}}">
            <div class="section-list-item" >
                <img class="section-list-logo" :src="section.img_path" alt="">
                <div class="section-list-details">
                    <h2>{{ section.name }}</h2>
                    {{ section.description }}
                </div>
            </div>
        </router-link>
        <div class="skeleton-list-item" v-if="loading" v-for="n in 3" :key="n"> <!--content skeleton-->
            <div class="skeleton-image"></div>
            <div class="skeleton-details">
                <div class="skeleton-title"></div>
                <div class="skeleton-description"></div>
            </div>
        </div>
    </div>

</template>

<script>
import { mapGetters } from 'vuex';
export default {
    data(){return{

    }},
    computed: {
        ...mapGetters(['user'])
    },
    props: {
        sections: Array, loading: Boolean,
    },
    mounted() {

    },
    methods: {

    }
}
</script>

<style scoped>
a {
    text-decoration: none;
    color: unset; font-weight: unset; font-size: unset;
    cursor: context-menu;
}
.sections-list {
    width: 100%;
    padding: 5px;
    display: flex; flex-direction: row;
    flex-wrap: wrap; align-items: flex-start;
    justify-content: center; align-items: center;
    gap: 16px; margin: 0 auto;
    width: 100%;
    padding: 20px 10px;
    font-size: 11px;
}
.section-list-item {
    display: flex; height: 97px;
    max-width: 450px; width: 100%;
    padding: 0 10px;
    margin-bottom: 20px; overflow-y: hidden;
}
.section-list-item:hover {
    cursor: pointer;
    outline: 1px solid rgba(0, 0, 0, 0.07);
    transform: translate(3px,-3px);
}
.section-list-logo {
    height: 98px; aspect-ratio: 1/1; object-fit: cover;
    margin-right: 10px; border-radius: 50px; outline: 1px solid red;
}
.section-list-details  h2 {
    font-weight: 500; font-size: 16px;
    max-height: 38px; padding-bottom: 5px;
    overflow: hidden;
}
/* Skeleton styles */
@keyframes skeleton-loading {
  0% {
    background-color: hsl(200, 20%, 80%);
  }
  100% {
    background-color: hsl(200, 20%, 95%);
  }
}
.skeleton-list-item {
    display: flex; height: 97px;
    max-width: 450px; width: 100%;
    padding: 0 10px;
    margin-bottom: 20px; overflow-y: hidden;
}
.skeleton-image {
    height: 98px; aspect-ratio: 1/1; object-fit: cover;
    margin-right: 10px; border-radius: 50px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
.skeleton-details {
    flex: 1;
    padding: 10px;
}
.skeleton-title {
    width: 60%;
    height: 16px;
    margin-bottom: 8px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
.skeleton-description {
    width: 100%;
    height: 48px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}

/* according to display*/
@media screen and (max-width: 560px) {
    
}
</style>