import { useEffect, useState } from "react";
import UploadImage from "../uploadImage/UploadImage.jsx";

function Algebraic() {

   const [images, setImages] = useState()
   const [resImage, setResImage] = useState()

   useEffect(() => {
    console.log("resImage State: ", resImage)
   }, [resImage])

   function handleInputChange(values) {
      console.log("values", values)
      setImages(values) 
   }

  function submitForm(e) {
    e.preventDefault();

    const formData = new FormData(e.target);

    // Adicionando arquivos ao FormData
    images.forEach((file, index) => {
      formData.append(`file${index + 1}`, file);
    });

    const payload = Object.fromEntries(formData)

    console.log(payload, images);

    fetch('http://localhost:5000/upload', {
      method: 'POST',
      body: formData,
    })
    .then(response => response.json())
    .then(data => {
      if (data && data.image) {
        fetch(`http://localhost:5000/images/${data.image}`)
        .then(response => { 
          return response.blob()
        })
        .then(blob => {
            const imageUrl = URL.createObjectURL(blob);
            return imageUrl
        })
        .then(image => setResImage(image))
        .catch(error => console.error('Erro ao carregar a nova imagem:', error));
      }
    })
    .catch(error => {
      console.log("erro", error)
    })
  }

  return (
    <div>
      <h1>Operações Algébricas</h1>
      <UploadImage onInputChange={handleInputChange} />
      <form onSubmit={submitForm}>
        <div>
          <label>Informe a operação: </label>
          <select name="operation">
            <option value="dissolver uniforme">Dissolver Uniforme</option>
            <option value="dissolver cruzado">Dissolver Cruzado</option>
          </select>
        </div>
        <div>
          <label>Informe o valor t: </label>
          <input type="text" name="parameter"/>
        </div>
        <input type="submit" />
      </form>
      {resImage && (
        <img src={resImage} key={resImage} />
      )}
    </div>
  );
}

export default Algebraic;
