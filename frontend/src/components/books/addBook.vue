<template>
    <div class="popup-bg">
        <div class="popup">
            <div class="popup-header">Create Book</div>
            <div class="body">
                <form ref="myForm" id="book-form">

                    <label for="name">Book Name</label>
                    <input ref="name" type="text" id="name" name="name" required><br><br>
                    
                    <div class="book-description">
                        <label for="description">Description</label>
                        <textarea ref="description" id="description" name="description" placeholder="Description about this books"></textarea>
                    </div><br>

                    <label for="pdf_file">PDF File</label>
                    <input ref="PDF" type="file" id="pdf_file" accept="application/pdf" ><br>

                    <label for="img_file">Cover Image</label>
                    <div style="display: flex; justify-content: center; margin-bottom: 6px;">
                        <img id="selectedImgPreview" class="" src="" alt=""> <!--add visible class to show-->
                    </div>
                    <input @change="showSelectedImage" ref="IMG" type="file" id="img_file"  accept="image/*"><br><br>

                    <label for="page-count">Page Count</label>
                    <input ref="page_count" type="number" id="page_count" name="page_count" min="1" ><br><br>
           
                    <label for="publication-date">Publication Date</label>
                    <input ref="date" type="date" id="publication_date" name="publication_date"><br><br>
                    
                    <label for="isbn">ISBN</label>
                    <input ref="isbn" type="number" id="isbn" name="isbn"><br><br>
                    
                </form>
            </div>
            <div class="popup-options">
                <button class="ok" @click="checkForm" >Submit</button>
                <button class="cancel" @click="toggleAddBook">Cancel</button>
            </div>
        </div>
    </div>
</template>

<script>
import axiosClient from '@/services/axios'

