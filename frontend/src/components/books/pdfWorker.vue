<template>

    <label for="pdf-file">PDF File</label>
    <input ref="pdf" type="file" id="pdf-file" accept="application/pdf" required>

    <div class="preview-box">
        <label for="image-file">Cover Image</label>
        <img id="image-file-preview" src="" alt="">
        <input ref="image" @change="showSelectedImage" type="file" id="image-file"  accept="image/*">
    </div>

    <label for="page-count">Page Count</label>
    <input ref="count" type="number" id="page-count" name="page_count" min="1" required><br><br>

</template>
  
  <script>
  
  export default {
    data() {
      return {
        image_file_selected: false,
      };
    },
    methods: {
        togglePreview() {
            this.image_file_selected = true;
        },
        showSelectedImage() {
            this.togglePreview()
            const image_file = document.getElementById("image-file");
            const image_file_preview = document.getElementById("image-file-preview");
            const files = image_file.files[0];
            if (files) {
                const fileReader = new FileReader();
                fileReader.readAsDataURL(files);
                fileReader.addEventListener("load", function () {
                image_file_preview.src = this.result
                });    
            } else {
                image_file_preview.src = ''
            }
        },
        handleChange(event) {
            console.log(event)
        },
        sendDataToParent() {
            const pdf = this.$refs.pdf.files[0]
            const image = this.$refs.image.files[0]
            const count = this.$count.value

        }
    },
    mounted() {
        let scriptElement = document.createElement('script');
        scriptElement.src = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.11.338/pdf.min.js";
        document.head.appendChild(scriptElement)

        scriptElement = document.createElement('script')
        scriptElement.textContent = `
        document.getElementById('pdf-file').addEventListener('change', function(event) {
          var file = event.target.files[0];
          var reader = new FileReader();
          
          reader.onload = function() {
              var pdfData = new Uint8Array(this.result);

              // Load the PDF file
              pdfjsLib.getDocument({ data: pdfData }).promise.then(function(pdf) {
                  // Get the total number of pages
                  var pageCount = pdf.numPages;

                  // Set the page count in the input field
                  document.getElementById('page-count').value = pageCount;

                  // Fetch the first page
                  return pdf.getPage(1);
              }).then(function(page) {
                  var viewport = page.getViewport({ scale: 1.0 });
                  var canvas = document.createElement('canvas');
                  var context = canvas.getContext('2d');
                  canvas.height = viewport.height;
                  canvas.width = viewport.width;

                  // Render the page onto the canvas
                  var renderTask = page.render({ canvasContext: context, viewport: viewport }).promise;
                  renderTask.then(function() {
                      // Convert the canvas to an image
                      var imageUrl = canvas.toDataURL();

                      // Create a new input element for the image
                      var imageInput = document.getElementById('image-file');

                      // Set the image data as the value of the input
                      var blob = dataURLToBlob(imageUrl);
                      var file = new File([blob], 'image.png', { type: 'image/png' });
                      var dataTransfer = new DataTransfer();
                      dataTransfer.items.add(new File([blob], 'extracted_image.png', { type: 'image/png' }));
                      imageInput.files = dataTransfer.files;

                      imageInput.dispatchEvent(new Event('change'));

                      // Trigger the file input
                      // imageInput.click();
                  });
              });
          };

          reader.readAsArrayBuffer(file);
      });

      // Helper function to convert data URL to Blob
      function dataURLToBlob(dataURL) {
          var parts = dataURL.split(';base64,');
          var contentType = parts[0].split(':')[1];
          var raw = window.atob(parts[1]);
          var rawLength = raw.length;
          var uInt8Array = new Uint8Array(rawLength);

          for (var i = 0; i < rawLength; ++i) {
              uInt8Array[i] = raw.charCodeAt(i);
          }

          return new Blob([uInt8Array], { type: contentType });
      }
        `;
        document.body.appendChild(scriptElement);

    },
  };
  </script>
  
<style scoped>
.preview-box {
    display: flex; flex-direction: column;
}
  #image-file-preview {
    height: 200px; display: flex; justify-content: center;
    object-fit: contain;
    border: 1px solid black;
  }
  
#book-form {
    width: 100%;
    margin: 0 auto;
    padding: 20px;
    border: 1px solid #ccc;
    border-radius: 5px;
}

label {
    display: block;
    margin-bottom: 5px;
}

input[type="text"],
input[type="number"],
input[type="file"],
input[type="date"],
textarea {
    width: 100%;
    padding: 8px;
    margin-bottom: 10px;
    border: 1px solid #ccc;
    border-radius: 3px;
}


</style>