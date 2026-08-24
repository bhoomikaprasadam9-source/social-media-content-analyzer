const fileInput = document.getElementById("fileInput");
const uploadBox = document.getElementById("uploadBox");
const fileName = document.getElementById("fileName");
const analyzeBtn = document.getElementById("analyzeBtn");

const loading = document.getElementById("loading");
const error = document.getElementById("error");
const result = document.getElementById("result");
const extractedText = document.getElementById("extractedText");

let selectedFile = null;


// File picker
fileInput.addEventListener("change", function () {
    if (fileInput.files.length > 0) {
        selectedFile = fileInput.files[0];
        fileName.textContent = selectedFile.name;
    }
});


// Drag and drop
uploadBox.addEventListener("dragover", function (event) {
    event.preventDefault();
    uploadBox.classList.add("dragover");
});

uploadBox.addEventListener("dragleave", function () {
    uploadBox.classList.remove("dragover");
});

uploadBox.addEventListener("drop", function (event) {
    event.preventDefault();

    uploadBox.classList.remove("dragover");

    if (event.dataTransfer.files.length > 0) {
        selectedFile = event.dataTransfer.files[0];
        fileName.textContent = selectedFile.name;
    }
});


// Analyze button
analyzeBtn.addEventListener("click", async function () {

    if (!selectedFile) {
        showError("Please select a PDF or image first.");
        return;
    }

    const allowedTypes = [
        "application/pdf",
        "image/png",
        "image/jpeg"
    ];

    if (!allowedTypes.includes(selectedFile.type)) {
        showError("Please upload a PDF, PNG, or JPG file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", selectedFile);

    loading.classList.remove("hidden");
    error.classList.add("hidden");
    result.classList.add("hidden");

    try {

        const response = await fetch(
            "/extract",
            {
                method: "POST",
                body: formData
            }
        );

        const data = await response.json();

        if (!response.ok) {
            throw new Error(data.detail || "Something went wrong.");
        }

        extractedText.textContent =
            data.text || "No text could be extracted from this file.";

        result.classList.remove("hidden");

    } catch (err) {

        showError(err.message);

    } finally {

        loading.classList.add("hidden");

    }
});


function showError(message) {
    error.textContent = message;
    error.classList.remove("hidden");
}