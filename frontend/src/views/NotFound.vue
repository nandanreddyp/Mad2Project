<template>
    <div class="not-found">
      <h1>404 - Page Not Found</h1>
      <p>The page you are looking for does not exist.</p>
      <button @click="goBack">Go Back</button>
    </div>
  </template>
  
  <script>
  export default {
    methods: {
      goBack() {
        // Navigate back to the previous page
        this.$router.go(-1);
      }
    }
  };
  </script>
  
  <style scoped>
  .not-found {
    text-align: center;
    padding: 20px;
    margin: auto;
  }
  .not-found button {
    padding: 10px 20px;
    background-color: #007bff;
    color: #fff;
    border: none;
    border-radius: 4px;
    cursor: pointer;
    transition: background-color 0.3s;
  }
  .not-found button:hover {
    background-color: #0056b3;
  }
  </style>
  