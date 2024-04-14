<template>
    <div class="container">
        <div style="display: flex; gap: 10px; padding: 10px">
            <button style="flex: 1;" @click="toggleAddBook">Create Book</button><button style="flex: 1;" @click="toggleEditBook">Edit Book</button>
        </div>
        <addBook v-if="add_book" :toggleAddBook="toggleAddBook"/>
        <editBook v-if="edit_book" :toggleEditBook="toggleEditBook"/>
    </div>
</template>
<script>
import addBook from '@/components/books/addBook.vue';
import editBook from '@/components/books/editBook.vue';

export default{
    components: { addBook, editBook },
    data(){return{
        add_book: false,
        edit_book: false,
    }},
    props: {
        // name: type,
    },
    methods: {
        toggleAddBook() {
            this.add_book = !this.add_book
        },
        toggleEditBook() {
            this.edit_book = !this.edit_book
        }
    },
    mounted(){

    },
    watch: {

    }
}
</script>
<style scoped>
.container {
    overflow: auto;
}
</style>