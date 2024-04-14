import { toast } from 'vue3-toastify'
import 'vue3-toastify/dist/index.css'

export function userExistsToast() {
    toast.warning('User exists with this email, please login to continue',{
        autoClose: 4000,
    })
}

export function loginToContinueToast() {
    toast.success('Please login to continue',{
        autoClose: 4000,
    })
}

export function registerToast() {
    toast.success('Account created, please login',{
        autoClose: 4000,
    })
}
export function loginToast() {
    toast.success('Welcome back!',{
        autoClose: 4000,
    })
}

export function formSubmitToast() {
    toast.success('Submitted form data',{
        autoClose: 4000,
    })
}

export function formUpdateToast() {
    toast.success('Updated form data',{
        autoClose: 4000,
    })
}

export function formDeleteToast() {
    toast.error('Deleted form data!',{
        autoClose: 4000,
    })
}