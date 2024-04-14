<template>
    <div class="popup-bg">
        <div class="popup">
            <h1 class="popup-header">{{ book_data.name }}</h1>
            <div class="body">
                <div class="book-img">
                    <img :src="book_data.img_path" alt="">
                </div>
                <div class="form-group">
                    <label for="return-date">Return Date:</label>
                    <input type="datetime-local" class="datetime-local" id="return-date" min="" name="return-date" required>
                </div>
                <div class="form-check">
                    <input type="checkbox" class="form-check-input" id="terms-checkbox" required>
                    <label for="terms-checkbox" class="form-check-label">I agree to the terms and conditions</label>
                </div>
            </div>
            <div class="popup-options">
                <button class="ok" @click="submitForm">Update</button>
                <button class="delete" @click="toggleDeletePopup">Delete</button>
                <button class="cancel" @click="toggleEditRequest">Cancel</button>
            </div>
        </div>
    </div>
    <deletePopup v-if="show_delete_popup" @confirm="delete_post=true; show_delete_popup = false" @cancel="show_delete_popup = false" />
</template>

<script>
import { formUpdateToast, formDeleteToast } from '@/services/toast'

import axiosClient from '@/services/axios'

import deletePopup from '@/components/layout/delete.vue'

export default {
    components:{ deletePopup },
    data() {return {
        book_data : {
            name:'Rich dad poor dad', img_path:'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSmuHAxZf3WqfmvsT2WtdKur-pA7SBPk1EUqK-AL96kgg&s'
        },
        min_date : new Date(new Date().getTime() - (new Date().getTimezoneOffset() * 60000)).toISOString().slice(0, 16),
        formdata: {
            book_id:'1',
            return_date:''
        },
        // delete
        show_delete_popup: false,
        delete_post: false,
    }},
    methods:{
        requestbook(){
            axiosClient.post(`/api/requests`)
            .then(resp=>{

            })
        },
        toggleDeletePopup() {
            this.show_delete_popup = true
        }
    },
    props:  {
        toggleEditRequest: Function,
    }
}
</script>

<style scoped>
/* popup */
.popup-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}
.popup {
    background-color: #fff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    max-width: 580px;
    width: 100%;
    max-height: 550px;
    height: 100%;
    /* overflow-y: auto; */
    display: flex; flex-direction: column;
}

/* heading */
.popup-header {
    font-family: Roboto,Arial,sans-serif;
    font-size: 20px;
    font-weight: 400;
    letter-spacing: 0;
    line-height: 26px;
    color: #e8e8e8;
    overflow: hidden;
    text-align: left;
    text-overflow: ellipsis;

    width: 100%;
    color: #2a2929;
    overflow: hidden;
    white-space: nowrap; /* Prevents wrapping of text */
    text-overflow: ellipsis; /* Add ellipsis for overflowed text */
    margin: 0px auto; /* Center the text horizontally */
    text-align: center;
}

/* body */
div.body {
    flex: 1; overflow-y: auto;
    display: flex; flex-direction: column;
    align-items: center;
}
/**/
.book-img img {
    width: 178px; height: 284px; object-fit: cover;
}
.form-group {
    width: 100%; display: flex; align-items: center; justify-content: center; gap: 10px; padding: 5px;
    margin-top: 30px;
}
.form-check {
    width: 100%; display: flex; align-items: center; justify-content: center; gap: 10px; padding: 20px;
}
label {
    font-weight: bold;
    font-size: 16px;
}

/* footer */
.popup-options {
    width: 100%; /* Occupy full width of the popup */
    display: flex; justify-content: space-evenly;
}
.popup-options button {
    padding: 10px 20px;
    margin: 0 10px;
    color: #333;
    border: none;
    border-radius: 50px;
    cursor: pointer;
}
.popup-options button.ok {
    color: rgb(32, 33, 36);
    background-color: rgb(138,180,248);
}
.popup-options button.delete {
    border: 1px solid red;
    color: #333;
}
.popup-options button.delete:hover {
    background-color: red; color: white;
}

.popup-options button.cancel {
    border: 1px solid black;
    color: #333;
}
.popup-options button:hover {
    transform: translate(-2px, 1px);
}
</style>
