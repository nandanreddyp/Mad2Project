<template>
    <div class="upload-bar" v-if="user.role==='librarian'">
        <button class="upload-button" @click="toggleAddAuthor">Create New Author</button>
        <addAuthor v-if="add_author" :toggleAddAuthor="toggleAddAuthor"/>
    </div>
    <form @submit.prevent="runSearch" class="collection-header">
        <div class="search">
            <input v-model="query" name="query" type="search" placeholder="Search in authors">
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
    <div class="collection-container" v-on:scroll="handleScroll" ref="authorsContainer">
        <authorsList :authors="authors" :has_next="has_next" :loading="loading"/>
    </div>
</template>

<script>
import axiosClient from '@/services/axios';

import authorsList from '@/components/authors/authors.vue'
import addAuthor from '@/components/authors/addAuthor.vue';

export default {
    data(){return {
        // loading data
        authors: [],
        page: 1,
        per_page: 7,
        has_next: null,
        loading: true,
        // filter
        query: this.$route.query.query,
        sort: 'newest',
        // title
        title: 'Recently added authors',
        // librarian requirements
        user: this.$store.state.user,
        add_author: false,
    }},
    components: {
        authorsList, addAuthor,
    },
    methods: {
        runSearch(){
            this.$router.push({name: this.user.role === 'librarian' ? 'librarian-authors' : 'user-authors', query:{query:this.query,sort:this.sort}})
            this.page=1; this.authors=[]; this.has_next = null
            if (this.query) {
                if (this.sort === 'newest') {
                    this.title=`Recent authors with search "${this.query}"`
                } else if (this.sort === 'oldest') {
                    this.title=`Oldest authors with search "${this.query}"`
                } else if (this.sort === 'asc') {
                    this.title=`Authors with search "${this.query}", sorted A-Z`
                } else if (this.sort === 'desc') {
                    this.title=`Authors with search "${this.query}", sorted Z-A`
                }
            } else {
                if (this.sort === 'newest') {
                    this.title='Recently added authors'
                } else if (this.sort === 'oldest') {
                    this.title='Oldest authors'
                } else if (this.sort === 'asc') {
                    this.title='Authors sorted by Name (A-Z)'
                } else if (this.sort === 'desc') {
                    this.title='Authors sorted by Name (Z-A)'
                }
            }
            this.loadAuthors(this.page, this.per_page)
        },
        loadAuthors(page, per_page) {
            this.loading = true
            setTimeout(()=>{
                axiosClient.get(`/api/authors?query=${this.query ? this.query : ''}&sort=${this.sort ? this.sort : ''}&page=${page}&per_page=${per_page}`)
                .then(resp => {
                    this.has_next = resp.data.page_data.has_next
                    resp.data.authors.forEach(obj => {
                        this.authors.push(obj)
                    })
                    this.loading = false;
                })
            }, 2000)
        },
        handleScroll() {
            const container = this.$refs.authorsContainer;
            const bottomOffset = container.scrollHeight - container.scrollTop - container.clientHeight;
            if (bottomOffset === 0 && !this.loading) {
                if (this.has_next !== false) {
                    this.page++
                    this.loadAuthors(this.page,this.per_page);
                }
            }
        },
        toggleAddAuthor() {
            this.add_author = !this.add_author
        }
    },
    mounted(){
        this.runSearch()
    },
    watch: {
        $route(to, from) {
            if (to.fullPath === '/authors?sort=newest' || to.fullPath === '/librarian/authors?sort=newest') {
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