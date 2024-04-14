<template>
    <div>
      <input type="file" @change="handleFileChange" accept=".pdf">
      <img :src="firstPageImage" v-if="firstPageImage">
    </div>
  </template>
  
  <script>
  import pdfjsLib from 'pdfjs-dist/webpack';
  
  export default {
    data() {
      return {
        firstPageImage: null
      };
    },
    methods: {
      async handleFileChange(event) {
        const file = event.target.files[0];
        if (!file) return;
  
        try {
          const pdf = await pdfjsLib.getDocument(URL.createObjectURL(file));
          const page = await pdf.getPage(1);
          const viewport = page.getViewport({ scale: 1 });
  
          const canvas = document.createElement('canvas');
          const context = canvas.getContext('2d');
          canvas.height = viewport.height;
          canvas.width = viewport.width;
  
          const renderContext = {
            canvasContext: context,
            viewport: viewport
          };
  
          await page.render(renderContext).promise;
          const imageData = canvas.toDataURL('image/png');
          this.firstPageImage = imageData;
        } catch (error) {
          console.error('Error loading PDF:', error);
        }
      }
    }
  };
  </script>
  