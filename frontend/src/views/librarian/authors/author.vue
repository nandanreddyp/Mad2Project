<template>
    <div class="container">
        <div class="skeleton-container" v-if="author_loading">
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
        <div class="author-container" v-else>
            <div class="author-header">
                <img class="author-image" :src="author.img_path" alt="">
                <div class="author-details">
                    <div class="author-title">{{ author.name }}</div>
                    <div class="author-meta">
                        <span>{{ author.authors_count + ' Authors' }}</span>
                        <span>{{'Created on: '+ formatISODate(author.created_date) }}</span>
                    </div>
                    <div class="author-options">
                        <button @click="toggleEditAuthor" class="blue">Edit</button>
                        <editAuthor v-if="edit_author" :toggleEditAuthor="toggleEditAuthor" :updatedToast="updatedToast"/>
                        <button @click="toggleAddBooks" >Add books</button>
                        <bookPickerDialog v-if="add_books" :type="type" :toggleAddBooks="toggleAddBooks" :updatedToast="updatedToast" :reloadPage="LoadAuthor"/>
                    </div>
                </div>
            </div>
            <div class="author-description" v-if="author.description">
                <h4>About author</h4>
                {{ author.description }}
            </div>
        </div>
        <div class="author-books">
            <authorBooks />
        </div>

    </div>
</template>

<script>
import axiosClient from '@/services/axios';

import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

import authorBooks from '@/components/authors/authorBooks.vue'
import editAuthor from '@/components/authors/editAuthor.vue'
import bookPickerDialog from '@/components/books/pickerDialog.vue';

export default {
    data(){return{
        type: 'author',
        author_loading: true,
        author_id: this.$route.params.id,
        author: null,
        books_loading: true,
        // popup openers
        edit_author: false,
        add_books: false,
    }},
    components: {
        authorBooks, editAuthor, bookPickerDialog, editAuthor,
    },
    methods: {
        formatISODate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString();
        },
        toggleEditAuthor() {
            this.edit_author = !this.edit_author
        },
        toggleAddBooks() {
            this.add_books = !this.add_books
        },
        LoadAuthor() {
            this.author_loading = true
            setTimeout(()=>{
                axiosClient.get(`/api/authors/${this.author_id}`)
                .then(resp => {
                    console.log(resp)
                    this.author = resp.data.author
                    this.author_loading = false
                })
            }, 2000)
        },
        updatedToast() {
            toast.success('Updated author',{autoClose: 4000,})
        }
    },
    mounted() {
        this.LoadAuthor()
    },
}
</script>

<style scoped>
.container {
    overflow: auto;
}

.author-container {
    padding: 5px;
    max-width: 900px;
    width: 100%;
    background-color: white;
    margin: 30px auto;
    box-shadow: 0 0 4px 2px rgba(189,189,189,1);
}

.author-header {
    display: flex;
    flex-wrap: wrap;
}

.author-image {
    width: 100%;
    height: auto;
    aspect-ratio: 1/1; object-fit: cover;
    max-width: 210px; 
    margin-right: 15px;
}

.author-details {
    flex: 1; /* Allow details to expand to fill remaining space */
    padding: 18px 15px 0;
}

.author-title {
    font-weight: 300;
    line-height: 1.4;
    white-space: normal;
    color: #212121;
    font-size: 24px;
    margin: 0 0 10px;
    max-height: 120px;
    overflow: hidden;
}

.author-meta {
    margin-top: 9px;
    font-weight: 300;
    font-size: 18px;
    color: #006621;
}

.author-options {
    display: flex;
    align-items: center;
    justify-content: space-evenly;
    margin-top: 10px;
}

.author-options button {
    min-width: 90px;
    width: max-content;
    cursor: pointer;
    color: #212529;
    background-color: #ffc107;
    border-color: #ffc107;
    padding: 3px 12px;
    border-radius: 5px;
}

.author-description {
    padding-top: 10px;
}

.author-description h4 {
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