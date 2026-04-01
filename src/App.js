import React, { useState } from 'react';

function App() {
  const [file, setFile] = useState(null);
  const [fileName, setFileName] = useState('');

  const handleFileChange = (event) => {
    const uploadedFile = event.target.files[0];
    if (uploadedFile) {
      setFile(uploadedFile);
      setFileName(uploadedFile.name);
    }
  };

  const handleFileUpload = () => {
    if (file) {
      // Placeholder for file analysis logic
      alert(`Uploaded file: ${fileName}`);
    } else {
      alert('Please upload a file first.');
    }
  };

  return (
    <div>
      <h1>File Upload and Analysis</h1>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleFileUpload}>Upload and Analyze</button>
      {fileName && <p>File: {fileName}</p>}
    </div>
  );
}

export default App;