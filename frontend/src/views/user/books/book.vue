<template>
    <div class="container">
        <div class="skeleton-container" v-if="loading">
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
        <div class="book-container" v-else>
            <div class="book-header">
                <img class="book-image" :src="book.img_path" alt="">
                <div class="book-details">
                    <div class="book-title">{{ book.name }}</div>
                    <div class="book-meta">
                        <span>{{ book.page_count + ' Pages' }}</span>
                        <span>{{'Published on: '+ formatISODate(book.publication_date) }}</span>
                        <span>{{'Reviews: ' + book.review}}</span>
                    </div>
                    <div class="book-authors">
                        Authors: 
                        <router-link v-for="author in authors" :to="{name:'user-author',params:{id:author.id}}">{{ author.name }}</router-link>
                    </div>
                    <div class="book-options">
                        <button class="blue">Edit</button>
                        <button>Add authors</button>
                        <button>Add to sections</button>
                        <button class="blue" @click="openBook(book.pdf_path)">View book</button>
                        <button @click="toggleAddRequest">Request</button>
                        <button @click="toggleEditRequest">Edit Request</button>
                        <addRequest v-if="make_request" :toggleAddRequest="toggleAddRequest"/>
                        <editRequest v-if="edit_request" :toggleEditRequest="toggleEditRequest"/>
                    </div>
                </div>
            </div>
            <div class="book-description" v-if="book.description">
                <h4>About book</h4>
                {{ book.description }}
            </div>
        </div>

        <!--reviews-->
        <reviews/>

    </div>
</template>

<script>
import axiosClient from '@/services/axios';

import reviews from '@/components/reviews/reviews.vue';
import addRequest from '@/components/requests/addRequest.vue';
import editRequest from '@/components/requests/editRequest.vue';

export default{
    data(){return{
        loading: true,
        book_id: this.$route.params.id,
        book: null,
        authors: null,
        reviews: ['a','b','c','d','e'],
        reviews_sort: 'newest',
        review_user: {'img_path':'http://127.0.0.1:5000/static/images/profiles/20240412221958_03dd.png','name':'Nandanreddy'},
        // popup openers
        make_request: false,
        edit_request: false,
    }},
    methods: {
        formatISODate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString();
        },
        toggleAddRequest() {
            this.make_request = !this.make_request
        },
        toggleEditRequest() {
            this.edit_request = !this.edit_request
        },
        openBook(url) {
            const newTab = window.open(url, '_blank');
            if (newTab) newTab.focus();
        }
    },
    mounted(){
        setTimeout(()=>{
            axiosClient.get(`/api/books/${this.book_id}`)
            .then(resp => {
                console.log(resp)
                this.book = resp.data.book
                this.authors = resp.data.authors
                this.loading = false
            })
        }, 2000)
    },
    components: {
        addRequest, editRequest, reviews
    }
}
</script>

<style scoped>
.container {
    overflow: auto;
}
.book-container {
    padding: 5px;
    max-width: 1000px; width: 100%;
    background-color: white;
    margin: 30px auto;
    box-shadow: 0 0 4px 2px rgba(189,189,189,1);
}
.book-header {
    display: flex; flex-wrap:wrap;
}
.book-image {
    width: 210px; height: 295px;
}
.book-details {
    flex: 1;
    padding: 18px 15px 0 15px;
}
.book-title {
    font-weight: 300;
    line-height: 41px;
    white-space: normal;
    color: #212121;
    font-size: 30px;
    margin: 0 0 0 0;
    max-height: 120px; height: 100%;
    overflow: hidden;
}
.book-meta {
    margin-top: 9px;
    font-weight: 300;
    font-size: 21px;
    color: #006621;
    display: flex; gap: 9px;
}
.book-authors {
    max-height: 50px;
    text-align: left;
    font-size: 12px;
    line-height: 20px;
    overflow: hidden;
    margin-top: 18px;
    font-weight: 525;
    font-size: 18px;
    display: flex; flex-wrap: wrap; align-items: center;
}
.book-authors a {
    color: rgb(84, 18, 18); background-color: rgba(0, 128, 0, 0.459);
    padding: 0px 6px; border-radius: 10px; margin: 3px 6px;
}
.book-options {
    width: 100%; margin-top: 50px;
    display: flex; align-items: center; justify-content: space-evenly;
}
.book-options button {
    min-width: 90px; width: max-content;
    cursor: pointer;
    color: #212529;
    background-color: #ffc107;
    border-color: #ffc107;
    padding: 3px; border-radius: 5px;
}
.book-options button.blue {
    background-color: #718dcd; color: black;
    border-color: #718dcd;
}
.book-description {
    padding-top: 10px;
}
.book-description h4 {
    font-size: 18; padding-bottom: 6px;
}