export default {
    components: {
    },
    data() {return {
        formdata: {
            name: '',
            description: '',
            publication_date: '',
            isbn: '',
            pdf_file: null,
            image_file: null,
            page_count: '',
        },
    }},
    methods:{
        showSelectedImage() {
            const image_file = document.getElementById("img_file");
            const image_file_preview = document.getElementById("selectedImgPreview");
            const files = image_file.files[0];
            if (files) {
                image_file_preview.classList.add('visible')
                const fileReader = new FileReader();
                fileReader.readAsDataURL(files);
                fileReader.addEventListener("load", function () {
                image_file_preview.src = this.result
                });    
            } else {
                image_file_preview.classList.remove('visible')
                image_file_preview.src = ''
            }
        },
        checkForm(){
            if (this.$refs.myForm.reportValidity()) {
                this.formdata.name = this.$refs.name.value
                this.formdata.description = this.$refs.description.value
                this.formdata.publication_date = this.$refs.date.value
                this.formdata.isbn = this.$refs.isbn.value
                this.formdata.page_count = this.$refs.page_count.value
                this.formdata.pdf_file = this.$refs.PDF.files[0]
                this.formdata.image_file = this.$refs.IMG.files[0]
                this.submitForm()
            }
        },
        submitForm() {
            axiosClient.post('/api/books',this.formdata,{
                headers:{
                    'Content-Type': 'multipart/form-data',
                }
            })
            .then(resp => {
                this.toggleAddBook()
                this.addedToast()
            })
        },
    },
    props: {
        toggleAddBook: Function, addedToast: Function, 
    },
    mounted() {
        let scriptElement = document.createElement('script'); // cdn injecting
        scriptElement.src = "https://cdnjs.cloudflare.com/ajax/libs/pdf.js/2.11.338/pdf.min.js";
        document.head.appendChild(scriptElement)
        scriptElement = document.createElement('script') // script injecting
        scriptElement.textContent = `
        document.getElementById('pdf_file').addEventListener('change', function(event) {
          var file = event.target.files[0];
          var reader = new FileReader();
          if (file) {
            reader.onload = function() {
                var pdfData = new Uint8Array(this.result);

                // Load the PDF file
                pdfjsLib.getDocument({ data: pdfData }).promise.then(function(pdf) {
                    // Get the total number of pages
                    var pageCount = pdf.numPages;

                    // Set the page count in the input field
                    document.getElementById('page_count').value = pageCount;

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
                        var imageInput = document.getElementById('img_file');

                        // Set the image data as the value of the input
                        var blob = dataURLToBlob(imageUrl);
                        var file = new File([blob], 'image.png', { type: 'image/png' });
                        var dataTransfer = new DataTransfer();
                        dataTransfer.items.add(new File([blob], 'extracted_image.png', { type: 'image/png' }));
                        imageInput.files = dataTransfer.files;

                        imageInput.dispatchEvent(new Event('change')); // important to trigger evet
                    });
                });
            }    
            reader.readAsArrayBuffer(file);
          } else {
            var imageInput = document.getElementById('img_file')
            imageInput.files = null
            imageInput.value = ''

            var image_file_preview = document.getElementById("selectedImgPreview")
            image_file_preview.classList.remove('visible')
            image_file_preview.src = ''

            // set pagecount to none
            document.getElementById('page-count').value = null;
          }
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
        document.body.appendChild(scriptElement); // script injection done
    },
}
</script>

<style scoped>
/* popup */
.popup-bg {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background-color: rgba(0, 0, 0, 0.5);
    display: flex;
    justify-content: center;
    align-items: center;
}
.popup {
    background-color: #fff;
    border-radius: 10px;
    padding: 20px;
    box-shadow: 0 0 10px rgba(0, 0, 0, 0.5);
    max-width: 580px;
    width: 100%;
    max-height: 550px;
    height: 100%;
    /* overflow-y: auto; */
    display: flex; flex-direction: column;
}

/* heading */
.popup-header {
    font-family: Roboto,Arial,sans-serif;
    font-size: 20px;
    font-weight: 400;
    letter-spacing: 0;
    line-height: 26px;
    color: #e8e8e8;
    overflow: hidden;
    text-align: left;
    text-overflow: ellipsis;

    width: 100%;
    color: #2a2929;
    overflow: hidden;
    white-space: nowrap; /* Prevents wrapping of text */
    text-overflow: ellipsis; /* Add ellipsis for overflowed text */
    margin: 0px auto; /* Center the text horizontally */
    margin-bottom: 5px;
    text-align: center;
}

/* body */
div.body {
    flex: 1; overflow-y: auto;
    display: flex; flex-direction: column;
    align-items: center;
}
.ratings-container {
    display: flex; flex-direction: column; align-items: center;
    padding: 25px;
}
.review-stars {
    display: flex;
    align-items: center;
}
.review-stars input {
    display: none;
}
.book-description {
    width: 100%;
}
.book-description textarea {
    width: 100%; height: 150px;
    padding: 10px;
    border: 1px solid #ccc;
    border-radius: 5px;
    /* margin: 16px 0px; */
    line-height: 1.5rem;
    resize: none;

    font-family: Roboto, Arial, sans-serif;
    font-size: 0.9rem;
    letter-spacing: .00625em;
    font-weight: 400;
}

/* form css */
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

/* selected image */
#selectedImgPreview.visible {
    display: unset;
    width: 100px; background-color: black; height: 150px;
    object-fit: cover;
}
#selectedImgPreview {
    display: none;
}


/* footer */
.popup-options {
    width: 100%; margin-top: 5px;
    display: flex; justify-content: space-evenly;
}
.popup-options button {
    padding: 10px 20px;
    margin: 0 10px;
    color: #333;
    border: none;
    border-radius: 50px;
    cursor: pointer;
}
.popup-options button.ok {
    color: rgb(32, 33, 36);
    background-color: rgb(138,180,248);
}
.popup-options button.cancel {
    border: 1px solid black;
    color: #333;
}
.popup-options button:hover {
    transform: translate(-2px, 1px);
}
</style>
