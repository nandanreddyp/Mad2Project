<template>
    <div class="popup-bg">
        <div class="popup">
            <div class="popup-header">Edit Author</div>
            <div class="body">
                <form ref="myForm" id="author-form">

                    <label for="name">Author Name</label>
                    <input v-model="formdata.name" ref="name" type="text" id="name" name="name" required><br><br>

                    <div class="author-description">
                        <label for="description">Description</label>
                        <textarea v-model="formdata.description" ref="description" id="description" name="description" placeholder="Description about this author"></textarea>
                    </div><br>

                    <label for="img_file">Cover Image <span style="font-size:10px">(Select new file, only if want chagne)</span></label>
                    <div style="display: flex; justify-content: center; margin-bottom: 6px;">
                        <img id="selectedImgPreview" class="" src="" alt=""> <!--add visible class to show-->
                    </div>
                    <input @change="showSelectedImage" ref="IMG" type="file" id="img_file"  accept="image/*"><br><br>

                </form>
            </div>
            <div class="popup-options">
                <button class="ok" @click="checkForm" >Submit</button>
                <button class="delete" @click="toggleDeletePopup"    >Delete</button>
                <button class="cancel" @click="toggleEditAuthor">Cancel</button>
            </div>
        </div>
    </div>
    <deletePopup v-if="show_delete_popup" @confirm="delete_post=true; show_delete_popup = false" @cancel="show_delete_popup = false" />
</template>

<script>
import axiosClient from '@/services/axios'

import deletePopup from '@/components/layout/delete.vue'

export default {
    components: {
        deletePopup,
    },
    props: {
        LoadAuthor: Function, toggleEditAuthor: Function, updatedToast: Function,
    },
    data() {return {
        author_id: this.$route.params.id,
        formdata: {
            name: '',
            description: '',
            image: null,
        },
        // delete
        show_delete_popup: false,
        delete_post: false,
    }},
    methods:{
        toggleDeletePopup(){
            this.show_delete_popup = true
        },
        showSelectedImage() {
            const image_file = document.getElementById("img_file");
            const image_file_preview = document.getElementById("selectedImgPreview");
            const files = image_file.files[0];
            if (files) {
                image_file_preview.classList.add('visible')
                const fileReader = new FileReader();
                fileReader.readAsDataURL(files);
                fileReader.addEventListener("load", function () {
                image_file_preview.src = this.result
                });    
            } else {
                image_file_preview.classList.remove('visible')
                image_file_preview.src = ''
            }
        },
        checkForm(){
            if (this.$refs.myForm.reportValidity()) {
                this.formdata.image_file = this.$refs.IMG.files[0]
                this.submitForm()
            }
        },
        submitForm() {
            axiosClient.put(`/api/authors/${this.author_id}`,this.formdata,{
                headers:{
                    'Content-Type': 'multipart/form-data',
                }
            })
            .then(resp => {
                this.toggleEditAuthor()
                this.LoadAuthor()
                this.updatedToast()
            })
        },
        deleteForm() {
            axiosClient.delete(`/api/authors/${this.author_id}`)
            .then(resp => {
                this.$router.push({ name: 'librarian-authors', query: { msg: 'deleted'}})
            })
        },
        LoadAuthorData() {
            axiosClient.get(`/api/authors/${this.author_id}`)
            .then(resp => {
                this.formdata.name = resp.data.author.name
                this.formdata.description = resp.data.author.description
            })
        }
    },
    watch: {
        delete_post(to, from) {
            this.deleteForm()
        }
    },
    mounted() {
        this.LoadAuthorData()
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
    margin-bottom: 5px;
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
.author-description {
    width: 100%;
}
.author-description textarea {
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

/* form css */
#author-form {
    width: 100%;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
input[type="file"],
input[type="date"],
textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}

/* selected image */
#selectedImgPreview.visible {
    display: unset;
    width: 100px; background-color: black; height: 150px;
    object-fit: cover;
}
#selectedImgPreview {
    display: none;
}



/* footer */
.popup-options {
    width: 100%; margin-top: 5px;
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
.popup-options button.delete {
    border: 1px solid black;
    color: #333;
}


.popup-options button.delete:hover {
    border: 1px solid red;
}
.popup-options button:hover {
    transform: translate(-2px, 1px);
}
</style>