/* reviews header */
.reviews-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px;
}
.reviews-header input, .reviews-header select{
    padding: 3px;
}
.reviews-body {
    display: flex; flex-direction: column;
    padding: 10px; overflow: auto; gap: 10px;
    border-top: 1px solid black;
}
/* make review */
.make-review {
    display: flex; flex-direction: column; align-items: center;
    border: 1px solid black; padding: 10px; border-radius: 10px;
}

.rating-box {
    width: 100%;
    display: flex; align-items: center; justify-content: space-between; gap: 6px;
}

textarea {
    width: 100%;
    height: 100px;
    resize: vertical;
    margin-bottom: 10px;
}

button {
    background-color: #30697b;
    color: white;
    padding: 10px 20px;
    border: none;
    border-radius: 5px;
    cursor: pointer;
}

button:hover {
    background-color: #225362;
}

/* Styling for stars */
.review-stars {
display: inline-block;
position: relative;
height: 50px;
line-height: 50px;
font-size: 50px;
}
.review-stars label {
position: absolute;
top: 0;
left: 0;
height: 100%;
cursor: pointer;
}
.review-stars label:last-child {
position: static;
}
.review-stars label:nth-child(1) {
z-index: 5;
}
.review-stars label:nth-child(2) {
z-index: 4;
}
.review-stars label:nth-child(3) {
z-index: 3;
}
.review-stars label:nth-child(4) {
z-index: 2;
}
.review-stars label:nth-child(5) {
z-index: 1;
}
.review-stars label input {
position: absolute;
top: 0;
left: 0;
opacity: 0;
}
.review-stars label .icon {
float: left;
color: transparent;
}
.review-stars label:last-child .icon {
color: #000;
}
.review-stars:not(:hover) label input:checked ~ .icon,
.review-stars:hover label:hover input ~ .icon {
color: yellow;
}
.review-stars label input:focus:not(:checked) ~ .icon:last-child {
color: #000;
text-shadow: 0 0 5px yellow;
}
/* loading reviews */
.review {
    width: 100%; border: 1px solid black; border-radius: 8px;
    min-height: 60px; padding: 5px;
}
.load-more-reviews {
    text-align: center;
}
.load-more-reviews button {
    background-color: black; color: white; padding: 3px; border-radius: 9px;
}


/* Skeleton styles */
@keyframes skeleton-loading {
  0% {
    background-color: hsl(200, 20%, 80%);
  }
  100% {
    background-color: hsl(200, 20%, 95%);
  }
}
.skeleton-container {
    padding: 5px 5px 5px 5px;
    max-width: 900px; width: 100%;
    height: 358px;
    background-color: white;
    margin: 30px auto;
    box-shadow: 0 0 4px 2px rgba(189,189,189,1);
}
.skeleton-header {
    width: 900px;
    display: flex; flex-wrap:nowrap;
}
.skeleton-image {
    width: 300px; height: 295px;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
.skeleton-details {
    display: flex; flex-direction: column; gap: 10px;
    width: 100%;
}
.skeleton-meta {
    display: flex;
    margin-left: 10px;
    width: 40%; height: 60px;
    animation: skeleton-loading 0.5s linear infinite alternate;  
}
.skeleton-description {
    width: 100%; height: 30px;
    margin-top: 10px;
    animation: skeleton-loading 0.5s linear infinite alternate; 
}

</style>