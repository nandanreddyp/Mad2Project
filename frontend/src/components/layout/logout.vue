<template>
    <div class="popup-bg">
        <div class="popup">
                <h2>Are you sure to logout?</h2>
                <div class="wide_options">
                    <button @click="runlogout">Yes</button><button @click="closelogout">No</button>
                </div>

        </div>        
    </div>
</template>

<script>
import { logOut } from '@/services/auth.js'


export default {
    name: 'logoutView',
    data() {
        return {
        }
    },
    props: {
        toggleLogout: Function,
    },
    methods: {
        runlogout() {
            logOut.call(this)
        },
        closelogout() {
            this.toggleLogout()
        }
    },
    components: {
    }
};
</script>

<style scoped>
.popup-bg {
    position: fixed; z-index: 1000;
    top: 0; left: 0;
    width: 100%; height: 100%;
    display: flex; justify-content: center;
    align-items: center;
    background-color: rgba(0, 0, 0, 0.473);
}
.popup-bg > .popup {
    text-align: center;
    max-width: 350px; width: 100%;
    max-height: 125px; height: 100%;
    background-color: #fff;
    padding: 10px; border-radius: 10px;
    display: flex; flex-direction: column; align-items: center; justify-content: center;
}
.popup h2 {
    padding: 6px;
}
.wide_options {
    width: 100%; padding-top: 6px;
    display: flex; justify-content: space-evenly;
}
.wide_options > button{
    padding: 5px; border-radius: 10px;
    width: 50px; cursor: pointer;
}
</style>