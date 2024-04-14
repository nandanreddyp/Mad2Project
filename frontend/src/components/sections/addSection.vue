<template>
    <div class="popup-bg">
        <div class="popup">
            <div class="popup-header">Create Section</div>
            <div class="body">

                <div class="section-description">
                    <textarea placeholder="Share details of your own experience about this section"></textarea>
                </div>
            </div>
            <div class="popup-options">
                <button class="ok">Submit</button>
                <button class="cancel" @click="toggleAddSection">Cancel</button>
            </div>
        </div>
    </div>
</template>

<script>
import axiosClient from '@/services/axios'

export default {
    data() {return {
        formdata: {
            rating: '',
            description: '',
        }
    }},
    methods:{
        uploadReview(){
            axiosClient.post(`/api/reviews`)
            .then(resp=>{

            })
        }
    },
    props: {
        toggleAddSection: Function, 
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
.ratings-container {
    display: flex; flex-direction: column; align-items: center;
    padding: 25px;
}
.review-stars {
    display: flex;
    align-items: center;
}
.review-stars input {
    display: none;
}
.section-description {
    width: 100%;
}
.section-description textarea {
    width: 100%; height: 300px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    margin: 16px 0px;
    line-height: 1.5rem;
    resize: none;

    font-family: Roboto, Arial, sans-serif;
    font-size: 0.9rem;
    letter-spacing: .00625em;
    font-weight: 400;
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
.popup-options button.cancel {
    border: 1px solid black;
    color: #333;
}
.popup-options button:hover {
    transform: translate(-2px, 1px);
}
</style>
