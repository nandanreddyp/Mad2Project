<template>
    <div class="popup">
        <h1>There is no friend as loyal as a book.</h1>
        <p>Ready to read? Enter your email to create or login to your account.</p>
        <form class="bar" action="" @submit.prevent="checkUser">
            <input type="email" id="email" placeholder="Email" v-model.lazy="form.email">
            <button type="submit">Enter</button>
        </form>
        <p v-if="response">{{ response }}</p>
    </div>
</template>

<script>
import { checkUser } from '@/services/auth.js'
export default {
    name: 'welcome',
    components: [],
    data() {return {
        form: { email: ''},
        response: '',
    }},
    methods: {
        checkUser() {
            if (this.form.email){
                checkUser.call(this,this.form)
            }
        }
    }
}
</script>

<style scoped>
.popup {
    border-image: linear-gradient(#f6b73c, #4d9f0c) 30; border-width: 4px; border-style: solid;
    background-color: #CEC5AD;
    padding: 30px; max-width: 500px; width: 100%;
    position: absolute; top: 50%; left: 50%;
    transform: translate(-50%,-50%);
    text-align: center;
}
.popup > p {
    padding: 5px;
}
h1, p {
    color: #38697F;
}
form.bar {
    display: flex; justify-content: center;
    width: 100%; margin-top: 6px;
}
form.bar > input {
    width: 80%; padding: 10px;
}
form.bar > button {
    padding: 10px; cursor: pointer;
}
</style>
