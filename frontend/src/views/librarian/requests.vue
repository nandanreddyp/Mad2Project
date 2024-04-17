<template>
    <form class="collection-header">
        <div class="collection-title">User Requests</div>
        <div class="collection-sort">
            Sort by
            <select title="sort by" v-model="sort" @change="runSearch" name="sort" id="">
                <option value="newest" >Recent</option>
                <option value="oldest" >Oldest</option>
            </select>
        </div>
    </form>
    <div class="collection-container" v-on:scroll="handleScroll" ref="requestsContainer">
        <table>
            <thead>
                <tr>
                    <th>User</th>
                    <th>Book</th>
                    <th>Status</th>
                    <th>Request Date</th>
                    <th>Return Date</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                <tr v-for="request in requests" :key="request.id">
                    <td>name</td> <!-- Assuming user has a 'name' attribute -->
                    <td>book name</td> <!-- Assuming book has a 'title' attribute -->
                    <td>status of request</td>
                    <td>when asked</td>
                    <td>when return</td>
                    <td class="action-buttons">
                        <button @click="issueRequest(request.id)">Issue</button>
                        <button @click="rejectRequest(request.id)">Reject</button>
                    </td>
                </tr>
            </tbody>
        </table>
    </div>

</template>

<script>
import axiosClient from '@/services/axios';

export default {
    data() {return{
        requests: [
            {},{},{}
        ],
        page: 1,
        per_page: 7,
        has_next: null,
        loading: true,
        // filter
        sort: 'newest'
    }},
    methods: {
        runSearch() {
            this.page=1; this.authors=[]; this.has_next = null
        },
        loadRequests() {
            axiosClient.get(`/api/librarian/requests`)
            .then(resp => {
                resp.data.requests.forEach(obj => {
                    this.requests.push(obj)
                })
                this.loading = true; // Remove the comma and semicolon instead
            })
        },
        issueRequest(requestId) {

        },
        rejectRequest(requestId) {

        }
    }
}
</script>

<style>
.collection-header {
    display: flex; align-items: center; justify-content: space-between;
    padding: 10px;
}
.collection-header input, .collection-header button, .collection-header select{
    padding: 3px;
}
.collection-title {
    font-size: 20px;
    font-weight: 700;
    padding: 5px;
}
.collection-container {
    flex: 1; overflow: auto;
}

.table-container {
  width: 100%;
  overflow-x: auto;
  white-space: nowrap; /* Prevent line breaks in table cells */
}

table {
  min-width: 100%; /* Ensure table takes up full width of container */
  border-collapse: collapse;
}

th, td {
  padding: 8px;
  border-bottom: 1px solid #ddd;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

.action-buttons {
  display: flex;
  gap: 10px;
}

/* Responsive styles */
@media screen and (max-width: 600px) {
  table {
    font-size: 12px; /* Adjust font size for smaller screens */
  }
}
</style>