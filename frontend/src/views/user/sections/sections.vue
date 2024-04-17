<template>
    <div class="upload-bar" v-if="user.role==='librarian'">
        <button class="upload-button" @click="toggleAddSection">Create New Section</button>
        <addSection v-if="add_section" :toggleAddSection="toggleAddSection" :addedToast="addedToast" :reloadPage="makeDefaultPageView"/>
    </div>
    <form @submit.prevent="runSearch" class="collection-header">
        <div class="search">
            <input v-model="query" name="query" type="search" placeholder="Search in sections">
            <button>Search</button>
        </div>
        <div class="collection-sort">
            Sort by
            <select title="sort by" v-model="sort" @change="runSearch" name="sort" id="">
                <option value="" :selected="sort === 'newest'" >Recent</option>
                <option value="oldest" :selected="sort === 'oldest'" >Oldest</option>
                <option value="asc"    :selected="sort === 'asc'"    >Name (A-Z)</option>
                <option value="desc"   :selected="sort === 'desc'"   >Name (Z-A)</option>
            </select>
        </div>
    </form>
    <div class="collection-title">{{title}}</div>
    <div class="collection-container" v-on:scroll="handleScroll" ref="sectionsContainer">
        <sectionsList :sections="sections" :has_next="has_next" :loading="loading"/>
    </div>
</template>

<script>
import axiosClient from '@/services/axios';

import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

import sectionsList from '@/components/sections/sections.vue'
import addSection from '@/components/sections/addSection.vue';

export default {
    data(){return{
        // lodaing data
        sections: [],
        page: 1,
        per_page: 7,
        has_next: null,
        loading: true,
        // filter
        query: this.$route.query.query || "",
        sort: this.$route.query.sort || "",
        // title
        title: 'Sections to explore books',
        // librarian requirements
        user: this.$store.state.user,
        add_section: false,
    }},
    components: {
        sectionsList, addSection,
    },
    methods: {
        runSearch() {
            this.$router.push(
                {name: this.user.role === 'librarian' ? 'librarian-sections' : 'user-sections', 
                query: {...(this.query !== '' && { query: this.query }), ...(this.sort !== '' && { sort: this.sort }),}
            })
            this.page=1; this.sections=[]; this.has_next = null
            if (this.query) {
                if (this.sort === '') {
                    this.title=`Recent sections with search "${this.query}"`
                } else if (this.sort === 'oldest') {
                    this.title=`Oldest sections with search "${this.query}"`
                } else if (this.sort === 'asc') {
                    this.title=`Sections with search "${this.query}", sorted A-Z`
                } else if (this.sort === 'desc') {
                    this.title=`Sections with search "${this.query}", sorted Z-A`
                }
            } else {
                if (this.sort === '') {
                    this.title='Recently added sections'
                } else if (this.sort === 'oldest') {
                    this.title='Oldest sections'
                } else if (this.sort === 'asc') {
                    this.title='Sections sorted by Name (A-Z)'
                } else if (this.sort === 'desc') {
                    this.title='Sections sorted by Name (Z-A)'
                }
            }
            // this.loadSections()
        },
        loadSections(page, per_page) {
            this.loading = true
            setTimeout(() => {
                axiosClient.get(`/api/sections?query=${this.query}&sort=${this.sort || 'newest' }&page=${page}&per_page=${per_page}`)
                .then(resp => {
                    this.has_next = resp.data.page_data.has_next
                    resp.data.sections.forEach(obj => {
                        this.sections.push(obj)
                    })
                    this.loading = false;
                })
            }, 2000)
        },
        handleScroll() {
            const container = this.$refs.sectionsContainer;
            const bottomOffset = container.scrollHeight - container.scrollTop - container.clientHeight;
            if (bottomOffset === 0 && !this.loading) {
                if (this.has_next !== false) {
                    this.page++
                    this.loadSections(this.page,this.per_page);
                }
            }
        },
        toggleAddSection() {
            this.add_section = !this.add_section
        },
        addedToast() {
            toast.success('Added section',{autoClose: 4000,})
        },
        showRedirectToasts() {
            if (this.$route.query.msg) { // for toast messages
                if (this.$route.query.msg === 'deleted') {
                toast.error('Deleted section',{autoClose: 4000,})
                }
            }
        },
        makeDefaultPageView() {
            this.sort=''; this.query=''; this.page=1; this.has_next=null; this.sections = []; this.title = 'Recently added sections';
            this.loadSections(this.page, this.per_page)
        }
    },
    mounted(){
        this.showRedirectToasts()
        this.makeDefaultPageView()
    },
    watch: {
        $route(to, from) {
            this.showRedirectToasts()
            if (to.fullPath === '/sections' || to.fullPath === '/librarian/sections') { // for sidebar click
                this.makeDefaultPageView()
            } else {
                this.loadSections(this.page, this.per_page )
            }
        }
    }
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