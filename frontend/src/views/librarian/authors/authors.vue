<template>
    <div class="upload-bar" v-if="user.role==='librarian'">
        <button class="upload-button" @click="toggleAddAuthor">Create New Author</button>
        <addAuthor v-if="add_author" :toggleAddAuthor="toggleAddAuthor" :addedToast="addedToast" :reloadPage="makeDefaultPageView"/>
    </div>
    <form @submit.prevent="runSearch" class="collection-header">
        <div class="search">
            <input v-model="query" name="query" type="search" placeholder="Search in authors">
            <button>Search</button>
        </div>
        <div class="collection-sort">
            Sort by
            <select title="sort by" v-model="sort" @change="runSearch" name="sort" id="">
                <option value="" >Recent</option>
                <option value="oldest" >Oldest</option>
                <option value="asc"    >Name (A-Z)</option>
                <option value="desc"   >Name (Z-A)</option>
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

import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

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
        query: this.$route.query.query || "",
        sort: this.$route.query.sort || "",
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
            this.$router.push(
                {name: this.user.role === 'librarian' ? 'librarian-authors' : 'user-authors', 
                query: {...(this.query !== '' && { query: this.query }), ...(this.sort !== '' && { sort: this.sort }),}
            })
            this.page=1; this.authors=[]; this.has_next = null
            if (this.query) {
                if (this.sort === '') {
                    this.title=`Recent authors with search "${this.query}"`
                } else if (this.sort === 'oldest') {
                    this.title=`Oldest authors with search "${this.query}"`
                } else if (this.sort === 'asc') {
                    this.title=`Authors with search "${this.query}", sorted A-Z`
                } else if (this.sort === 'desc') {
                    this.title=`Authors with search "${this.query}", sorted Z-A`
                }
            } else {
                if (this.sort === '') {
                    this.title='Recently added authors'
                } else if (this.sort === 'oldest') {
                    this.title='Oldest authors'
                } else if (this.sort === 'asc') {
                    this.title='Authors sorted by Name (A-Z)'
                } else if (this.sort === 'desc') {
                    this.title='Authors sorted by Name (Z-A)'
                }
            }
            // this.loadAuthors(this.page, this.per_page)
        },
        loadAuthors(page, per_page) {
            this.loading = true
            setTimeout(()=>{
                axiosClient.get(`/api/authors?query=${this.query}&sort=${this.sort || 'newest' }&page=${page}&per_page=${per_page}`)
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
        },
        addedToast() {
            toast.success('Added author',{autoClose: 4000,})
        },
        showRedirectToasts() {
            if (this.$route.query.msg) { // for toast messages
                if (this.$route.query.msg === 'deleted') {
                toast.error('Deleted author',{autoClose: 4000,})
                }
            }
        },
        makeDefaultPageView() {
            this.sort=''; this.query=''; this.page=1; this.has_next=null; this.authors = []; this.title = 'Recently added authors';
            this.loadAuthors(this.page, this.per_page)
        }
    },
    mounted(){
        this.showRedirectToasts()
        this.makeDefaultPageView()
    },
    watch: {
        $route(to, from) {
            this.showRedirectToasts()
            if (to.fullPath === '/authors' || to.fullPath === '/librarian/authors') { // for sidebar click
                this.makeDefaultPageView()
            } else {
                this.loadAuthors(this.page, this.per_page)
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