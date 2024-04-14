<template>
    <div class="container">
        <div class="skeleton-container" v-if="section_loading">
            <div class="skeleton-header">
                <div class="skeleton-image"></div>
                <div class="skeleton-details">
                    <div class="skeleton-meta"></div>
                    <div class="skeleton-meta"></div>
                    <div class="skeleton-meta"></div>
                </div>
            </div>
            <div class="skeleton-description"></div>
        </div>
        <div class="section-container" v-else>
            <div class="section-header">
                <img class="section-image" :src="section.img_path" alt="">
                <div class="section-details">
                    <div class="section-title">{{ section.name }}</div>
                    <div class="section-meta">
                        <span>{{ section.sections_count + ' Sections' }}</span>
                        <span>{{'Created on: '+ formatISODate(section.created_date) }}</span>
                    </div>
                    <div class="section-options">
                        <button class="blue">Edit</button>
                        <button>Add books</button>
                    </div>
                </div>
            </div>
            <div class="section-description" v-if="section.description">
                <h4>About section</h4>
                {{ section.description }}
            </div>
        </div>
        <div class="section-books">
            <sectionBooks />
        </div>

    </div>
</template>

<script>
import axiosClient from '@/services/axios';

import sectionBooks from '@/components/sections/sectionBooks.vue'

export default {
    data(){return{
        section_loading: true,
        section_id: this.$route.params.id,
        section: null,
        books_loading: true,
    }},
    components: {
        sectionBooks,
    },
    methods: {
        formatISODate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString();
        },
    },
    mounted() {
        axiosClient.get(`/api/sections/${this.section_id}`)
        .then(resp=>{
            this.section = resp.data
            this.section_loading = false
        })
    }
}
</script>

<style scoped>
.container {
    overflow: auto;
}

.section-container {
    padding: 5px;
    max-width: 900px;
    width: 100%;
    background-color: white;
    margin: 30px auto;
    box-shadow: 0 0 4px 2px rgba(189,189,189,1);
}

.section-header {
    display: flex;
    flex-wrap: wrap;
}

.section-image {
    width: 100%;
    height: auto;
    aspect-ratio: 1/1; object-fit: cover;
    max-width: 210px; 
    margin-right: 15px;
}

.section-details {
    flex: 1; /* Allow details to expand to fill remaining space */
    padding: 18px 15px 0;
}

.section-title {
    font-weight: 300;
    line-height: 1.4;
    white-space: normal;
    color: #212121;
    font-size: 24px;
    margin: 0 0 10px;
    max-height: 120px;
    overflow: hidden;
}

.section-meta {
    margin-top: 9px;
    font-weight: 300;
    font-size: 18px;
    color: #006621;
}

.section-options {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    margin-top: 10px;
}

.section-options button {
    min-width: 90px;
    width: max-content;
    cursor: pointer;
    color: #212529;
    background-color: #ffc107;
    border-color: #ffc107;
    padding: 3px 12px;
    border-radius: 5px;
}

.section-description {
    padding-top: 10px;
}

.section-description h4 {
    font-size: 18px;
    padding-bottom: 6px;
}



/* section books */
.section-books {

}
</style>