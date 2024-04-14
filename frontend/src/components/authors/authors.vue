<template>
    <div class="authors-list" >
        <router-link v-for="author in authors" :key="author.id"  :to="user.role==='user' ? { name: 'user-author', params: { id: author.id } } : { name: 'librarian-author', params: { id: author.id} }">
            <div class="author-list-item">
                
                    <img class="author-list-logo" :src="author.img_path" alt="">
                    <div class="author-list-details">
                        <h2>{{author.name}}</h2>
                        <div class="author-meta">
                            <span>{{ author.page_count + ' Pages' }}</span>
                            <span>{{'Published on: '+ formatISODate(author.publication_date) }}</span>
                            <span>{{'Ratings: ' + author.rating}}</span>
                        </div>
                        {{author.description}}
                    </div>            
            </div>
        </router-link>
        <div class="author-list-item-skeleton" v-if="loading" v-for="n in 3" :key="n"> <!--content skeleton-->
            <div class="skeleton-image"></div>
            <div class="skeleton-details">
                <div class="skeleton-title"></div>
                <div class="skeleton-meta">
                    <span></span>
                </div>
                <div class="skeleton-description"></div>
            </div>
        </div>
        <div class="author-list-end">
            <h2 v-if="has_next === false">-End-</h2>
        </div>
    </div>
</template>

<script>
import { mapGetters } from 'vuex';
export default {
    data() {
        return {
        }
    },
    computed: {
        ...mapGetters(['user'])
    },
    props: {
        authors: Array, has_next: Boolean, loading: Boolean,
    },
    mounted() {
    },
    methods: {
        formatISODate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString();
        },
    }
}
</script>

<style scoped>
a {
    text-decoration: none;
    color: unset; font-weight: unset; font-size: unset;
    cursor: context-menu;
}
.authors-list {
    width: 100%;
    padding: 5px 10px;
    display: flex;
    flex-direction: column;
    font-size: 11px;
}
.author-list-item {
    display: flex;
    height: 97px;
    margin-bottom: 20px;
    overflow-y: hidden;
}
.author-list-item:hover {
    cursor: pointer;
    outline: 1px solid rgba(0, 0, 0, 0.07);
    transform: translate(3px,-3px);
}
.author-list-logo {
    height: 98px;
    aspect-ratio: 15/18;
    margin-right: 10px;
}
.author-list-details h2 {
    font-weight: 500;
    font-size: 16px;
    max-height: 38px; padding-bottom: 5px;
    overflow: hidden;
}
.author-meta {
    display: flex;
    flex-wrap: nowrap;
    gap: 5px;
    letter-spacing: 0;
    font-size: 13px;
    color: #006621;
    padding-bottom: 5px;
}
.author-list-end {
    display: flex; align-items: center; justify-content: center;
    margin-bottom: 10px;
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
.author-list-item-skeleton {
    display: flex;
    height: 97px;
    margin-bottom: 20px;
    overflow-y: hidden;
}
.skeleton-image {
    height: 98px;
    aspect-ratio: 15/18;
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
.skeleton-meta {
    display: flex;
    margin-bottom: 8px;
}
.skeleton-meta span {
    width: 30%;
    height: 12px;
    margin-right: 10px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
.skeleton-description {
    width: 100%;
    height: 48px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
</style>
