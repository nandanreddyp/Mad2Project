<template>
    <div class="popup-background">
        <div class="popup-background-blur"></div>
        <div class="picker-dialog">
            <div class="popup-header">
                <h2>Select books to add</h2>
                <svg @click="closePopup" height="25px" id="Layer_1" style="cursor: pointer;enable-background:new 0 0 512 512;" version="1.1" viewBox="0 0 512 512" width="25px" xml:space="preserve" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink"><path d="M443.6,387.1L312.4,255.4l131.5-130c5.4-5.4,5.4-14.2,0-19.6l-37.4-37.6c-2.6-2.6-6.1-4-9.8-4c-3.7,0-7.2,1.5-9.8,4  L256,197.8L124.9,68.3c-2.6-2.6-6.1-4-9.8-4c-3.7,0-7.2,1.5-9.8,4L68,105.9c-5.4,5.4-5.4,14.2,0,19.6l131.5,130L68.4,387.1  c-2.6,2.6-4.1,6.1-4.1,9.8c0,3.7,1.4,7.2,4.1,9.8l37.4,37.6c2.7,2.7,6.2,4.1,9.8,4.1c3.5,0,7.1-1.3,9.8-4.1L256,313.1l130.7,131.1  c2.7,2.7,6.2,4.1,9.8,4.1c3.5,0,7.1-1.3,9.8-4.1l37.4-37.6c2.6-2.6,4.1-6.1,4.1-9.8C447.7,393.2,446.2,389.7,443.6,387.1z"/></svg>
            </div>
            <div class="popup-search-sort">
                <form class="main-header-search" @submit.prevent="" >
                    <input placeholder="search book" type="search" id="search">
                    <button>
                        <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" width="20" height="20" viewBox="0 0 50 50">
                            <path d="M 21 3 C 11.621094 3 4 10.621094 4 20 C 4 29.378906 11.621094 37 21 37 C 24.710938 37 28.140625 35.804688 30.9375 33.78125 L 44.09375 46.90625 L 46.90625 44.09375 L 33.90625 31.0625 C 36.460938 28.085938 38 24.222656 38 20 C 38 10.621094 30.378906 3 21 3 Z M 21 5 C 29.296875 5 36 11.703125 36 20 C 36 28.296875 29.296875 35 21 35 C 12.703125 35 6 28.296875 6 20 C 6 11.703125 12.703125 5 21 5 Z"></path>
                        </svg>
                    </button>
                </form>
                <div class="sort">
                    Sort by
                    <select name="sort" id="sort">
                        <option value="latest" selected>Latest</option>
                        <option value="oldest">Oldest</option>
                        <option value="asc">Name (A-Z)</option>
                        <option value="desc">Name (Z-A)</option>
                    </select>
                </div>
            </div>
            <div class="popup-results">
                <h3 style="padding-left: 6px;">Latest books</h3>
                <div class="books-list" v-if="!loading">
                    <div class="book-list-item" v-for="book in books" :key="book.id">
                        <img class="book-list-logo" :src="book.img_path" alt="">
                        <div class="book-list-details">
                            <h2>{{book.name}}</h2>
                            <div class="book-meta">
                                <span>{{ book.page_count + ' Pages' }}</span>
                                <span>{{'Published on: '+ formatISODate(book.publication_date) }}</span>
                                <span>{{'Ratings: ' + book.rating}}</span>
                            </div>
                            {{book.description}}
                        </div>
                        <div class="book-button">
                            <div v-if="!book.is_associated" @click="addBook(book.id)" class="book-button-add">
                                Add
                            </div>
                            <div v-else @click="removeBook(book.id)" class="book-button-remove">
                                Remove
                            </div>
                        </div>
                    </div>
                </div>
                <div class="books-list" v-if="loading"> <!--content skeleton-->
                    <div class="book-list-item" v-for="n in 3" :key="n">
                        <div class="skeleton-image"></div>
                        <div class="skeleton-details">
                            <div class="skeleton-title"></div>
                            <div class="skeleton-meta">
                                <span></span>
                            </div>
                            <div class="skeleton-description"></div>
                        </div>
                    </div>
                </div> 
            </div>
        </div>
    </div>
</template>

<script>
import axiosClient from '@/services/axios'

