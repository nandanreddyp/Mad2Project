<template>
    <form @submit.prevent="runSearch" class="collection-header">
        <div class="search">
            <input v-model="query" name="query" type="search" placeholder="Search in books">
            <button>Search</button>
        </div>
        <div class="collection-sort">
            <div>Sort by</div>
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

export default {
    data(){return {
        author_id: this.$route.params.id,
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
        title: 'Recently added books'
    }},
    components: {
        booksList,
    },
    methods: {
        runSearch(){
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
                axiosClient.get(`/api/authors/${this.author_id}/books?query=${this.query ? this.query : ''}&sort=${this.sort ? this.sort : ''}&page=${page}&per_page=${per_page}`)
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
        }
    },
    mounted(){
        this.runSearch()
    },
    watch: {
    },
}
</script>

<style scoped>
.collection-header {
    display: flex;
    flex-wrap: wrap; /* Allow elements to wrap to the next line on smaller screens */
    align-items: center;
    justify-content: space-between;
    padding: 10px; width: 100%;
}
.search {
    display: flex;
    margin-right: 10px; /* Add some spacing between the search and sort elements */
}
.search input {
    width: 100%; /* Make the input take up all available space */
    max-width: 200px; /* Limit the maximum width of the input for larger screens */
}
.collection-sort {
    display: flex; white-space: nowrap; align-items: center;
    margin-left: 10px; /* Add some spacing between the sort and search elements */
}
.collection-sort select {
    width: 100%; /* Make the select element take up all available space */
    max-width: 200px; /* Limit the maximum width of the select for larger screens */
    margin-left: 10px;
}
/* Adjust padding for better spacing */
.collection-header input,
.collection-header button,
.collection-header select {
    padding: 8px; /* Increase padding for better touch usability on smaller screens */
}

/* Apply media queries for specific screen sizes */
@media screen and (max-width: 530px) {
    .collection-header {
        flex-direction: column; /* Stack elements vertically on smaller screens */
    }
    .search,
    .collection-sort {
        width: 100%;
        max-width: 100%; /* Ensure elements take up full width on smaller screens */
        margin: 0; /* Remove margins on smaller screens */
    }
}

.collection-title {
    font-size: 20px;
    font-weight: 700;
    padding: 5px;
}
.collection-container {
    flex: 1; overflow: auto;
}
</style>