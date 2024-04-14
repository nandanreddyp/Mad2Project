import axiosClient from "./axios";

import { loginToContinueToast } from "@/services/toast.js"

export function checkUser(form) {
    axiosClient.get('/api/auth/login?email='+form.email)
    .then(resp => {
      this.$router.push('/login')
    }).catch(err => {
        if (err.response) {
            this.$store.commit('setUser',{email:form.email})
            this.$store.state.isAuthenticated = false
            if (err.response.status === 404) {
                return this.$router.push('/register')
            }
        }
    })
}

export function register(form) {
    axiosClient.post('/api/auth/register',form)
    .then(resp => {
      if (resp.status == 200 ) {
        this.$store.commit('setUser',{email : form.email})
        this.$router.push('/login')
      }
    }).catch(error => {
      if (error.response) { // request was made but server had error
        if (error.response.status === 409) {
          this.$store.commit('setUser',{email : form.email})
          this.$router.push('/login')
        }
      } else {
        this.response = 'Fill required details'
      }
    })
}

export function logIn(form) {
    axiosClient.post('/api/auth/login',form)
    .then(resp => {
        if (resp.data.access_token) {
          this.$store.commit('setUser',resp.data.user)
          this.$store.commit('setAuthentication',true)
          localStorage.setItem('access_token', resp.data.access_token);
        if (resp.data.user.role === 'librarian') {
          this.$router.push('/librarian')
        } else {
          this.$router.push('/')
        }
        }
    }).catch(error => {
        if (error.response) { 
        if (error.response.status === 404) {
            this.response = 'Check email or password'
        }
        } else if (error.request) {
        ;
        } else {
        ;
        }
    })
}

export function logOut() {
    axiosClient.post('/api/auth/logout')
    .then(resp => {
      if (resp.status == 200) {
        this.$store.commit('removeUser')
        localStorage.removeItem('access_token');
        this.$router.push('/in')
      }
    }).catch(error => {
      try {
        this.$store.commit('removeUser')
        localStorage.removeItem('access_token');
        this.$router.push('/in')
      } finally {
        ;
      }
    })
}