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
                        <button @click="toggleEditSection" class="blue">Edit</button>
                        <editSection v-if="edit_section" :toggleEditSection="toggleEditSection" :LoadSection="LoadSection" :updatedToast="updatedToast"/>
                        <button @click="toggleAddBooks">Add books</button>
                        <bookPickerDialog v-if="add_books" :type="type" :toggleAddBooks="toggleAddBooks" :reloadPage="LoadSection" :updatedToast="updatedToast"/>
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

import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

import sectionBooks from '@/components/sections/sectionBooks.vue'
import editSection from '@/components/sections/editSection.vue'
import bookPickerDialog from '@/components/books/pickerDialog.vue'

export default {
    data(){return{
        type: 'section',
        section_loading: true,
        section_id: this.$route.params.id,
        section: null,
        books_loading: true,
        // popup openers
        edit_section: false,
        add_books: false,
    }},
    components: {
        sectionBooks, bookPickerDialog, editSection
    },
    methods: {
        formatISODate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString();
        },
        toggleEditSection() {
            this.edit_section = !this.edit_section
        },
        toggleAddBooks() {
            this.add_books = !this.add_books
        },
        LoadSection() {
            this.section_loading = true
            setTimeout(()=>{
                axiosClient.get(`/api/sections/${this.section_id}`)
                .then(resp => {
                    console.log(resp)
                    this.section = resp.data.section
                    this.section_loading = false
                })
            }, 2000)
        },
        updatedToast() {
            toast.success('Updated section',{autoClose: 4000,})
        }
    },
    mounted() {
        this.LoadSection()
    },
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



/* skeleton loader */

.skeleton-container {
  background-color: #f5f5f5; /* Background color for the skeleton container */
  border-radius: 5px; /* Rounded corners */
  padding: 20px; /* Padding around the skeleton container */
  margin-bottom: 20px; /* Margin bottom to create space between elements */
}

.skeleton-header {
  display: flex;
  align-items: center;
}

.skeleton-image {
  width: 100px; /* Width of the skeleton image */
  height: 100px; /* Height of the skeleton image */
  background-color: #ccc; /* Background color for the skeleton image */
  border-radius: 50%; /* Create a circular shape */
  margin-right: 20px; /* Margin to create space between the image and details */
}

.skeleton-details {
  flex: 1; /* Allow details to expand to fill remaining space */
}

.skeleton-meta {
  width: 80%; /* Width of the skeleton meta */
  height: 20px; /* Height of the skeleton meta */
  background-color: #ccc; /* Background color for the skeleton meta */
  margin-bottom: 10px; /* Margin bottom to create space between meta items */
}

.skeleton-description {
  height: 100px; /* Height of the skeleton description */
  background-color: #ccc; /* Background color for the skeleton description */
  margin-top: 20px; /* Margin top to create space between header and description */
}

</style>