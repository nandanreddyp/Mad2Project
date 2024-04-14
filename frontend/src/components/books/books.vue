<template>
    <div class="books-list" >
        <router-link v-for="book in books" :key="book.id"  :to="user.role==='user' ? { name: 'user-book', params: { id: book.id } } : { name: 'librarian-book', params: { id: book.id} }">
            <div class="book-list-item">
                
                    <img class="book-list-logo" :src="book.img_path" alt="">
                    <div class="book-list-details">
                        <h2>{{book.name}}</h2>
                        <div class="book-meta">
                            <span>{{ book.page_count + ' Pages' }}</span>
                            <span>{{'Published on: '+ formatISODate(book.publication_date) }}</span>
                            <span>{{'Ratings: ' + book.rating}}</span>
                        </div>
                        {{book.description}}
                    </div>            
            </div>
        </router-link>
        <div class="book-list-item-skeleton" v-if="loading" v-for="n in 3" :key="n"> <!--content skeleton-->
            <div class="skeleton-image"></div>
            <div class="skeleton-details">
                <div class="skeleton-title"></div>
                <div class="skeleton-meta">
                    <span></span>
                </div>
                <div class="skeleton-description"></div>
            </div>
        </div>
        <div class="book-list-end">
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
        books: Array, has_next: Boolean, loading: Boolean,
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
.books-list {
    width: 100%;
    padding: 5px 10px;
    display: flex;
    flex-direction: column;
    font-size: 11px;
}
.book-list-item {
    display: flex;
    height: 97px;
    margin-bottom: 20px;
    overflow-y: hidden;
}
.book-list-item:hover {
    cursor: pointer;
    outline: 1px solid rgba(0, 0, 0, 0.07);
    transform: translate(3px,-3px);
}
.book-list-logo {
    height: 98px;
    aspect-ratio: 15/18;
    margin-right: 10px;
}
.book-list-details h2 {
    font-weight: 500;
    font-size: 16px;
    max-height: 38px; padding-bottom: 5px;
    overflow: hidden;
}
.book-meta {
    display: flex;
    flex-wrap: nowrap;
    gap: 5px;
    letter-spacing: 0;
    font-size: 13px;
    color: #006621;
    padding-bottom: 5px;
}
.book-list-end {
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
.book-list-item-skeleton {
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
