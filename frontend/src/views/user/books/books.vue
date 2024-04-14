<template>
    <div class="upload-bar" v-if="user.role==='librarian'">
        <button class="upload-button" @click="toggleAddBook">Create New Book</button>
        <addBook v-if="add_book" :toggleAddBook="toggleAddBook"/>
    </div>
    <form @submit.prevent="runSearch" class="collection-header">
        <div class="search">
            <input v-model="query" name="query" type="search" placeholder="Search in books">
            <button>Search</button>
        </div>
        <div class="collection-sort">
            Sort by
            <select v-model="sort" @change="runSearch" name="sort" id="">
                <option value="newest" :selected="sort === 'newest'" >Recent</option>
                <option value="oldest" :selected="sort === 'oldest'" >Oldest</option>
                <option value="asc"    :selected="sort === 'asc'"    >Name (A-Z)</option>
                <option value="desc"   :selected="sort === 'desc'"   >Name (Z-A)</option>
            </select>
        </div>
    </form>
    <div class="collection-title">{{title}}</div>
    <div class="collection-container" v-on:scroll="handleScroll" ref="booksContainer">
        <booksList :books="books" :has_next="has_next" :loading="loading"/>
    </div>
</template>

<script>
import axiosClient from '@/services/axios';

import booksList from '@/components/books/books.vue'
import addBook from '@/components/books/addBook.vue';

export default {
    data(){return {
        // loading data
        books: [],
        page: 1,
        per_page: 7,
        has_next: null,
        loading: true,
        // filter
        query: this.$route.query.query,
        sort: 'newest',
        // title
        title: 'Recently added books',
        // librarian requirements
        user: this.$store.state.user,
        add_book: false,
    }},
    components: {
        booksList, addBook,
    },
    methods: {
        runSearch(){
            this.$router.push({name: this.user.role === 'librarian' ? 'librarian-books' : 'user-books', query:{query:this.query,sort:this.sort}})
            this.page=1; this.books=[]; this.has_next = null
            if (this.query) {
                if (this.sort === 'newest') {
                    this.title=`Recent books with search "${this.query}"`
                } else if (this.sort === 'oldest') {
                    this.title=`Oldest books with search "${this.query}"`
                } else if (this.sort === 'asc') {
                    this.title=`Books with search "${this.query}", sorted A-Z`
                } else if (this.sort === 'desc') {
                    this.title=`Books with search "${this.query}", sorted Z-A`
                }
            } else {
                if (this.sort === 'newest') {
                    this.title='Recently added books'
                } else if (this.sort === 'oldest') {
                    this.title='Oldest books'
                } else if (this.sort === 'asc') {
                    this.title='Books sorted by Name (A-Z)'
                } else if (this.sort === 'desc') {
                    this.title='Books sorted by Name (Z-A)'
                }
            }
            this.loadBooks(this.page, this.per_page)
        },
        loadBooks(page, per_page) {
            this.loading = true
            setTimeout(()=>{
                axiosClient.get(`/api/books?query=${this.query ? this.query : ''}&sort=${this.sort ? this.sort : ''}&page=${page}&per_page=${per_page}`)
                .then(resp => {
                    this.has_next = resp.data.page_data.has_next
                    resp.data.books.forEach(obj => {
                        this.books.push(obj)
                    })
                    this.loading = false;
                })
            }, 2000)
        },
        handleScroll() {
            const container = this.$refs.booksContainer;
            const bottomOffset = container.scrollHeight - container.scrollTop - container.clientHeight;
            if (bottomOffset === 0 && !this.loading) {
                if (this.has_next !== false) {
                    this.page++
                    this.loadBooks(this.page,this.per_page);
                }
            }
        },
        toggleAddBook() {
            this.add_book = !this.add_book
        }
    },
    mounted(){
        this.runSearch()
    },
    watch: {
        $route(to, from) {
            if (to.fullPath === '/books?sort=newest' || to.fullPath === '/librarian/books?sort=newest') {
                this.sort = 'newest'
                this.runSearch()
            }
        }
    },
}
</script>

<style scoped>
.collection-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px;
}
.collection-header input, .collection-header button, .collection-header select{
    padding: 3px;
}
.collection-title {
    font-size: 20px;
    font-weight: 700;
    padding: 5px;
}
.collection-container {
    flex: 1; overflow: auto;
}

/* admin upload bar */
.upload-bar {
    width: 100%; display: flex; justify-content: center;
    border-bottom: 1px solid black;
}
.upload-button {
    padding: 10px 20px;
    margin: 10px 10px;
    color: #333;
    border: none;
    border-radius: 50px;
    cursor: pointer;
    color: rgb(32, 33, 36);
    background-color: rgb(138,180,248);
}
.upload-button:hover {
    transform: translate(-2px, 1px);
    background-color: rgb(69, 121, 204);
}
</style>