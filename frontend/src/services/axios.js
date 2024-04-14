import axios from 'axios'
import store from './vuex'

const axiosClient = axios.create({
    baseURL: 'http://127.0.0.1:5000',
    withCredentials: true,
    headers: {
        'Content-Type':'application/json',
        Accept: 'application/json'
    }
})

axiosClient.interceptors.request.use(
    config => {
        const access_token = localStorage.getItem('access_token')
        if (access_token) {
            config.headers.Authorization = `Bearer ${access_token}`
        }
        return config
    },
    error => {
        return Promise.rejectt(error);
    }
)
axiosClient.interceptors.response.use(
    response => {
        return response;
    },
    error => {
        if (error.response.status === 401) {
            console.log('Authentication error')
            store.commit('removeUser')
            window.location.href = '/login'
            return error
        }
        return Promise.reject(error)
    }
)

export default axiosClient