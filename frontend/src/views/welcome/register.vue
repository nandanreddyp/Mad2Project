<template>
    <div class="popup">
        <h1>Create account to read</h1>
        <p>Create a account to read on any device at any time</p>
        <form class="bar" @submit.prevent="submitForm">
            <label for="email">Email <span class="required">*</span></label>
            <input type="email" required id="email" placeholder="Email" v-model="formdata.email">
            <br>
            <label for="f_name">First Name <span class="required">*</span></label>
            <input type="text" required id="f_name" placeholder="First Name" v-model="formdata.f_name">
            <br>
            <label for="l_name">Last Name</label>
            <input type="text" id="l_name" placeholder="Last Name" v-model="formdata.l_name">
            <br>
            <label for="password">Password <span class="required">*</span></label>
            <input type="password" required id="password" placeholder="Password" v-model="formdata.password">
            <br>
            <label for="re-password">Re-enter Password <span class="required">*</span></label>
            <input type="password" required id="re-password" placeholder="Re-enter password" v-model="formdata.password1" @blur="checkPasswords">
            <br>
            <label for="dob">Date Of Birth <span class="required">*</span></label>
            <input type="date" required id="dob" placeholder="Date of borth" v-model="formdata.dob">
            <br>
            <label for="profile_pic">Profile Picture</label>
            <input class="fileInputElement" type="file" id="profile_pic" accept="image/*" ref="img_file" @change="handleFileChange">
            <br>
            <button type="submit">Enter</button>
        </form>
        <p class="alert" v-if="response">{{ response }}</p>        
    </div>
</template>

<script>
import { register } from '@/services/auth'

export default {
    data() {
        return {
            formdata: {email: this.$store.state.user.email, f_name:"User", l_name:"", password:"12345678", password1:"12345678", dob:"2004-04-09", img_file:"" },
            response: ''
        }
    },
    methods: {
        submitForm() {
            register.call(this,this.formdata)
        },
        checkPasswords() {
            if (this.formdata.password != '' && this.formdata.password != this.formdata.password1) {
                this.response = 'Re-entered passwords not matching'
                return 0
            } else {
                this.response = ''
                return 1
            }
        },
        handleFileChange(event) {
            this.formdata.img_file = event.target.files[0]
        }
    },
    mounted() {

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


</style>