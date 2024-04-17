<template>
    <div class="request-list">
        <div class="request-list-item" v-for="request in requests" :key="request.id">

        </div>
        <div class="request-list-end">
            <h2 v-if="has_next === false">-End-</h2>
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
        requests: Array, has_next: Boolean, loading: Boolean,
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
.requests-list {
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
.request-list-item {
    display: flex; height: 97px;
    max-width: 450px; width: 100%;
    padding: 0 10px;
    margin-bottom: 20px; overflow-y: hidden;
}
.request-list-item:hover {
    cursor: pointer;
    outline: 1px solid rgba(0, 0, 0, 0.07);
    transform: translate(3px,-3px);
}


@keyframes skeleton-loading {
  0% {
    background-color: hsl(200, 20%, 80%);
  }
  100% {
    background-color: hsl(200, 20%, 95%);
  }
}
</style>