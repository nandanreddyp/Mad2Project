<!--
show graphs
-->
<template>
    <div class="img-container">
        <img :src="img1" alt="">
        <br>
        <img :src="img2" alt="">
        <br>
        <img :src="img3" alt="">
    </div>
</template>
<script>
import axiosClient from "@/services/axios"

export default{
    data() {return{
        img1: '',
        img2: '',
        img3: '',
    }},
    mounted() {
        axiosClient.get('/api/librarian/analytics')
        .then(resp => {
            console.log(resp)
            this.img1 = resp.data.first
            this.img2 = resp.data.second
            this.img3 = resp.data.third
        })
    }
}

</script>
<style>
.img-container {
    margin: 10px 0px;
    width: 100%; display: flex; flex-direction: column; justify-content: center;
}
.img-container img {
    width: 50%; margin: auto;
}
</style>