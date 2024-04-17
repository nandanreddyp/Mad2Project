import axiosClient from "./axios";

export function checkUser(formdata) {
    axiosClient.get('/api/auth/login?email='+formdata.email)
    .then(resp => {
      this.$store.commit('setUser',{email:formdata.email})
      if (resp.data.found) {
        this.$router.push({name:'login',query:{found:true}})
      } else {
        this.$router.push({name:'register',query:{found:false}})
      }
    }).catch(err => { console.log(err) })
}

export function register(formdata) {
    axiosClient.post('/api/auth/register',formdata,{
      headers:{'Content-Type': 'multipart/form-data',}
    })
    .then(resp => {
      this.$store.commit('setUser',{email : formdata.email})
      if (resp.data.exists) {
        this.$router.push({name:'login',query:{exists:true}})
      } else {
        // created login
        this.$router.push({name:'login',query:{exists:false}})
      }
    }).catch(err => { console.log(err) })
}


import { toast } from 'vue3-toastify'
export function logIn(form) {
    axiosClient.post('/api/auth/login',form)
    .then(resp => {
        if (resp.data.access_token) {
          this.$store.commit('setUser',resp.data.user)
          this.$store.commit('setAuthentication',true)
          localStorage.setItem('access_token', resp.data.access_token);
          if (resp.data.user.role === 'librarian') {
            this.$router.push({name:'librarian-home',query:{login:'success'}})
          } else {
            this.$router.push({name:'user-home',query:{login:'success'}})
          }
        } else {
          toast.error('Incorrect email or password!')
          this.response = 'Incorrect password or email'
        }
    }).catch(err => { console.log(err) })
}

export function logOut() {
    axiosClient.post('/api/auth/logout')
    .then(resp => {
      if (resp.status == 200) {
        this.$store.commit('removeUser')
        localStorage.removeItem('access_token');
        this.$router.push({name:'welcome',query:{logout:true}})
      }
    }).catch(error => {
      alert(error)
    })
}