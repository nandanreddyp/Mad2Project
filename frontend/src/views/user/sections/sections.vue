<template>
    <form @submit.prevent="runSearch" class="collection-header">
        <div class="search">
            <input v-model="query" name="query" type="search" placeholder="Search in sections">
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
    <div class="collection-container" v-on:scroll="handleScroll" ref="sectionsContainer">
        <sectionsList :sections="sections" :loading="loading"/>
    </div>
</template>

<script>
import axiosClient from '@/services/axios';

import sectionsList from '@/components/sections/sections.vue'

export default {
    data(){return{
        // lodaing data
        sections: [],
        loading: true,
        // filter
        query: this.$route.query.query,
        sort: 'newest',
        // title
        title: 'Sections to explore books'
    }},
    components: {
        sectionsList,
    },
    methods: {
        runSearch() {
            this.$router.push({path:'/sections',query:{query:this.query,sort:this.sort}})
            this.sections=[]
            if (this.query) {
                if (this.sort === 'newest') {
                    this.title=`Recent sections with search "${this.query}"`
                } else if (this.sort === 'oldest') {
                    this.title=`Oldest sections with search "${this.query}"`
                } else if (this.sort === 'asc') {
                    this.title=`Sections with search "${this.query}", sorted A-Z`
                } else if (this.sort === 'desc') {
                    this.title=`Sections with search "${this.query}", sorted Z-A`
                }
            } else {
                if (this.sort === 'newest') {
                    this.title='Recently added sections'
                } else if (this.sort === 'oldest') {
                    this.title='Oldest sections'
                } else if (this.sort === 'asc') {
                    this.title='Sections sorted by Name (A-Z)'
                } else if (this.sort === 'desc') {
                    this.title='Sections sorted by Name (Z-A)'
                }
            }
            this.loadSections()
        },
        loadSections() {
            this.loading = true
            setTimeout(() => {
                axiosClient.get(`/api/sections?query=${this.query ? this.query : ''}&sort=${this.sort ? this.sort : ''}`)
                .then(resp => {
                    resp.data.sections.forEach(obj => {
                        this.sections.push(obj)
                    })
                })
                this.loading = false;
            }, 2000)
        }
    },
    mounted(){
        this.runSearch()
    },
    watch: {
        $route(to, from) {
            if (to.fullPath === '/sections?sort=newest') {
                this.sort = 'newest'
                this.runSearch()
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
    max-height: 35px;
}
.collection-container {
    /* max-height: calc(100% - 35px); */
    flex: 1; overflow-y: scroll;
}

/* according to display*/
@media screen and (max-width: 560px) {
    .collection-container{
        max-height: unset;
        flex: 1; overflow: scroll;
    }
}
</style>