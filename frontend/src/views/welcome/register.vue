<template>
    <div class="popup">
        <h1>Create account to read</h1>
        <p>Create a account to read on any device at any time</p>
        <!-- <span>{{ JSON.stringify(FormData) }}</span> -->
        <form class="bar" @submit.prevent="submitForm">
            <label for="email">Email <span class="required">*</span></label>
            <input type="email" required id="email" placeholder="Email" v-model="FormData.email">
            <br>
            <label for="f_name">First name <span class="required">*</span></label>
            <input type="text" required id="f_name" v-model="FormData.f_name">
            <br>
            <label for="l_name">Last name</label>
            <input type="text" id="l_name" v-model="FormData.l_name">
            <br>
            <label for="password">Password <span class="required">*</span></label>
            <input type="password" required id="password" placeholder="Password" v-model="FormData.password">
            <br>
            <label for="re-password">Re-enter password <span class="required">*</span></label>
            <input type="password" required id="re-password" placeholder="Re-enter password" v-model="FormData.password1" @blur="checkPasswords">
            <br>
            <label for="dob">Date of birth <span class="required">*</span></label>
            <input type="date" required id="dob" placeholder="Date of borth" v-model="FormData.dob">
            <br>
            <div class="profile-upload">
                <img class="profile-upload-view" :src="uploadImageUrl" alt="">
                <div class="profile-upload-upload">
                    <label for="profile_pic">Profile picture</label>
                    <input class="fileInputElement" @change="uploadImage" type="file" id="profile_pic" accept="image/*">
                </div>                
            </div>
            <br>
            <button>Enter</button>
        </form>
        <p class="alert" v-if="response">{{ response }}</p>        
    </div>

</template>

<script>
import { register } from '@/services/auth'
import { upload, getUrl } from '@/services/fileHandle'
import axiosClient from '@/services/axios';

export default {
    data() {
        return {
            FormData: {email: this.$store.state.user.email, f_name:"NandanReddy", l_name:"Parnapalli", password:"Passkey123", password1:"Passkey123", dob:"2004-04-09", 'image-id':'' },
            uploadImageUrl: '',
            response: ''
        }
    },
    methods: {
        async uploadImage(event) {
            const file = event.target.files[0]
            this.FormData['image-id'] = await upload('profile-image',file,)
            this.uploadImageUrl = this.FormData['image-id']
        },
        async submitForm() {
            if (this.FormData.email && this.checkPasswords() && this.FormData.f_name && this.FormData.dob) {
                register.call(this,this.FormData)
            } else {
                this.response = 'Please fill details'
            }
        },
        checkPasswords() {
            if (this.FormData.password != '' && this.FormData.password != this.FormData.password1) {
                this.response = 'Re-entered passwords not matching'
                return 0
            } else {
                this.response = ''
                return 1
            }
        }
    },
    async mounted() {
        var response
        response =   await getUrl('profile-image','/static/images/profiles/default.png')
        this.uploadImageUrl = response['url']
    },
    components: {
        
    }
};
</script>

<style scoped>
.popup {
    border-image: linear-gradient(#f6b73c, #4d9f0c) 30; border-width: 4px; border-style: solid;
    background-color: #CEC5AD;
    border-radius: 5px; padding: 30px;
    box-shadow: 0 60px 40px -30px rgba(0, 0, 0, 0.1);
    margin-top: 100px; margin-bottom: 100px;
    height: max-content;
    max-width: 500px; width: 100%;
}
h1, p {
    color: #38697F;
    padding: 5px; text-align: center;
}
label {
    color: black;
}
form.bar {
    display: flex; flex-direction: column;
    margin-top: 10px;
}
input, button {
    padding: 10px;
}
button {
    margin: 0px 9px 5px 9px; cursor: pointer;
}
.fileInputElement {
    background-color: #38697F;
    color: white; width: 100%;
}
span.required {
    color: red;
}
.alert {
    background-color: red; color: white;
    text-align: center; margin-top: 20px;
}

.profile-upload {
    display: flex; border: 1px solid black;
    border-radius: 10px;
}
img.profile-upload-view {
    aspect-ratio: 1/1;
    width: 150px; padding: 10px;
    object-fit: cover;
}
.profile-upload-upload {
    display: flex; flex-direction: column; justify-content: center;
    padding-right: 10px; width: auto;
}
</style>