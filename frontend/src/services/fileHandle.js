import axiosClient from "./axios";

const axiosConfig = {
    headers: {
        'accept': 'application/json',
        'Accept-Language': 'en-US,en;q=0.8',
        'Content-Type': 'multipart/form-data'
    }
}
var requestPromise

export async function getUrl(type,file_path) {
    let data = new FormData(); let url;
    if (type==='profile-image'){
        url = `/api/files/images/profiles?path=${file_path}`
    } else if (type==='section-image') {
        url = `/api/files/images/sections?path=${file_path}`
    } else if (type==='book-image') {
        url =  `/api/files/images/books?path=${file_path}`
    } else if (type==='book-pdf'){
        url = `/api/files/pdfs?path=${file_path}`
    }
    requestPromise = await axiosClient.get(url, data, axiosConfig)
    return requestPromise.data
}

export async function download(type,file_path,) {
    let data = new FormData(); let url;
    data.append('download',true)
    data.append('id',file_path)
    if (type==='profile-image'){
        url = `/api/files/images/profiles?path=${file_path}`
    } else if (type==='section-image') {
        url = `/api/files/images/sections?path=${file_path}`
    } else if (type==='book-image') {
        url =  `/api/files/images/books?path=${file_path}`
    } else if (type==='book-pdf'){
        url = `/api/files/pdfs?path=${file_path}`
    }
    requestPromise = await axiosClient.get(url, data, axiosConfig)
}

export async function upload(type,file,) {
    let data = new FormData(); let url;
    data.append('file',file,file.name)
    if (type==='profile-image'){
        url = `/api/files/images/profiles`
    } else if (type==='section-image') {
        url = `/api/files/images/sections`
    } else if (type==='book-image') {
        url =  `/api/files/images/books`
    } else if (type==='book-pdf'){
        url = `/api/files/pdfs`
    }
    requestPromise = await axiosClient.post(url, data, axiosConfig)
    return requestPromise.data.id
}

export async function update(type,file,previous_id,) {
    let data = new FormData(); let url;
    data.append('id',previous_id)
    if (type==='profile-image'){
        url = `/api/files/images/profiles?path=${file_path}`
    } else if (type==='section-image') {
        url = `/api/files/images/sections?path=${file_path}`
    } else if (type==='book-image') {
        url =  `/api/files/images/books?path=${file_path}`
    } else if (type==='book-pdf'){
        url = `/api/files/pdfs?path=${file_path}`
    }
    requestPromise = await axiosClient.put(url, data, axiosConfig)
    return requestPromise.data.id
}

export async function remove(type,previous_id) {
    let data = new FormData(); let url;
    data.append('id',previous_id)
    if (type==='profile-image'){
        url = `/api/files/images/profiles?path=${file_path}`
    } else if (type==='section-image') {
        url = `/api/files/images/sections?path=${file_path}`
    } else if (type==='book-image') {
        url =  `/api/files/images/books?path=${file_path}`
    } else if (type==='book-pdf'){
        url = `/api/files/pdfs?path=${file_path}`
    }
    requestPromise = await axiosClient.delete(url, data, axiosConfig)
    return 200
}