export default {
    data() { return {
        id: this.$route.params.id,
        books: [],
        loading: true,
        perpage: 7,
    }},
    props: {
        toggleAddBooks: Function, LoadAuthor: Function, type: String, updatedToast: Function, reloadPage: Function,
    },
    mounted() {
        this.fetchBooks()
    },
    unmounted(){

    },
    methods: {
        formatISODate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString();
        },
        fetchBooks() {
            let url
            if (this.type=='author') {
                url = `/api/authors/${this.id}/add/books`
            } else {
                url = `/api/sections/${this.id}/add/books`
            }
            axiosClient.get(url)
            .then( resp => {
                console.log(resp)
                this.books = resp.data.books
                this.loading = false
            })
        },
        addBook(book_id) {
            const index = this.books.findIndex(book => book.id === book_id)
            if (index !== -1) {
                this.books[index].is_associated = true
                let url
                if (this.type=='author') {
                    url = `/api/authors/${this.id}/add/books/${book_id}`
                } else {
                    url = `/api/sections/${this.id}/add/books/${book_id}`
                }
                axiosClient.post(url)
            }
        },
        removeBook(book_id) {
            const index = this.books.findIndex(book => book.id === book_id)
            if (index !== -1) {
                this.books[index].is_associated = false
                let url
                if (this.type=='author') {
                    url = `/api/authors/${this.id}/add/books/${book_id}`
                } else {
                    url = `/api/sections/${this.id}/add/books/${book_id}`
                }
                axiosClient.delete(url)
            }
        },
        closePopup() {
            this.toggleAddBooks()
            this.updatedToast()
            this.reloadPage()
        }
    }
}
</script>

<style scoped>
.popup-background-blur {
    background: #000; opacity: 0.5;
    width: 100%; height: 100%;
    position: absolute; top: 0; left: 0;
}
.picker-dialog {
    opacity: 1;
    background-color: #fff;
    box-shadow: 0 .25rem 1rem rgba(0,0,0,.12),0 0 .25rem rgba(0,0,0,.12);
    position: absolute;
    z-index: 10;
    top: 50%; left: 50%; transform: translate(-50%, -50%);
    max-width: 950px; width: 100%; max-height: 590px; height: 100%;
    display: flex; flex-direction: column;
}
/*header*/
.popup-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 18px 9px 9px 9px;
}
/*search-sort*/
.popup-search-sort {
    display: flex; align-items: center; justify-content: space-between;
    padding: 5px 5px;
    border-bottom: 1px solid black;
}
.main-header-search {
    display: flex; align-items: center; gap: 10px;
    padding: 0 10px; height: 30px;
    border: 1px solid black; border-radius: 50px;
    width: 50%;
}
.main-header-search > input {
    padding: 6px;
    border: none; background: none;
    width: 100%;
}
.main-header-search > input:focus {
    outline: none;
}
.main-header-search > button {
    border: none; background: none;
}
.main-header-search > button:hover {
    cursor: pointer;
}
/*results*/
.popup-results {
    flex: 1;
    overflow-y: auto;
    scrollbar-width: thin;
}
.books-list {
    width: 100%;
    padding: 5px;
    display: flex;
    flex-direction: column;
    font-size: 11px;
}
.book-list-item {
    display: flex;
    height: 97px;
    margin-bottom: 20px;
    overflow-y: hidden;
    position: relative;
}
.book-list-logo {
    height: 98px;
    aspect-ratio: 15/18;
    margin-right: 10px;
}
.book-list-details h2 {
    font-weight: 500;
    font-size: 16px;
    max-height: 38px; padding-bottom: 5px;
    overflow: hidden;
}
.book-meta {
    display: flex;
    flex-wrap: nowrap;
    gap: 5px;
    letter-spacing: 0;
    font-size: 13px;
    color: #006621;
    padding-bottom: 5px;
}
/*button to add or remove*/
.book-button {
    position: absolute;
    right: 25px; margin-top: 5px;
    cursor: pointer;
}
.book-button-add {
    padding: 3px; width: 50px;
    background-color: green; color: white;
    text-align: center; border-radius: 5px;
}
.book-button-remove {
    padding: 3px; width: 50px;
    background-color: red; color: white;
    text-align: center; border-radius: 5px;
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
.skeleton {
    background-color: #f0f0f0;
    overflow: hidden;
}
.skeleton-image {
    height: 98px;
    aspect-ratio: 15/18;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
.skeleton-details {
    flex: 1;
    padding: 10px;
}
.skeleton-title {
    width: 60%;
    height: 16px;
    margin-bottom: 8px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
.skeleton-meta {
    display: flex;
    margin-bottom: 8px;
}
.skeleton-meta span {
    width: 30%;
    height: 12px;
    margin-right: 10px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
.skeleton-description {
    width: 100%;
    height: 48px;
    background-color: #ddd;
    animation: skeleton-loading 0.5s linear infinite alternate;
}
</style>