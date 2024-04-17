 <template>
    <div class="popup">
        <h1>Welcome back!</h1>
        <p>Login to your account to continue.</p>
        <form class="bar" @submit.prevent="submitForm">
            <label for="email">Email</label>
            <input type="email" id="email" placeholder="Email" v-model="FormData.email">
            <br>
            <label for="password">Password</label>
            <input type="password" id="password" placeholder="Password" v-model="FormData.password">
            <button type="submit">Login</button>
        </form>
        <p class="alert" v-if="response">{{ response }}</p>
    </div>
</template>

<script scoped>
import { logIn } from '@/services/auth'
export default {
    data() {
        return {
            FormData: {
                email: this.$store.state.user.email , password: '',
            },
            response: ''
        }
    },
    methods: {
        async submitForm() {
            if (this.FormData.email && this.FormData.password) {
                logIn.call(this,this.FormData)
            } else {
                this.response = 'Please fill details'
            }
        }
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
    scrollbar-width: thin;
    height: max-content;
    max-width: 500px; width: 100%;
}
h1, p {
    color: #38697F;
    padding: 5px; text-align: center;
}
label {
    color: #150303;
}
form.bar {
    display: flex; flex-direction: column;
    margin-top: 15px;
}
input, button {
    padding: 10px; 
}
button {
    margin: 25px 9px 5px 9px;
    cursor: pointer;
}
.alert {
    background-color: red; color: white;
    text-align: center; margin-top: 20px;
}
</style>