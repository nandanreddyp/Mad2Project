<template>
    <div class="collection-title">
        <svg style="margin-bottom: 10px; stroke: #6b9bd2;" xmlns="http://www.w3.org/2000/svg" fill="#000000" width="30px" height="30px" viewBox="0 0 16 16" id="request-send-16px"><path id="Path_44" data-name="Path 44" d="M-18,11a2,2,0,0,0,2-2,2,2,0,0,0-2-2,2,2,0,0,0-2,2A2,2,0,0,0-18,11Zm0-3a1,1,0,0,1,1,1,1,1,0,0,1-1,1,1,1,0,0,1-1-1A1,1,0,0,1-18,8Zm2.5,4h-5A2.5,2.5,0,0,0-23,14.5,1.5,1.5,0,0,0-21.5,16h7A1.5,1.5,0,0,0-13,14.5,2.5,2.5,0,0,0-15.5,12Zm1,3h-7a.5.5,0,0,1-.5-.5A1.5,1.5,0,0,1-20.5,13h5A1.5,1.5,0,0,1-14,14.5.5.5,0,0,1-14.5,15ZM-7,2.5v5A2.5,2.5,0,0,1-9.5,10h-2.793l-1.853,1.854A.5.5,0,0,1-14.5,12a.493.493,0,0,1-.191-.038A.5.5,0,0,1-15,11.5v-2a.5.5,0,0,1,.5-.5.5.5,0,0,1,.5.5v.793l1.146-1.147A.5.5,0,0,1-12.5,9h3A1.5,1.5,0,0,0-8,7.5v-5A1.5,1.5,0,0,0-9.5,1h-7A1.5,1.5,0,0,0-18,2.5v3a.5.5,0,0,1-.5.5.5.5,0,0,1-.5-.5v-3A2.5,2.5,0,0,1-16.5,0h7A2.5,2.5,0,0,1-7,2.5Zm-7.854,3.646L-12.707,4H-14.5a.5.5,0,0,1-.5-.5.5.5,0,0,1,.5-.5h3a.5.5,0,0,1,.191.038.506.506,0,0,1,.271.271A.5.5,0,0,1-11,3.5v3a.5.5,0,0,1-.5.5.5.5,0,0,1-.5-.5V4.707l-2.146,2.147A.5.5,0,0,1-14.5,7a.5.5,0,0,1-.354-.146A.5.5,0,0,1-14.854,6.146Z" transform="translate(23)"/></svg>
        User Requests</div>
    <div class="collection-container">
        <div class="active-requests-container">
            <div class="table-container">
                <table>
                    <thead>
                        <tr>
                            <th>Sl.no</th>
                            <th>User name</th>
                            <th>Book name</th>
                            <th>Requested on</th>
                            <th>Return date</th>
                            <th>Action</th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr v-for="(request, index) in requests" :key="request.id">
                            <td>{{ index+1 }}</td>
                            <td>{{ request.user_name }}</td>
                            <td>{{ request.book_name }}</td>
                            <td>{{ formatISODate(request.created_datetime) }}</td>
                            <td>{{ formatISODate(request.end_datetime) }}</td>
                            <td>
                                <button @click="issueRequest(request.id)" >Issue</button>
                                <button @click="rejectRequest(request.id)" >Reject</button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
        </div>
    </div>
</template>

<script>
import axiosClient from '@/services/axios';

export default {
    data() {return{
        requests: [
        ],
    }},
    methods: {
        loadRequests() {
            axiosClient.get(`/api/librarian/requests`)
            .then(resp => {
                console.log(resp)
                this.requests = resp.data.requests
            })
        },
        formatISODate(isoDate) {
            const date = new Date(isoDate);
            return date.toLocaleDateString();
        },
        issueRequest(reqid) {
            axiosClient.put(`/api/librarian/requests/${reqid}`)
            .then(resp => {
                this.requests = this.requests.filter(request => request.id !== reqid);
            })
        },
        rejectRequest(reqid) {
            axiosClient.delete(`/api/librarian/requests/${reqid}`)
            .then(resp => {
                this.requests = this.requests.filter(request => request.id !== reqid);
            })
        }
    },
    mounted() {
        this.loadRequests()
    }
}
</script>

<style>
.collection-title {
    font-size: 20px;
    font-weight: 700;
    padding: 10px 10px;
    display: flex; align-items: center; gap: 6px;
}
.collection-container {
    flex: 1; overflow: auto;
}
/* table collection styling */
.active-requests-container .collection-title, .completed-requests-container .collection-title {
    padding-left: 25px;
}
.table-container {
    width: 100%;
    display: block; overflow-x: auto;
}
table {
    padding: 0 10px;
    width: 100%; 
}
table thead th {
    background-color: black;
    padding: 10px; font-size: 13px; font-weight: 500; color: gray;
}
table tbody tr {
    margin-bottom: 10px;
}
</style>