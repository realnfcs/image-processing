import { useState } from "react";

function UploadImage({ onInputChange }) {

   function handleOnChange(e) {
      const selectedFiles = e.target.files;

      // Convertendo a lista de arquivos para um array
      const fileList = Array.from(selectedFiles);

      fileList.forEach((file, index) => {

         const reader = new FileReader();

         // Configurando o evento onload para a leitura do arquivo
         reader.onload = function () {

            // Se for a última imagem, criar o objeto JSON e chamar a função de callback
            if (index === fileList.length - 1) {
               const jsonDataList = fileList.map((file, i) => ({
                  imagem: reader.result.split(',')[1],
               }));

               console.log(jsonDataList)

               // Chamando a função de callback fornecida no componente pai
               onInputChange(jsonDataList);
            }
         }
      })
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
      { /*img src={preview} className="preview"/> */ }
    </div>
  );
}

export default UploadImage;
