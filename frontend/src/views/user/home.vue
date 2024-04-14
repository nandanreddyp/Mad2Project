<template>
    <div class="main-container">

        <div class="continue-book-section" v-if="is_last_book">
            <div class="collection-title">
                <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#6b9bd2" stroke-width="3" stroke-linecap="round" stroke-linejoin="arcs"><polyline points="16 18 22 12 16 6"></polyline><polyline points="8 6 2 12 8 18"></polyline></svg>
                Continue reading from where you left</div>
            <div class="collection-container" v-on:scroll="handleScroll" ref="booksContainer">
                <booksList :books="last_book" :loading="loading" :has_next="true"/>
            </div>
        </div>

        <div class="collection-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#6b9bd2" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"><path d="M19 21l-7-5-7 5V5a2 2 0 0 1 2-2h10a2 2 0 0 1 2 2z"></path></svg>
            Books you got access to</div>
        <div class="collection-container"  v-on:scroll="handleScroll" ref="booksContainer">
            <booksList  v-if="is_access_books" :books="access_books" :loading="loading" :has_next="true"/>

            <div v-else style="min-height: 200px; display: flex; flex-direction: column; align-items: center; justify-content: center;">
                <h2 style="text-align: center;">Make book requests to get access to read books</h2>
                <router-link style="text-decoration: none; background-color: blue; color: white; width: max-content; padding: 5px; margin: 10px; border-radius: 5px;" :to="{name:'user-books'}">Click here to view latest books</router-link>
            </div>
        </div>

        <div class="collection-title">
            <svg xmlns="http://www.w3.org/2000/svg" width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="#6b9bd2" stroke-width="3" stroke-linecap="round" stroke-linejoin="arcs"><polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon></svg>
            Popular books</div>
        <div class="collection-container" ref="booksContainer">
            <booksList :books="popular_books" :loading="loading" :has_next="true"/>
        </div>

    </div>
</template>

<script>
import booksList from '@/components/books/books.vue'
import axiosClient from '@/services/axios'
export default {
    data(){return {
            last_book : [],
            access_books : [],
            popular_books : [],
            is_last_book: false,
            is_access_books: false,
            loading: true,
    }},
    components: {
        booksList
    },
    methods: {
        fetchLastBook() {
            this.is_last_book = true;
            setTimeout(()=>{
                axiosClient.get(`/api/books/${1}`)
                .then(resp => {
                    this.last_book.push(resp.data.book)
                })
                this.loading = false;
            }, 2000)
        },
        fetchAccessBooks() {
            this.is_access_books = true;
            setTimeout(()=>{
                axiosClient.get(`/api/books?per_page=6`)
                .then(resp => {
                    this.access_books = resp.data.books
                })
                this.loading = false;
            }, 2000)
        },
        fetchPopularBooks() {
            setTimeout(()=>{
                axiosClient.get(`/api/books?per_page=6`)
                .then(resp => {
                    this.popular_books = resp.data.books
                })
                this.loading = false;
            }, 2000)
        }
    },
    mounted() {
        this.fetchLastBook()
        this.fetchAccessBooks()
        this.fetchPopularBooks()
    },

    beforeDestroy() {

    }
}
</script>

<style scoped>
.collection-title {
    font-size: 20px;
    font-weight: 700;
    padding: 10px 5px;
    display: flex; align-items: center; gap: 3px;
}
.main-container {
    overflow: auto; padding: 0 10px;
}
.collection-container {
    border-bottom: 1px solid black;
    /* flex: 1; overflow: auto;*/
    flex: 1;
}
</style>