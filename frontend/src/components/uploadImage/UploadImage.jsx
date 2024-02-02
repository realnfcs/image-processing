import { useState } from "react";

function UploadImage({ onInputChange }) {

   function handleOnChange(e) {
      const selectedFiles = e.target.files;

      // Convertendo a lista de arquivos para um array
      const fileList = Array.from(selectedFiles);
      //console.log(fileList)

      onInputChange(fileList)
   }

  return (
    <div className="dropzone">
      <input 
         type="file" 
         name="image" 
         onChange={handleOnChange} 
         accept="image/png, image/jpg, image/tif, image/tiff, image/bmp"
         multiple
      />
    </div>
  );
}

export default UploadImage;
